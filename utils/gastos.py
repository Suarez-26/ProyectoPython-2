# gastos/gastos.py

import data.databases as archivos
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
    archivos.guardar_datos()
    print(f"Gasto registrado con ID {nuevo_gasto['id']}.")


# Funcion para ver todos los gastos registrados
def Menu_Listar_gastos():
    print("\n ------Listar los gastos ------")
    print("1. Ver todos los gatos")
    print("2. Filtar por fechas ")
    print("3. Atras")

    tipo_ista = input("Selecciona una opción (1-3): ")
    if tipo_ista == "1":
        ver_todos_los_gastos()
    elif tipo_ista == "2":
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
    """Filtra los gastos por un rango de fechas"""
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


def generar_reporte():
    print("\n--- GENERAR REPORTE ---")
    print("Selecciona el tipo de reporte:")
    print("1. Diario")
    print("2. Semanal")
    print("3. Mensual")

    tipo_reporte = input("Selecciona una opción (1-3): ")

    if tipo_reporte == "1":
        generar_reporte_diario()
    elif tipo_reporte == "2":
        generar_reporte_semanal()
    elif tipo_reporte == "3":
        generar_reporte_mensual()
    else:
        print("Opción inválida.")

def generar_reporte_diario():
    """Genera el reporte diario"""
    fecha = input("Ingrese la fecha para el reporte (DD-MM-AAAA): ")
    gastos_dia = [gasto for gasto in gastos if gasto['fecha'] == fecha]
    
    if not gastos_dia:
        print(f"No hay gastos registrados para el día {fecha}.")
        return

    total_dia = sum(g['cantidad'] for g in gastos_dia)
    print(f"\n--- Reporte Diario ---")
    print(f"Fecha: {fecha}")
    print(f"Total de gastos: ${total_dia:.2f}")


    for gasto in gastos_dia:
        print(f"ID: {gasto['id']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")
    
    guardar_o_mostrar_reporte("diario", gastos_dia, total_dia)

def generar_reporte_semanal():
    """Genera el reporte semanal"""
    semana_inicio = input("Ingrese la fecha de inicio de la semana (DD-MM-AAAA): ")
    semana_inicio = datetime(semana_inicio)
    semana_fin = semana_inicio + timedelta(days=6)

    gastos_semana = [gasto for gasto in gastos if semana_inicio <= datetime(gasto['fecha']) <= semana_fin]

    if not gastos_semana:
        print(f"No hay gastos registrados para la semana del {semana_inicio} al {semana_fin}.")
        return

    total_semana = sum(g['cantidad'] for g in gastos_semana)
    print(f"\n--- Reporte Semanal ---")
    print(f"Semana: {semana_inicio} al {semana_fin}")
    print(f"Total de gastos: ${total_semana:.2f}")
    
    for gasto in gastos_semana:
        print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")
    
    guardar_o_mostrar_reporte("semanal", gastos_semana, total_semana)

def generar_reporte_mensual():
    """Genera el reporte mensual"""
    mes = input("Ingrese el mes y año (MM-AAAA) para el reporte: ")
    
    gastos_mes = [gasto for gasto in gastos if gasto['fecha'][3:7] == mes]

    if not gastos_mes:
        print(f"No hay gastos registrados para el mes {mes}.")
        return

    total_mes = sum(g['cantidad'] for g in gastos_mes)
    print(f"\n--- Reporte Mensual ---")
    print(f"Mes: {mes}")
    print(f"Total de gastos: ${total_mes:.2f}")
    
    for gasto in gastos_mes:
        print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")
    
    guardar_o_mostrar_reporte("mensual", gastos_mes, total_mes)

def guardar_o_mostrar_reporte(tipo_reporte, gastos_filtrados, total):
    # Función que guarda o muestra el reporte dependiendo de la opción del usuario
    opcion = input("¿Quieres guardar este reporte como archivo JSON o TXT? (json/txt): ")
    
    if opcion == "json":
        nombre_archivo = f"reporte_{tipo_reporte}.json"
        reporte = {
            "tipo_reporte": tipo_reporte,
            "total": total,
            "gastos": gastos_filtrados
        }
        archivos.guardar_reporte_json(nombre_archivo, reporte)
    elif opcion == "txt":
        nombre_archivo = f"reporte_{tipo_reporte}.txt"
        archivos.guardar_reporte_txt(nombre_archivo, gastos_filtrados, total, tipo_reporte)
    else:
        print("Opción inválida. Mostrando reporte en pantalla.")
        mostrar_reporte_en_pantalla(gastos_filtrados, total, tipo_reporte)

def mostrar_reporte_en_pantalla(gastos_filtrados, total, tipo_reporte):
    # Muestra el reporte en pantalla
    print(f"\n--- Reporte {tipo_reporte.capitalize()} ---")
    print(f"Total: ${total:.2f}")
    for gasto in gastos_filtrados:
        print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")

