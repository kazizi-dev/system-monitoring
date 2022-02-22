import config
import requests

class ElasticService():
    """
    class responsible for maintaining connection to Elasticsearch
    and limiting the user to allowed operations only.
    """

    def __init__(self) -> None:
        self.client_url = config.ELASTIC_URL

    
    # check if index name is valid
    def __does_index_exist(self, index):
        response = requests.get(
            self.client_url + '/_cat/indices', 
            data="", 
            auth=(config.ELASTIC_USER, config.ELASTIC_PWD), 
            verify=True, 
            headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        )

        return True if index in response.text else False
        

    # query data from elasticsearch index
    def get_query_response(self, index, query):
        if self.__does_index_exist(index):
            response = requests.get(
                f"{self.client_url}/{index}/_search", 
                data=query,
                auth=(config.ELASTIC_USER, config.ELASTIC_PWD), 
                verify=True, 
                headers={'Accept': 'application/json', 'Content-type': 'application/json'}
            )

            return response.json()
        
        return {}