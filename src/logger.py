import logging

def setup_logging():
    logging.basicConfig(filename='jira_export.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


