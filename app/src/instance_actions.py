import boto3
import botocore
import jmespath
import click
from pprint import pprint

## do we need to implement list of ids
## add region option 
## add dry-run option 

@click.group()
@click.option('--debug/--no-debug', default=False, help='Run command on debug mode')
@click.option('--instance_id', prompt='Enter the instance_id',help='The instance which action will be on.')
@click.pass_context
def kancli(ctx, debug, instance_id):
    ctx.obj['DEBUG'] = debug
    ctx.obj['BOTO_CLIENT'] = boto3.client('ec2', region_name="us-east-1")
    ctx.obj['INSTANCE_ID'] = instance_id
    

@kancli.command()
@click.pass_context
def start_instance(ctx):
    client = ctx.obj['BOTO_CLIENT']
    ec2 = boto3.resource('ec2', region_name="us-east-1")
    instance = ec2.Instance(ctx.obj['INSTANCE_ID'])

    if instance.state['Name'] == 'stopping':
        response = client.start_instances(InstanceIds=[ctx.obj['INSTANCE_ID']])
        click.echo("Sent request to start instance: " + ctx.obj['INSTANCE_ID'])
        if ctx.obj['DEBUG']:
            pprint(response)
    else:
        click.echo("{} is in {} state".format(ctx.obj['INSTANCE_ID'], instance.state['Name']))




def stop_instance(instance_id):
    # TODO: replace this print to a real call to stop instance
    print("Sent request to stop instance: ", instance_id)


def terminate_instance(instance_id):
    # TODO: replace this print to a real call to terminate instance
    print("Sent request to terminate instance: ", instance_id)


def no_action_found(instance_id):
    raise RuntimeError("Unknown instance action selected")


def select_action(instance_action):
    return {
        'start': start_instance,
        'stop': stop_instance,
        'terminate': terminate_instance
    }.get(instance_action, no_action_found)



if __name__ == '__main__':
    kancli(obj={})
