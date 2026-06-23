import os
import json

class ConfigReader:
    _config = None
    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config =json.load(config_file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']

    @staticmethod
    def get_api_base_url():
        # Return api_base_url if present, otherwise fallback to base_url
        cfg = ConfigReader.load_config()
        return cfg.get('api_base_url') 
    
    @staticmethod
    def get_username():
        return ConfigReader.load_config()['credentials']['username']

    @staticmethod
    def get_password():
        return ConfigReader.load_config()['credentials']['password']
    
    @staticmethod
    def get_timeout():
        return ConfigReader.load_config()['timeout']['implicit']