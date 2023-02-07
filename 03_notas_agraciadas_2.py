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

""" CREADORA DE TABLA
un algoritmo que te diga cuanto vas a estar 
pagando a futuro por una financiaci�n dadas 
las constantes de la tabla de arriba 
a la izquierda

el calculo del interes se aplica una vez al a�o y se divide por 12 meses del a�o
las cuotas son fijas

hipoteca = ahorro + interes

variables para el calculo de la hipoteca:
    - valor hogar: precio_casa
    - desembolso: desembolso
    - gastos escriban�a: notariado
    - plazo de pago: plazo_hipoteca
    - interes a pagar: interes

Pendiente: datetime
"""




def identificar_cifra():
    """
Se ingresa por pantalla una variable y retorna una tupla(bool, int or float)
Si return es (True, ) el segundo elemento es float
Si return es (False, ) el segundo elemento es int

bool sirve para identificar si el valor es determinado o requiere posterior procesamiento.

Si bool = True, requiere procesamiento
Si bool = False, valor determinado

disclaimer:    Los valores determinados se expresan siempre redondeados a enteros

    posibles variantes de entradas de test:
        primera condicion
        - 550000
        - 20
        segunda condicion:
        - 2.200.000
        - 550.000
        - 20.57
        - 0.2
        - 0.21
        tercera condicion:
        - 20%
        - 20.6%
        - 20.57%
        cuarta condicion:
        - 550.000,0
        - 0,2
        - 20,0%
    """

    global cifra
    cifra = raw_input('Declarar cifra = ')
    
    if cifra.replace(",","") == cifra:
        if cifra.isdigit():
            if int(cifra) > 100:#TODO: Decidir si el c�digo es a prueba de tontos (abs) y por l�gica - acepto cualquier valor?
                print '1- cifra expresada monetariamente'
                return False, int(cifra)
            elif 0 <= int(cifra) <= 100:
                print '1- cifra expresada porcentualmente'
                return True, float(cifra)/100
            else:
                print '1- primera condicion fallida'
                return False, None

        elif cifra.replace(".","").isdigit():
            if cifra.count('.') > 1:
                print '2- cifra expresada monetariamente'
                return False, int(cifra.replace(".",""))
            if int(float(cifra)) > 100:
                print '2- cifra expresada monetariamente'
                return False, int(cifra.replace(".",""))
            elif 0 < int(float(cifra)) <= 100:
                print '2- cifra expresada de forma porcentual'
                return True, float(cifra)/100
            elif int(float(cifra)) == 0:
                print '2- cifra expresada de forma porcentual'
                return True, float(cifra)
            else:
                print '2- segunda condicion fallida'
                return False, None
        
        elif cifra.replace(".","").replace("%","").isdigit():
            cifraux = cifra.replace(".","").replace("%","")
            if cifraux.count('.') == 0 and 0 <= int(cifraux) <= 100:
                #ERROR: 0.2% -> 0.02
                print '3- cifra expresada de forma porcentual sin decimales'
                return True, float(cifraux)/100
            elif len(cifraux) > 2:
                print '3- cifra expresada de forma porcentual con decimales'
                return True, float(cifra.replace('%',''))/100#TODO: toma como valor aceptable 101%
            else:#TODO: ESTOY ACA, PERO VOY A PROBAR '20.6' se me ocurre arreglar el exceso de decimales con un len al string y tomarlo para el round-loque importa es la posicion del punto 20.6, no es lo mismo que 2.06 
                print '3- tercera condicion fallida'
                return False, None
                
        else:
            print 'error etapa 1'

    elif cifra.count(',') > 0:
        if cifra.count(',') > 1:
            return 'No entiendo el numero'

        else:
            if cifra.replace(',','').isdigit(): 
                cifraux = cifra.replace(",",".")
                if int(float(cifraux)) > 0:
                    if int(float(cifraux)) > 1000: #TODO: de vuelta tener en cuenta si es para tontos, porque la logica que fuerza es margen intelectual que quito en otra variable - borra esta mierda
                        print '4- cifra expresada de forma monetaria'
                        return False, int(float(cifraux))
                    
                    elif 0 < int(float(cifraux)) < 100:
                        print '4- cifra expresada de forma porcentual entre 0 y 100'
                        return True, float(cifraux)/100

                elif int(float(cifraux)) == 0:
                    print '4- cifra expresada de forma porcentual'
                    return True, float(cifraux)
                else:
                    print '4- cuarta condicion fallida'
                    return False, None

            elif cifra.replace(',','').replace('.','').isdigit():
                cifraux = cifra.replace('.','').replace(',','.')
                if int(float(cifraux)) > 0:
                    print '5- cifra expresada de forma monetaria'
                    return False, int(float(cifraux))
                elif int(float(cifraux)) == 0:
                    print '5- cifra expresada de forma porcentual'
                    return True, float(cifraux)/100 #CHECK: input as: 2.100,6 no sense
                else:
                    print '5- quinta condicion fallida'
                    return False, None
                    
            elif cifra.replace(',','').replace('.','').replace('%','').isdigit():
                cifraux = cifra.replace('.','').replace(',','.').replace('%','')
                if int(float(cifraux)) > 0:
                    if int(float(cifraux)) > 100:
                        print '6- No tiene logica un numero tan grande con el valor %'
                    elif 0 < int(float(cifraux)) <= 100:
                        print '6- cifra expresada de forma porcentual entre 0 y 100'#CHECK: como un valor que diga % va a estar expresado de forma monetaria?
                        return True, float(cifraux)/100
                elif int(float(cifraux)) == 0:
                    print '6- cifra expreado de forma porcentual'
                    return True, float(cifraux)
                else:
                    print '6- sexta condicion fallida'
                    return False, None

            else:
                print 'error etapa 2'               


def main():
#    global ingreso, hip_alquiler, mantenimiento
#    global suministros, lifestyle, extra

    

    print 'BIENVENIDO A LA GESTORA FINANCIERA!\n'
    print 'Provea los siguientes datos por favor:'
    
#    if not gestora_de_dinero():
#        print 'Saliendo del programa'
#        return

    print 'Pasando gestora_de_dinero()\nContinua el programa'
    

    print 'Definimos valor casa a 2.200.000'
    valor_casa = 2200000
#    calcular, desembolso = identificar_cifra()
    print identificar_cifra()
    
if __name__ == '__main__':
    main()

    
    




