from pymongo import MongoClient
import os

# Cargar las variables de entorno
from dotenv import load_dotenv

class Conexion:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("MONGO_DATABASE")]
        self.collection = self.db[os.getenv("MONGO_COLLECTION")]

    def insertar(self, documento):
        self.collection.insert_one(documento)

    def obtener(self, filtro):
        return self.collection.find_one(filtro)

    def obtener_todos(self):
        return self.collection.find()

    def actualizar(self, filtro, documento):
        self.collection.update_one(filtro, documento)

    def eliminar(self, filtro):
        self.collection.delete_one(filtro)

    def eliminar_todos(self):
        self.collection.delete_many({})

    def cerrar_conexion(self):
        self.client.close()