import utils.gastos as gastos
import data.databases as archivos

def mostrar_menu():
    print("------ BIENVENIDO AL GESTOR DE GASTOS ------")
    print("\n1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Generar reportes")
    print("4. Salir")

def main():
    archivos.cargar_datos()

    while True:
        mostrar_menu()

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            gastos.registrar_gasto()
        elif opcion == "2":
            gastos.Menu_Listar_gastos()
        elif opcion == "3":
            gastos.generar_reporte()
        elif opcion == "5":
            print("¡Gracias por usar el simulador!")
            archivos.guardar_datos()
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
