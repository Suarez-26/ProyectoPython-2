# databases.py
# Examen
import json
import os

def guardar_datos(gastos):
    with open("gastos.json", "w") as archivo:
        json.dump(gastos, archivo, indent=4)

# Cargar  data en JSON 
def cargar_datos():
    if os.path.exists("gastos.json"):
        with open("gastos.json", "r") as archivo:
            return json.load(archivo)
    return []
# guardar reporte json 
def guardar_reporte_json(nombre_archivo, reporte):
    # Verificar si la carpeta 'reports' existe, y si no, crearla
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Guardar el reporte en el archivo JSON
    with open(nombre_archivo, "w") as archivo:
        json.dump(reporte, archivo, indent=4)
    print(f"Reporte guardado en {nombre_archivo}")

# guatardar reporte txt
def guardar_reporte_txt(nombre_archivo, gastos_filtrados, total, tipo_reporte):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"--- Reporte {tipo_reporte.capitalize()} ---\n")
        archivo.write(f"Total: ${total:.2f}\n")
        for gasto in gastos_filtrados:
            archivo.write(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, Descripción: {gasto['descripcion']}\n")
    print(f"Reporte guardado en {nombre_archivo}")
