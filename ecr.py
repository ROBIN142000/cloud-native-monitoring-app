import boto3

client = boto3.client('ecr')

repository_name = "my-cloud-native-repo"
response = client.create_repository(
    repositoryName=repository_name,
    tags=[
            {
                'Key': 'repo',
                'Value': 'monitor-app'
            },
        ],
)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)