
import click
from pprint import pprint
import boto3
import botocore
import jmespath


@click.group()
@click.option('--debug/--no-debug', default=False, help='Run command on debug mode')
@click.pass_context
def kancli(ctx, debug):
    # click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    ctx.obj['DEBUG'] = debug
    

def extrected_data(instances, region):

    return_extracted_data = { "name": region }
    data_object = "Reservations[*].Instances[*].{InstanceId: InstanceId, InstanceType: InstanceType, LaunchTime: LaunchTime, \
    State: State.Name, MacAddress: NetworkInterfaces[0].MacAddress, NetworkInterface: NetworkInterfaces[0].NetworkInterfaceId, PrivateIpAddress: PrivateIpAddress \
    RootDeviceName: RootDeviceName, RootDeviceType: RootDeviceType, SecurityGroups: SecurityGroups, StateReason: StateReason \
    Tags: Tags}"
    response_filtered = jmespath.search(data_object, instances)
    return_extracted_data["instances"] = [insta[0] for insta in response_filtered]
    return return_extracted_data


@kancli.command()
@click.pass_context
def get_instances(ctx):
    kandula_instances_data = { "providers": [
        {"name": "aws",
        "regions": [
        ]}
    ]}
    regions_items = {}

    # Get list of regions i used hardcoded because i am using only one region
    ec2_client = boto3.client('ec2', region_name = 'us-east-1')
    regions = ['us-east-1','us-west-2', 'us-east-2']

    for region in regions:
        try:
            current_session = boto3.Session(region_name = region)
            ec2_client = current_session.client('ec2')
            answer = ec2_client.describe_instances()
            regions_items = extrected_data(answer, region)
            kandula_instances_data["providers"][0]["regions"].append(regions_items)
        except botocore.exceptions.ClientError as error:
            print("There is error with the aws client, ", error)
    
    if ctx.obj['DEBUG']:
        click.echo(pprint(kandula_instances_data))
    
    return kandula_instances_data



if __name__ == '__main__':
    kancli(obj={})
