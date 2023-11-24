from pruebas.test_login import TestLogin
import schedule
import time

class Main():
    
    def __init__(self):
        print("Iniciando pruebas")
        self.contador_pruebas = 0
        schedule.every(1).minutes.do(self.iniciar_pruebas)
        self.run_scheduler()

    def iniciar_pruebas(self):
        self.contador_pruebas += 1
        print(f"\nPrueba #{self.contador_pruebas}")
        print("Iniciando pruebas")
        TestLogin().test_login()
        print("Pruebas finalizadas")

    def run_scheduler(self):
        try:
            while True:
                schedule.run_pending()
                time.sleep(0.5)  # Reducción del tiempo de espera del bucle
        except KeyboardInterrupt:
            print("\nDeteniendo la ejecución del script.")

if __name__ == "__main__":
    Main()
