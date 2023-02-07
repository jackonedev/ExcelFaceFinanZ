""" CREADORA DE TABLA
un algoritmo que te diga cuanto vas a estar 
pagando a futuro por una financiación dadas 
las constantes de la tabla de arriba 
a la izquierda

el calculo del interes se aplica una vez al año y se divide por 12 meses del año
las cuotas son fijas

hipoteca = ahorro + interes

variables para el calculo de la hipoteca:
  - valor hogar: precio_casa
  - desembolso: desembolso
  - gastos escribanía: notariado
  - plazo de pago: plazo_hipoteca
  - interes a pagar: interes

Pendiente: datetime
"""



""" GESTORA DE DINERO
Cuando el dinero INGRESA, se plantean condiciones y un orden.
Cuando se termina de cumplir con todas las condiciones, el total restante es AHORRO.

ingreso constante = ingreso

#TODO: un generador para agregar condiciones a futuro, itertools.count - str = 'gasto_{next(x)}' - lista.append(str)

gasto_1 = hip/alquiler Mensual: hip_alquiler
gasto_2 = Gasto Mantenimiento: mantenimiento
gasto_3 = Gasto Suministros: suministros
gasto_4 = Cash lifestyle: lifestyle
gasto_5 = Extra (#TODO): extra - (es un elemento vacío adicional de repuesto)

"""
from itertools import count



def ingreso_numerico(label):#TODO: Decorators

    x_while = count(1)
    x_while_limit = 5

    print '"{}" debe ser un numero'.format(label)
    ingreso = raw_input('declaro = ')
    ingreso = ingreso.replace('.','')
    while not ingreso.isdigit():
        chance = next(x_while)
        print 'Intento {} de {}'.format(chance, x_while_limit)
        ingreso = raw_input('Vuelva a ingresar "{}" = '.format(label))
        
        if chance == x_while_limit:
            print 'Intentos agotados\n'
            return
    print
    return ingreso
    
def cargar_variables():
    """
    En esta funcion creamos las variables de ingreso al sistema.
    Representan valores constantes en el tiempo.
    
    Las variables:
      - ingreso: Sueldo Mensual
      - hip_alquiler: Hip/Alquiler Mensual
      - mantenimiento: Gastos de Mantenimiento
      - suministros: Gastos de Suministros
      - lifestyle: Cash Lifestyle
      - extra: variable de repuesto
    """
    global ingreso, hip_alquiler, mantenimiento
    global suministros, lifestyle, extra
    ingreso = ingreso_numerico('Sueldo Mensual')
    if not ingreso:
        return
      
    hip_alquiler = ingreso_numerico('Hip/Alquiler Mensual')#TODO: esta variable requiere un calculo aparte
    mantenimiento = ingreso_numerico('Gastos de Mantenimiento')
    suministros = ingreso_numerico('Gasto Suministros')
    lifestyle = ingreso_numerico('Cash Lifestyle')
    extra = ''
    print
    return [ingreso, hip_alquiler, mantenimiento,\
             suministros, lifestyle, extra]


def ingreso_bool():#TODO: en desuso

    x_bool = count(1)
    x_bool_limit = 3  

    print '< 1: Si >    < 0: No >'    
    ingreso = raw_input('>> ')
    if not (ingreso == '1' or ingreso == '0'):
        print 'Intento {} de {}'.format(next(x_bool), x_bool_limit)
        ingreso = raw_input('>> ')

    if x_bool == x_bool_limit:
        print 'Intento agotados\n'
        return
    print
    return ingreso


def gestora_de_dinero():
    global alquila
    constantes = cargar_variables()
    
    if not constantes:
        print 'EJECUCION INTERRUMPIDA'
        return 

    print 'Las constantes son: '
    print constantes
    
    print 'Creamos ambos escenarios financieros: HIPOTECA Y ALQUILER'
#    print 'Alquilas?'
#    alquila = ingreso_bool()#TODO: Debe devolver ambos escenarios
#    print 'Alquila = {}'.format(bool(alquila))

    constantes_dicc = {
    'Sueldo_Mensual':'', 
    'Hip/Alquiler_Mensual':'',
    'Ahorros_Mensuales':'',
    'Gastos_Mantenimiento':'',
    'Gastos_Suministros':'',
    'pct_Cash_Req/Mes':'',
    'Cash_Lifestyle':''
    }

    paga_hipoteca = {}
    paga_alquiler = {}
    
    print constantes_dicc
    


    return True

def main():
    global ingreso, hip_alquiler, mantenimiento
    global suministros, lifestyle, extra
    global alquila
    

    print 'BIENVENIDO A LA GESTORA FINANCIERA!\n'
    print 'Provea los siguientes datos por favor:'
    
    if not gestora_de_dinero():#TODO: debe retornar algo
        print 'Saliendo del programa'
        return
      
    print 'Continua el programa'

if __name__ == '__main__':
    main()

    
    




