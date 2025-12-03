# archivos/manejo_archivos.py

import json

# Archivo donde se guardan los gastos
archivo_gastos = "gastos.json"

# Lista global de gastos
gastos = []

# Funcion para cargar todos los datos 
def cargar_datos():
    """Carga los gastos desde el archivo JSON"""
    global gastos
    try:
        with open(archivo_gastos, 'r') as f:
            gastos = json.load(f)
        print(f"Datos cargados. {len(gastos)} gastos encontrados.")
    except FileNotFoundError:
        print("No se encontró el archivo de gastos. Empezando con una lista vacía.")
        gastos = []

# Funcion para guardar todos los datos 

def guardar_datos():
    """Guarda los gastos en el archivo JSON"""
    with open(archivo_gastos, 'w') as f:
        json.dump(gastos, f, indent=4)
    print("Datos guardados correctamente.")


# Funcion para guardar loa Reportes en JSON

def guardar_reporte_json(nombre_archivo, reporte):
    """Guarda el reporte en un archivo JSON"""
    with open(nombre_archivo, 'w') as f:
        json.dump(reporte, f, indent=4)
    print(f"Reporte guardado como {nombre_archivo}.")

# Funcion para guardar los Reportes en archivois TXT
def guardar_reporte_txt(nombre_archivo, gastos_filtrados, total, tipo_reporte):
    """Guarda el reporte en un archivo TXT"""
    with open(nombre_archivo, 'w') as f:
        f.write(f"--- Reporte {tipo_reporte.capitalize()} ---\n")
        f.write(f"Total de gastos: ${total:.2f}\n")
        f.write("-" * 60 + "\n")
        
        for gasto in gastos_filtrados:
            f.write(f"ID: {gasto['id']}, Fecha: {gasto['fecha']}, "
                    f"Categoría: {gasto['categoria']}, Monto: ${gasto['cantidad']:.2f}, "
                    f"Descripción: {gasto['descripcion']}\n")
            f.write("-" * 60 + "\n")
    print(f"Reporte guardado como {nombre_archivo}.")
