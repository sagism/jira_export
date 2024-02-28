import csv
import datetime
import logging
from config_loader import load_config
from jira_connector import fetch_jira_items
from logger import setup_logging

def export_jira_issues(config_path):
    setup_logging()  # Initialize logging
    config = load_config(config_path)
    start_time = datetime.datetime.now()
    
    with open('jira_export.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write CSV header based on the first instance's field mapping for simplicity
        headers = ['Export Time'] + list(config['instances'][0]['field_mapping'].values())
        writer.writerow(headers)
        
        for instance in config['instances']:
            try:
                issues = fetch_jira_items(instance)
                for issue in issues:
                    # Map and write each issue to the CSV, prepending the script's start time
                    row = [start_time] + [issue[field] for field in instance['field_mapping'].keys()]
                    writer.writerow(row)
                logging.info(f"Exported {len(issues)} items from {instance['url']}")
            except Exception as e:
                logging.error(f"Failed to export from {instance['url']}: {e}")
    
    logging.info("Export completed.")

if __name__ == "__main__":
    export_jira_issues("config.json")

