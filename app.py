# Description: Prueba unitaria para el inicio de sesión en el sistema
# Documentacion oficial de Selenium con Python: https://selenium-python.readthedocs.io/index.html
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from db.config import Conexion
import traceback

class TestLogin():
    
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("URL")
        self.user = os.getenv("USUARIO")
        self.password = os.getenv("PASSWORD")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Iniciando prueba de inicio de sesión")
                
    def guardar_datos_prueba(self, estado, error):
        conexion = Conexion()
        try:
            conexion.insertar({"accion":"test_login",
                               "estado":estado,
                               "error":error, 
                               "fecha":time.strftime("%c"), 
                               "datos":{"url":self.url,"user":self.user,"password":self.password},
                               "seguimiento_pila":traceback.format_exc()})
        except Exception as e:
            print(e)
        finally:
            conexion.cerrar_conexion()
        

    def test_login(self):
        try:
            self.driver.get(self.url)
            username_field = self.driver.find_element(By.ID,"txtUserName")
            username_field.send_keys(self.user)
            password_field = self.driver.find_element(By.ID,"txtPassword")
            password_field.send_keys(self.password)
            self.driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()
            time.sleep(3)
            if self.driver.find_element(By.ID,"userLink").text == self.user:
                print("Inicio de sesión correcto")
                self.guardar_datos_prueba("correcto", "")
            else:
                print("Inicio de sesión incorrecto")
                self.guardar_datos_prueba("incorrecto", "Inicio de sesión incorrecto")
        except Exception as e:
            print(e)
            self.guardar_datos_prueba("incorrecto", str(e))
        finally:
            self.driver.close()
            print("Prueba finalizada")


if __name__ == "__main__":
    test = TestLogin()
    test.test_login()
