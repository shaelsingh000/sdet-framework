import yaml
import os

class ConfigReader:
    def __init__(self):
        env = os.getenv("ENV","dev")
        config_path = f"config/{env}.yaml"

        with open(config_path,"r") as file:
            self.config = yaml.safe_load(file)
    
    def get(self,key):
        return self.config(key)