""" CREADORA DE TABLA PARTE SUPERIOR
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
    - gastos escribanía: notariado
    - plazo de pago: plazo_hipoteca
    - interes a pagar: interes

Pendiente: datetime
"""
from packpy.ingresar_datos_2_7 import ingresar_numerico, ingresar_cifra, ingresar_agno

def elegir_simbolo_moneda(Europa=True):
    if Europa:
        America = False
        mon_sym = '�'
    elif not Europa:
        America = True
        mon_sym = '$'
    print 'Simbolo: {}'.format(mon_sym)
    return mon_sym


def main():
#    global ingreso, hip_alquiler, mantenimiento
#    global suministros, lifestyle, extra

    global mon_sym

    print '\t======'*5
    print '\t  BIENVENIDO A LA GESTORA FINANCIERA!'
    print '\t======'*5
    print
    
    print '\nDeterminando formato moneda por default:'
    mon_sym = elegir_simbolo_moneda()


    print '\nPROVEA los siguientes datos por favor:'
    


#    if not gestora_de_dinero():
#        print 'Saliendo del programa'
#        return



    almacenar_datos = {}#Dicto()


    print 'Pasando gestora_de_dinero()\nIngresando al programa'
    print
    print 'Definimos VALOR CASA a 2.200.000'
    valor_casa = ingresar_numerico('valor_casa')

    almacenar_datos.ingresar('valor_casa', valor_casa)
    almacenar_datos.prefijo(mon_sym).sufijo('%')
    print almacenar_datos

    print 'Confirmo que usted ha ingresado €{}'.format(valor_casa)
    if not valor_casa:
        print 'error'
        return
    print

    print 'Definamos un VALOR DE DESEMBOLSO'
    # ERRORES
    # 25.000 > 25%
    _calcular, desembolso = ingresar_cifra('Desembolso')
    if _calcular:
        print 'El porcentaje de desembolso: {}%'.format(desembolso*100)
        print 'Desembolso: ', desembolso*valor_casa
    else:
        print 'El porcentaje de desembolso: {}%'.format(desembolso/valor_casa*100)
        print 'Desembolso: ', desembolso
    print
    
    print 'Definimos la cifra ESCRIBANIA'
    _calcular, notariado = ingresar_cifra('Notariado')
    if _calcular:
        print 'El porcentaje de Notariado: {}%'.format(notariado*100)

        print 'Notariado: ', notariado*valor_casa
    else:
        print 'El porcentaje de Notariado: {}%'.format(notariado/valor_casa*100)
        print 'Notariado: ', notariado
    
    print 'Definimos PLAZO de hipoteca a 30 agnos'
    plazo_hipoteca = ingresar_agno('plazo_hipoteca')
    if not plazo_hipoteca:
        print 'Saliendo del programa'
        return


    print '\nContinuar con el programa...\n'
    
    print 'Antes de salir fijate las variables que tenes!!!!!'
    
    print 'TODO: CIFRA INTERES'
    print 
    

if __name__ == '__main__':
    main()

    
    




