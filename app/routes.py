import datetime

from flask import current_app as app
from flask import render_template, request, flash

from app.src import instance_data, app_health, instance_shutdown_scheduling
from app.src.instance_actions import select_action
from datetime import datetime

from prometheus_client import start_http_server, Gauge, Counter

start_http_server(9333, '0.0.0.0')
request_counter = Counter('num_of_requests_total', 'num_page_accesses', ['method', 'endpoint'])
request_counter.labels('get', '/home')
request_counter.labels('get', '/about')
request_counter.labels('get', '/instances')
request_counter.labels('get', '/scheduler')
request_counter.labels('get', '/health')
request_counter.labels('get', '/metrics')

@app.route("/")
@app.route("/home")
def home():
    request_counter.labels('get', '/home').inc()
    page = request.args.get('page', 1, type=int)
    return render_template('home.html')


@app.route("/about")
def about():
    request_counter.labels('get', '/about').inc()
    return render_template('about.html', title='About')


@app.route("/instances", methods=['GET'])
def instances():
    request_counter.labels('get', '/get').inc()
    instance_data_output = instance_data.get_instances(*request.args)
    return render_template('instances.html', title='Instances',
                           providers=instance_data_output["providers"])


@app.route("/instances/<string:instance_id>/<string:instance_action>", methods=['GET', 'POST'])
def instance_actions(instance_id, instance_action):
    try:
        select_action(instance_action)(instance_id)
        flash("Your request to {} instance {} is in progress".format(instance_action, instance_id), "info")
    except Exception:
        flash("Cannot perform action '{}' on instance: {}".format(instance_action, instance_id), "danger")

    instance_data_output = instance_data.get_instances()
    return render_template('instances.html', title='Instances', providers=instance_data_output["providers"])


@app.route("/scheduler", methods=['GET', 'POST'])
def scheduler():
    request_counter.labels('get', '/scheduler').inc()
    if request.method == 'POST':
        instance_shutdown_scheduling.handle_instance(request.form)

    scheduled_instances = instance_shutdown_scheduling.get_scheduled_instances()
    return render_template('scheduler.html', title='Scheduling',
                           scheduled_instances=scheduled_instances["Instances"])


@app.route("/health", methods=['GET'])
def health():
    request_counter.labels('get', '/health').inc()
    health_metrics, is_app_healthy = app_health.get_app_health()

    return render_template('health.html', title='Application Health',
                           healthchecks=health_metrics), 200 if is_app_healthy else 500


@app.route("/metrics", methods=['GET'])
def metrics():
    request_counter.labels('get', '/metrics').inc()
    return render_template('metrics.html', title='metrics', )


@app.template_filter()
def format_datetime(timestamp):
    date_value = datetime.fromtimestamp(timestamp / 1000)
    return date_value.strftime("%d/%m/%y %H:%M:%S")


@app.template_filter()
def today_scheduling(hour):
    now = datetime.now()
    today_scheduling_time = now.replace(second=0, microsecond=0, minute=0, hour=hour)
    return today_scheduling_time.strftime("%d/%m/%y %H:%M:%S")
