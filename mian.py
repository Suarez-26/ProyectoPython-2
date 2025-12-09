# main.py
from utils.gastos import *
from utils.reportes import *

def main():
        while True:
            print("\n==== GESTIÓN DE GASTOS ====")
            print("1. Registrar Gasto")
            print("2. Listar Gastos")
            print("3. Generar Reporte")
            print("4. Salir")
            
            opcion = input("Selecciona una opción (1-4): ")
            
            if opcion == "1":
                registrar_gasto()
            elif opcion == "2":
                menu_listar_gastos()
            elif opcion == "3":
                generar_reporte()
            elif opcion == "4":
                print("¡Adiós!")
                break
            else:
                print("Opción no válida.")
            
if __name__ == "__main__":
    main()
