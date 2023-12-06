# Creando una clase para el manejo de logs
# Autor: Joshua Morin

import logging
import os
import sys
from datetime import datetime

class Loggs():
    
    def __init__(self, path):
        self.path = path
        self.name = 'logs.log'
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def loggs(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        file_handler = logging.FileHandler(self.path + self.name)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.formatter)
        self.log.addHandler(file_handler)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(self.formatter)
        self.log.addHandler(stream_handler)
        return self.log
    