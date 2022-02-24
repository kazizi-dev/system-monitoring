import sys
import pandas as pd
from tabulate import tabulate
from colorama import Fore
from elasticservice import ElasticService
from slackservice import SlackService
from jiraservice import JiraService
import config
from datetime import datetime

def populate_es_with_data():
    elastic = ElasticService()
    elastic.populate_index_with_data(config.INDEX, config.ELASTIC_DATA)
        
def get_data_as_df(index, type, value):
    service = ElasticService()
    
    query = ""
    if value == "all":
        query = """{
            "size": 10000,
            "query": {"match_all": {}},
            "_source": ["timestamp","group","message","error_code","severity"]
        }"""
    else:
        query = ("""{
            "size": 10000,
            "query": {"bool": {"filter": [{"term": {"%s": "%s"}}]}},
            "_source": ["timestamp","group","message","error_code","severity"]
        }""" % (type, value))
    
    result = []
    result.append(service.get_query_response(index, query))

    dfs = []
    for res in result:
        df = pd.DataFrame.from_dict([document['_source'] for document in res['hits']['hits']])
        dfs.append(df)

    return pd.concat(dfs, join='outer', ignore_index=True)


def create_jira_issue(df):
    jira = JiraService()

    # clean up data
    # filter = "error"
    # jira.delete_tickets(filter)

    groups = df['group']
    errors = df['error_code']
    messages = df['message']
    severities = df['severity']

    description = []
    for i in range(len(df)):
        description.append(f"[team]: {groups[i]}, [error]: {errors[i]}, [message]: {messages[i]}, [severity]: {severities[i]}")
    description = "\n".join(description)
    summary = f"Errors [{str(datetime.utcnow())[0:10]}]"
    ticket_type = "Bug"

    jira.create_ticket(summary, description, ticket_type)


def create_slack_alert(df):     
    text = []
    text.append(f"Detected {len(df)} issues!\n")
    text.append(f"Impacted teams:\n")
    for team in list(set(df['group'])):
        text.append(f"  :small_red_triangle: {team}")
    text = "\n".join(text)

    slack = SlackService()
    slack.send_alert_to_slack(text, "analytics")


if __name__ == "__main__":
    filter_type = sys.argv[1:][0]
    filter_value = sys.argv[1:][1]

    # skip if data is present
    # populate_es_with_data()

    df = get_data_as_df(config.INDEX, filter_type, filter_value)

    create_slack_alert(df)
    create_jira_issue(df)

    print(Fore.LIGHTGREEN_EX + tabulate(df, headers = 'keys', tablefmt = 'psql') + Fore.RESET)
