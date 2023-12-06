import yaml

class Common():
    def __init__(self):
        with open('config.yaml', mode='r') as f:
            self._config = yaml.full_load(f)
    
    def config(self):
        return self._config