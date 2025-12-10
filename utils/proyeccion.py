from data.databases import *
from utils.gastos import*

def proyeccion_gasto(dias_futuros):
    # Validar que el número de días sea un entero positivo
    try:
        dias_futuros = int(dias_futuros)
        if dias_futuros <= 0:
            raise ValueError("El número de días debe ser positivo.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    # Filtrar los gastos de los últimos 30 días
    fecha_hoy = datetime.now()
    fecha_30_dias_antes = fecha_hoy - timedelta(days=30)

    gastos_ultimos_30_dias = [
        gasto for gasto in gastos
        if fecha_30_dias_antes <= datetime.strptime(gasto['fecha'], "%d-%m-%Y") <= fecha_hoy
    ]

    if len(gastos_ultimos_30_dias) == 0:
        print("No hay suficientes datos históricos para realizar la proyección.")
        return

    # Calcular el promedio diario de gasto total y por categoría
    total_gasto_30_dias = sum(gasto['cantidad'] for gasto in gastos_ultimos_30_dias)
    promedio_diario_total = total_gasto_30_dias / 30

    gasto_por_categoria = {}
    for gasto in gastos_ultimos_30_dias:
        categoria = gasto['categoria']
        if categoria not in gasto_por_categoria:
            gasto_por_categoria[categoria] = 0
        gasto_por_categoria[categoria] += gasto['cantidad']

    promedio_diario_categoria = {categoria: total / 30 for categoria, total in gasto_por_categoria.items()}

    # Proyección para los próximos N días
    proyeccion_total = promedio_diario_total * dias_futuros
    proyeccion_categoria = {categoria: promedio_diario * dias_futuros for categoria, promedio_diario in promedio_diario_categoria.items()}

    # Crear el reporte en formato JSON
    reporte_proyeccion = {
        "dias_proyectados": dias_futuros,
        "gasto_proyectado_total": proyeccion_total,
        "gasto_proyectado_por_categoria": proyeccion_categoria
    }

    # Guardar el reporte en un archivo JSON
    guardar_reporte_json("reporte_proyeccion.json", reporte_proyeccion)

    # Mostrar el resumen en consola
    print(f"Gasto proyectado total para los próximos {dias_futuros} días: ${proyeccion_total:.2f}")
    print("Gasto proyectado por categoría:")
    for categoria, monto in proyeccion_categoria.items():
        print(f"  {categoria}: ${monto:.2f}")
