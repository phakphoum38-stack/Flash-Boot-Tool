import json

def save_config(config):
    with open("cloud_config.json", "w") as f:
        json.dump(config, f)

def load_config():
    with open("cloud_config.json", "r") as f:
        return json.load(f)
