import config
import pandas as pd
import slack
import json
from datetime import datetime

class SlackService():
    """
    class responsible for sending Slack alerts.
    """

    def __init__(self) -> None:
        self.client = slack.WebClient(config.SLACK_TOKEN)

    def __get_slack_json_msg(self, df):
        """
        build the json data for slack
        """

        result = []
        result.append(f"""Detected {len(df)} issues!\n""")
        result = "\n".join(result)

        json_message = json.dumps([{
            "footer": "",
            "footer_icon": "",
            "title": f"Metrics Report\n",
            "text": f"{result}\n\n\n",
            "color":"#008bcf",
            "attachment_type":"default", 
            "actions":[
                {
                    "name":"elastic", "text":"Dashboard", "type":"button", "value":"Yes", "style": "primary",
                    "url": config.DASHBOARD_LINK
                },
                {
                    "name":"jira", "text":"Jira", "type":"button", "value":"Yes", "style":"danger",
                    "url": config.JIRA_LINK
                }
            ]
        }])

        return json_message
    

    def send_alert_to_slack(self, df, slack_channel):
        if len(df) > 0:
            self.client.chat_postMessage(
                channel=slack_channel, 
                attachments=self.__get_slack_json_msg(df)
            )
