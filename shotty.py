import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    print(response)