import json

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        # Add basic validation if necessary
        return config
    except FileNotFoundError:
        raise Exception(f"Configuration file {config_path} not found.")
    except json.JSONDecodeError:
        raise Exception(f"Configuration file {config_path} is not a valid JSON.")

