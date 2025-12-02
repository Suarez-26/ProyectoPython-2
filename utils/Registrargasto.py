from utils.menus import *
from data.databases import *
import datetime

def registrar_gasto():
    gastos = cargar_datos()

    cantidad = float(input("Ingrese el monto: "))
    categoria = input("Categoría (comida, transporte, etc): ").capitalize()
    descripcion = input("Descripción (opcional): ")
    fecha = (input(f"Ingrese la fecha del gasto del {categoria}"))

    nuevo_gasto = {
        "cantidad": cantidad,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": fecha,
    }

    gastos.append(nuevo_gasto)
    guardar_datos(gastos)

    print("\n✔ Gasto registrado con éxito.\n")

# -------------- lista de gastos -------------

def MostrarTodosGastos(gastos):
    print("\n=== TODOS LOS GASTOS ===")
    for g in gastos:
        print(f"{g['fecha']} - {g['descripcion']} ({g['categoria']})  ${g['monto']}")
    print()


def FiltrarPorCategoria(gastos, categoria):
    
    categoria = input("Ingrese la categoria a filtar :") 


    print(f"\n=== GASTOS EN CATEGORÍA: {categoria} ===")
    filtrados = [g for g in gastos if g["categoria"] == categoria]
    
    if not filtrados:
        print("No hay gastos en esa categoría.")
        return

    for g in filtrados:
        print(f"{g['fecha']} - {g['descripcion']}  ${g['monto']}")
    print()


def FiltrarPorRangofechas(gastos, FechaInicio, FechaFin):
    FechaInicio = input("Fecha inicio (YYYY-MM-DD): ")
    FechaFin = input("Fecha fin (YYYY-MM-DD): ")
    
    print(f"\n--- GASTOS ENTRE {FechaInicio} Y {FechaFin} ---")

    fi = datetime.datetime.strptime(FechaInicio, "%Y-%m-%d")
    ff = datetime.datetime.strptime(FechaFin, "%Y-%m-%d")

    filtrados = []
    for g in gastos:
        fecha_g = datetime.datetime.strptime(g["fecha"], "%Y-%m-%d")
        if fi <= fecha_g <= ff:
            filtrados.append(g)

    if not filtrados:
        print("No hay gastos en ese rango de fechas.")
        return

    for g in filtrados:
        print(f"{g['fecha']} - {g['descripcion']} ({g['categoria']})  ${g['monto']}")
    print()

# --------------------------------------------------
