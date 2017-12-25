"""
App to fecth secrets from dynmodb
"""
import os
import json
import yaml
import boto3


class App(object):
    """
    Application class that holds the logic functios
    """
    def __init__(self):
        """
        Constructor to load boto3 dynmodb class
        """
        with open("app/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.client = boto3.client('dynamodb', region_name='{}'.format(cfg['aws']['region_name']))
        # self.client = boto3.client('dynamodb', region_name='{}'.format(cfg['aws']['region_name']), \
        # aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],\
        # aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])


    def fetch_secret(self, table_name, key):
        """
        Function to get secret
        """
        secret = self.client.get_item(TableName='{}'.format(table_name), \
                                 Key={"code_name":{"S": '{}'.format(key)}})
        secret_json = json.dumps(secret['Item'])
        #result = pprint.pprint(pretty_result)
        return secret_json

    def health_check(self, container, project):
        """
        health check function, return project info and app status
        """
        data = {'container' : "{}".format(container), 'project' : "{}"\
                .format(project), 'status' : "healthy"}
        health = json.dumps(data, sort_keys=True, indent=4)

        return health