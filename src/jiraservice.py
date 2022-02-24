from jira import JIRA
import config

class JiraService():
    """
    class responsible for creating and deleting issues on Jira.
    """
    
    def __init__(self):
        self.client = JIRA(
            options={'server': config.JIRA_SERVER}, 
            basic_auth=(config.JIRA_USERNAME, config.JIRA_TOKEN)
        )

    def create_ticket(self, summary, description, issue_type):
        self.client.create_issue(fields={
            'project': {'key': config.JIRA_PROJECT_KEY},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        })

    def delete_tickets(self, summary):
        issues = self.client.search_issues(
            'project="%s" AND summary~"%s"' % (config.JIRA_PROJECT_KEY, summary), 
            maxResults=1000
        )

        for issue in issues:
            issue.delete()
