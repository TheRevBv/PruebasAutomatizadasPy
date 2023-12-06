from pruebas.test_login import TestLogin
import schedule
import time
import argparse
from utils.common import Common

class Main():
    
    def __init__(self, intervalo, nombre_prueba):
        self.contador_pruebas = 0
        schedule.every(intervalo).minutes.do(self.iniciar_pruebas, nombre_prueba)
        self.run_scheduler()
        
    def iniciar_pruebas(self, nombre_prueba):
        self.contador_pruebas += 1
        print(f"\nPrueba #{self.contador_pruebas}")
        print("Iniciando pruebas")
        if nombre_prueba == 'login':
            TestLogin().test_login()
        else:
            print("\nNo se ha encontrado el test que quieres ejecutar")     
        print("Pruebas finalizadas")
        
    def run_scheduler(self):
        try:
            while True:
                schedule.run_pending()
                time.sleep(0.5) #Reducción del tiempo de espera del bucle
        except KeyboardInterrupt:
            print("\nDeteniendo la ejecución del script.")
            exit()
                    

if __name__ == "__main__":
    common = Common()
    args = argparse.ArgumentParser()
    tests_choices = list(common.config()['pruebas'].keys())
    args.add_argument('prueba', help='El test que quieres ejecutar', type=str, choices=tests_choices)
    
    args = args.parse_args()    
    test = args.prueba
    if test == '':
        print("No se ha introducido ningún test")
        exit()
    intervalo = common.config()['pruebas'][test]['intervalo']
    print(f"El test {test} se ejecutará cada {intervalo} minutos")
    Main(intervalo, test)
    