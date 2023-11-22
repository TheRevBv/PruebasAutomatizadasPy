# Description: Prueba unitaria para el inicio de sesión en el sistema
# Documentacion oficial de Selenium con Python: https://selenium-python.readthedocs.io/index.html
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

def test_login():
    # Cargar las variables de entorno
    load_dotenv()
    # Obtener el la url del navegador, usuario y contraseña de las variables de entorno
    
    url = os.getenv("URL")
    user = os.getenv("USUARIO")
    password = os.getenv("PASSWORD")
    # ruta_chromedriver = os.getenv("RUTA_CHROMEDRIVER") + "PruebasAutomatizadasPy\Browsers\chromedriver.exe"
    
    # Iniciar el navegador
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(ruta_chromedriver)
    driver.maximize_window()  

    # Ir a la página de inicio de sesión
    driver.get(url)

    # Buscar el campo de nombre de usuario
    username_field = driver.find_element(By.ID,"txtUserName")

    # Introducir el nombre de usuario
    username_field.send_keys(user)

    # Buscar el campo de contraseña
    password_field = driver.find_element(By.ID,"txtPassword")

    # Introducir la contraseña
    password_field.send_keys(password)

    # Hacer clic en el botón de inicio de sesión, tomando en cuenta el css selector button.btn.btn-primary
    driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()
    
    # Esperar 3 segundos a que cargue la página
    time.sleep(3)

    # Comprobar si el usuario ha iniciado sesión correctamente
    if driver.find_element(By.ID,"userLink").text == user:
        print("Inicio de sesión correcto")
    else:
        print("Inicio de sesión incorrecto")

    # Cerrar el navegador
    driver.close()


if __name__ == "__main__":
    test_login()
