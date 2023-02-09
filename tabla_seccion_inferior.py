""""
PRIMERA ACLARACION. EL USUARIO DEBE INGRESAR SOLO NUMEROS POSITIVOS. 
CORREGIR ESTO SINGIFICA IR EN CONTRA DE LA FILOSOFIA DEL SOFWTWARE. 

EL SOFTWARE DEBE SER AGIL. 
AL USUARIO NO LE DEBE IMPORTAR EL SIGNO QUE TIENE EL VALOR QUE INGRESA.

NO SE HA IMPLEMENTADO LA FUNCION abs()
PARA QUE APRENDA

...
pip install openpyxl


from openpyxl import Workbook

wb = Workbook()
"""
from itertools import count
from packpy.ingresar_datos import ingresar_numerico

def cargar_variables():
    """
    En esta funcion creamos las variables de ingreso al sistema.
    Representan valores constantes en el tiempo.
    
    Las variables:
        - ingreso: Sueldo Mensual
        - alquiler: Hip/Alquiler Mensual
        - mantenimiento: Gastos de Mantenimiento
        - suministros: Gastos de Suministros
        - lifestyle: Cash Lifestyle
        - extra: variable de repuesto
    """
    global ingreso, hipoteca, alquiler, mantenimiento
    global suministros, lifestyle, extra

    ingreso = ingresar_numerico('Ingreso Mensual')
    if not ingreso:
        return

    alquiler = ingresar_numerico('Alquiler Mensual ')#TODO: esta variable requiere un calculo aparte
    if not alquiler:
        return

    mantenimiento = ingresar_numerico('Mantenimiento Mensual')
    if not mantenimiento:
        return

    suministros = ingresar_numerico('Suministros Mensuales')
    if not suministros:
        return

    lifestyle = ingresar_numerico('Cash Lifestyle')
    if not lifestyle:
        return

    extra = ''
    print()
    return [ingreso, alquiler, mantenimiento,\
            suministros, lifestyle, extra]


def gestora_de_dinero():
    global paga_hipoteca, paga_alquiler
    constantes = cargar_variables()
    
    if not constantes:
        print( 'EJECUCION INTERRUMPIDA')
        return 

    print( 'Creamos ambos escenarios financieros: HIPOTECA Y ALQUILER')

    constantes_dicc = {
    'Sueldo_Mensual': constantes[0],
    'Hip/Alquiler_Mensual': -constantes[1],
    'Ahorros_Mensuales': '',
    'Gastos_Mantenimiento': constantes[2],
    'Gastos_Suministros': -constantes[3],
    'pct_Cash_Req/Mes': '',
    'Cash_Lifestyle': -constantes[4]
    }

    paga_hipoteca = {}
    paga_alquiler = {}

    paga_hipoteca.update(constantes_dicc)
    paga_hipoteca['Gastos_Mantenimiento'] *= -1
    paga_alquiler.update(constantes_dicc)
    
    ahorro_hipoteca = sum([x for x in paga_hipoteca.values() if isinstance(x, int)])
    ahorro_alquiler = sum([x for x in paga_alquiler.values() if isinstance(x, int)])

    pct_reqmes_hipoteca = (paga_hipoteca['Sueldo_Mensual'] - ahorro_hipoteca) / paga_hipoteca['Sueldo_Mensual']  
    pct_reqmes_alquiler = (paga_alquiler['Sueldo_Mensual'] - ahorro_alquiler) / paga_alquiler['Sueldo_Mensual']

    paga_hipoteca['Ahorros_Mensuales'] = ahorro_hipoteca
    paga_hipoteca['pct_Cash_Req/Mes'] = pct_reqmes_hipoteca
    paga_alquiler['Ahorros_Mensuales'] = ahorro_alquiler
    paga_alquiler['pct_Cash_Req/Mes'] = pct_reqmes_alquiler

    return True

def main():
    global ingreso, alquiler, mantenimiento
    global suministros, lifestyle, extra
    global paga_hipoteca, paga_alquiler
    

    contador_principal = count(1)#TODO: no tiene sentido creo


    print( '\t======'*5)
    print( '\t  BIENVENIDO A LA GESTORA FINANCIERA!')
    print( '\t======'*5)
    print( '\n>> {})  Provea los siguientes datos por favor:'.format(next(contador_principal)))
    
    if not gestora_de_dinero():#TODO: debe retornar algo
        print( 'Error en gestora_de_dinero()\nSaliendo del programa')
        return
    
    print()
    # print( '>> {})  El escenario de PAGA HIPOTECA es: '.format(next(contador_principal)))
    # for llave, valor in paga_hipoteca.items():
    #     print( '{}: {}'.format(llave, valor))
    # print()
    # print( '>> {})  El escenario de PAGA ALQUILER es: '.format(next(contador_principal)))
    # for llave, valor in paga_alquiler.items():
    #     print( '{}: {}'.format(llave, valor))


    print( '\nTerminando el programa')

    return paga_alquiler, paga_hipoteca

if __name__ == '__main__':
    main()

    
    




