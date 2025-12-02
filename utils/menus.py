from utils.Registrargasto import *
from data.databases import *
from mian import *

def Menu_Principal():
    while True:
        print("""=============================================
             Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================""")
        
        opt = input("--> INGRESE UNA OPCIÓN : ")

        if opt == "1":
            Menu_RegistrarGasto()
        elif opt == "2":
            Menu_ListarGastos()
        elif opt == "3":
            Menu_CalcularTotalGastos()
        elif opt == "4":
            Menu_GenerarReporteGastos()
        elif opt == "5":
            print("¡Hasta pronto!")
            break
        else:
            print(" OPCIÓN NO VÁLIDA, INTENTE NUEVAMENTE\n")

#-----------------------------------------------------------------------------------

def Menu_RegistrarGasto():
    print("""=============================================
            Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:

- Monto del gasto:
- Categoría (ej. comida, transporte, entretenimiento, otros):
- Descripción (opcional):

Ingrese 'S' para insertar o 'C' para cancelar.
=============================================""") 

    opt = input("--> INGRESE UNA OPCIÓN (S/C): ")

    if opt == 's':
        registrar_gasto()
    elif opt == 'c':
        print(">> Volviendo al menú principal...\n")
    else:
        print(" Opción inválida. Regresando al menú principal...\n")

# --------------------------------------------------------------------------------------------

def Menu_ListarGastos():
    while True:
        print("""=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================""")
        
        opt = input("--> INGRESE UNA OPCIÓN : ")

        if opt == "1":
            MostrarTodosGastos(gastos)
        elif opt == "2":
            FiltrarPorCategoria(gastos, categoria)
        elif opt == "3":
            FiltrarPorRangofechas(gastos, fecha_inicio, fecha_fin)
        elif opt == "4":
            print(">> Regresando al menú principal...\n")
            break
        else:
            print(" LA OPCION NO ES VALIDA\n")

    
# ------------------------------------------------------------------------------------------------

def Menu_CalcularTotalGastos():
    print("""=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================""")
    opt = (input("--> INGRESE UNA OPCION :"))
    
    if opt == 1:
        pass
    else:
        pass
    
    
#---------------------------------------------------------------------------------------------------

def Menu_GenerarReporteGastos():
    print("""=============================================
           Generar Reporte de Gastos
=============================================
Seleccione el tipo de reporte:

1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar al menú principal
=============================================""")
    
Menu_Principal()




