# reportes.py
from datetime import datetime, timedelta
from data.databases import *
from utils.gastos import *
from utils.screen import *

def generar_reporte():
    limpiar_consola()
    print("=="*25)
    print("\n--- GENERAR REPORTE ---")
    print("=="*25)
    print("Selecciona el tipo de reporte:")
    print("1. Diario")
    print("2. Semanal")
    print("3. Mensual")
    print("=="*25)

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
    semana_inicio = input("Ingrese la fecha de inicio de la semana (DD-MM-AAAA): ")
    semana_inicio = datetime.strptime(semana_inicio, "%d-%m-%Y")
    semana_fin = semana_inicio + timedelta(days=6)

    gastos_semana = [gasto for gasto in gastos if semana_inicio <= datetime.strptime(gasto['fecha'], "%d-%m-%Y") <= semana_fin]

    if not gastos_semana:
        print(f"No hay gastos registrados para la semana del {semana_inicio} al {semana_fin}.")
        return

    total_semana = sum(g['cantidad'] for g in gastos_semana)
    print(f"\n--- Reporte Semanal ---")
    print(f"Semana: {semana_inicio.strftime('%d-%m-%Y')} al {semana_fin.strftime('%d-%m-%Y')}")
    print(f"Total de gastos: ${total_semana:.2f}")
    
    for gasto in gastos_semana:
        print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")
    
    guardar_o_mostrar_reporte("semanal", gastos_semana, total_semana)

def generar_reporte_mensual():
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
    opcion = input("¿Quieres guardar este reporte como archivo JSON o TXT? (json/txt): ")
    
    if opcion == "json":
        nombre_archivo = f"reporte_{tipo_reporte}.json"
        reporte = {
            "tipo_reporte": tipo_reporte,
            "total": total,
            "gastos": gastos_filtrados
        }
        guardar_reporte_json(nombre_archivo, reporte)
    elif opcion == "txt":
        nombre_archivo = f"reporte_{tipo_reporte}.txt"
        guardar_reporte_txt(nombre_archivo, gastos_filtrados, total, tipo_reporte)
    else:
        print("Opción inválida. Mostrando reporte en pantalla.")
        mostrar_reporte_en_pantalla(gastos_filtrados, total, tipo_reporte)

def mostrar_reporte_en_pantalla(gastos_filtrados, total, tipo_reporte):
    print(f"\n--- Reporte {tipo_reporte.capitalize()} ---")
    print(f"Total: ${total:.2f}")
    for gasto in gastos_filtrados:
        print(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}")
