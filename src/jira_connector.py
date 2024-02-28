from jira import JIRA
from field_mapper import apply_field_mapping, apply_value_mapping

def fetch_jira_items(instance_config):
    options = {'server': instance_config['url']}
    jira = JIRA(options, basic_auth=(instance_config['username'], instance_config['password']))
    issues = jira.search_issues(instance_config['query'])
    mapped_issues = []
    for issue in issues:
        mapped_issue = {}
        for field, mapped_field in instance_config['field_mapping'].items():
            value = issue.fields.__dict__.get(field, '')
            mapped_value = apply_value_mapping(instance_config, field, value)
            mapped_issue[mapped_field] = mapped_value
        mapped_issues.append(mapped_issue)
    return mapped_issues

