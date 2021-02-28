import boto3
import botocore

def get_machine_time():
    # TODO: implement real call to get machine time in milliseconds. If attempt is not possible, return 0
    return 1602824750094


def check_aws_connection():
    # TODO: implement real call to aws describe instances. If successful, return true. otherwise return False
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    try:
        ec2_client.describe_instances()
    except botocore.exceptions.ProfileNotFound as err:
        print("The error is :" , err)
        return False
    else:
        return True


def check_db_connection():
    # TODO: implement real select query to db. If successful, return true. otherwise return False
    return True


def is_app_healthy(healthchecks):
    return all([check["Value"] for check in healthchecks])


def get_app_health():
    healthchecks = [
        {"Name": "machine-time", "Value": get_machine_time()},
        {"Name": "aws-connection", "Value": check_aws_connection()},
        {"Name": "db-connection", "Value": check_db_connection()},
    ]

    return healthchecks, is_app_healthy(healthchecks)
