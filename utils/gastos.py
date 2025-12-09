# gastos.py
from data.databases import *
from utils.screen import *
from datetime import datetime, timedelta

# Lista global de gastos
gastos = []

def registrar_gasto():
    print("\nRegistrar un nuevo gasto:")

    # Pedir fecha, cantidad, categoría y descripción
    fecha = input("Fecha (DD-MM-AAAA): ")
    cantidad = float(input("Cantidad: $"))
    categoria = input("Categoría: ")
    descripcion = input("Descripción: ")

    # Crear un nuevo gasto
    nuevo_gasto = {
        "id": len(gastos) + 1,
        "fecha": fecha,
        "cantidad": cantidad,
        "categoria": categoria,
        "descripcion": descripcion
    }

    # Agregar el nuevo gasto a la lista
    gastos.append(nuevo_gasto)
    
    # Guardar los datos
    guardar_datos(gastos)
    print(f"Gasto registrado con ID {nuevo_gasto['id']}.")

def menu_listar_gastos():
    limpiar_consola()
    print("=="*25)
    print("\n ------ Listar los gastos ------")
    print("=="*25)
    print("1. Ver todos los gastos")
    print("2. Filtrar por fechas")
    print("3. Atras")
    print("=="*25)

    tipo_lista = input("Selecciona una opción (1-3): ")
    if tipo_lista == "1":
        ver_todos_los_gastos()
    elif tipo_lista == "2":
        filtrar_por_fecha()
    else:
        print("Opción inválida.")

def ver_todos_los_gastos():
        print("\nVer todos los gastos:")

        if len(gastos) == 0:
            print("No hay gastos registrados.")
            return

        print(f"Total de gastos: {len(gastos)}")
        for gasto in gastos:
            print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Cantidad: ${gasto['cantidad']}, Categoría: {gasto['categoria']}, Descripción: {gasto['descripcion']}")

def filtrar_por_fecha():
    # Filtra los gastos por un rango de fechas
    limpiar_consola()
    print("\n--- FILTRAR POR FECHA ---")
    fecha_inicio = input("Ingresa la fecha de inicio (DD-MM-AAAA): ")
    fecha_fin = input("Ingresa la fecha de fin (DD-MM-AAAA): ")

    gastos_filtrados = [
        gasto for gasto in gastos
        if fecha_inicio <= gasto['fecha'] <= fecha_fin
    ]

    if not gastos_filtrados:
        print("No hay gastos en ese rango de fechas.")
    else:
        print(f"Gastos entre {fecha_inicio} y {fecha_fin}:")
        for gasto in gastos_filtrados:
                print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Cantidad: ${gasto['cantidad']}, Categoría: {gasto['categoria']}, Descripción: {gasto['descripcion']}")