import yaml

def load_config(path="/home/abhijeet_anand/Workspace/N2/config/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
