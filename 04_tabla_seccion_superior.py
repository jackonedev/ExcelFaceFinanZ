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

from packpy.ingresar_datos import ingresar_numerico, ingresar_cifra, ingresar_agno

def main():
#    global ingreso, hip_alquiler, mantenimiento
#    global suministros, lifestyle, extra


    print( '\t======'*5)
    print( '\t  BIENVENIDO A LA GESTORA FINANCIERA!')
    print( '\t======'*5)
    print( 'Provea los siguientes datos por favor:')
    
#    if not gestora_de_dinero():
#        print( 'Saliendo del programa')
#        return

    print( 'Pasando gestora_de_dinero()\nContinua el programa')
    

    print( 'Definimos valor casa a 2.200.000')
    valor_casa = ingresar_numerico('valor_casa')
    calcular, desembolso = ingresar_cifra()
    if calcular:
        print( 'Desembolso: ', desembolso*valor_casa)

    calcular, notariado = ingresar_cifra()
    if calcular:
        print( 'Notariado: ', notariado*valor_casa)
    
    print( 'Definimos plazo de hipoteca a 30 años')
    plazo_hipoteca = ingresar_agno('plazo_hipoteca')
    if not plazo_hipoteca:
        print( 'Saliendo del programa')
        return

if __name__ == '__main__':
    main()

    
    




