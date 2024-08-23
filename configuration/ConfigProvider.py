import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini')

class ConfigProvider:
    def __init__(self):
        self.config = global_config

    def get(self, section:str, prop: str) -> str:
        return self.config[section].get(prop)

    def get_ui_url(self) -> str:
        return self.config["ui"].get("base_url")
    
    def get_ui_timeout(self) -> int:
        return self.config["ui"].get("timeout")

    def get_api_url(self) -> str:
        return self.config["api"].get("base_url")
    
    def get_api_token(self) -> str:
        return self.config["api"].get("token")