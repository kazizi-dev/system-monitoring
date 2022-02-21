from datetime import datetime
from urllib import request
from elasticsearch import Elasticsearch
import certifi
import config
from colorama import Fore, Style
import json
import requests

class ElasticService():
    """
    class responsible for maintaining connection to Elasticsearch
    and limiting the user to allowed operations only.
    """

    def __init__(self) -> None:
        self.client_url = config.ELASTIC_URL

    
    # check if index name is valid
    def does_index_exist(self, index):
        headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        response = requests.get(
            self.client_url + '/_cat/indices', 
            data="", 
            auth=(config.ELASTIC_USER, config.ELASTIC_PWD), 
            verify=True, 
            headers = headers)

        if index in response.text:
            print(f"{Fore.GREEN}[Elasticsearch]: index found{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}[Elasticsearch]: index not found{Style.RESET_ALL}")
            return False
        

    # query data from elasticsearch index
    def get_query_response(self, index, query):
        if self.does_index_exist(index):
            headers={'Accept': 'application/json', 'Content-type': 'application/json'}        
            response = requests.get(
                f"{self.client_url}/{index}/_search", 
                data='{"query": {"match_all": {}}}', 
                auth=(config.ELASTIC_USER, config.ELASTIC_PWD), 
                verify=True, 
                headers = headers)

            return response.json()
        
        return {}