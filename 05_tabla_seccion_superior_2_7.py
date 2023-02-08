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

# IMPORTAMOS LIBRERIAS

"œ"
from packpy.elegir_formato_2_7 import elegir_moneda_sistema# -> http://www.python.org/peps/pep-0263.html
from packpy.ingresar_datos_2_7 import ingresar_numerico, ingresar_cifra, ingresar_agno, ingresar_tasa
from packpy.almacenar_datos import Dicto



def main():
#    global ingreso, hip_alquiler, mantenimiento
#    global suministros, lifestyle, extra
    global mon_sym
    global valor_casa, desembolso, notariado, plazo_agno, tasa_interes    


    print '\t======'*5
    print '\t  BIENVENIDO A LA GESTORA FINANCIERA!'
    print '\t======'*5
    print
    print '\n>>  Determinando formato moneda por default:'
    mon_sym = elegir_moneda_sistema(Europa=True)
    if mon_sym == 'euro':
        mon_sym = '�'
    print 'Simbolo: {}'.format(mon_sym)
    print '\n>>  PROVEA los siguientes datos por favor:'
#    if not gestora_de_dinero():
#        print 'Saliendo del programa'
#        return
    print 'Pasando gestora_de_dinero()\nIngresando al programa'
    print
    



    """Por favor, a continuacion no utilice el caracter "-"  """
    almacenar_datos = Dicto(name='hip_alquiler')




    print '>>  Definimos VALOR CASA a 2.200.000'
    valor_casa = ingresar_numerico('valor_casa')
    if not valor_casa:
        print 'error'
        return
    almacenar_datos.ingresar('valor_casa', valor_casa)
    almacenar_datos.prefijo(mon_sym)
    print 'Confirmando valor -> ', almacenar_datos

    print

    print '>>  Definamos un VALOR DE DESEMBOLSO'
    # ERRORES#TODO
    # 25.000 -> 25%
    _calcular, desembolso = ingresar_cifra('Desembolso')

    if not desembolso:
        print 'error'
        return
    if _calcular:
        porcentaje = desembolso *100
        valor = int(desembolso*valor_casa)
    else:
        porcentaje = float(desembolso)/float(valor_casa)*100
        valor = int(desembolso)
    
    almacenar_datos.ingresar('desembolso', valor)
    almacenar_datos.prefijo(mon_sym)
    print 'Desembolso -> {}'.format(almacenar_datos)
    almacenar_datos.ingresar('desembolso_porcentaje', porcentaje)
    almacenar_datos.sufijo('%')
    print 'El porcentaje de desembolso -> {}'.format(almacenar_datos)
    
    print   

    print '>>  Definimos la cifra ESCRIBANIA'
    campo = 'Notariado'
    _calcular, notariado = ingresar_cifra(campo)
    if not notariado:
        print 'error'
        return
    if _calcular:
        porcentaje = notariado *100
        valor = int(notariado*valor_casa)
    else:
        porcentaje = float(notariado)/float(valor_casa)*100
        valor = int(notariado)
    ##DRY
    almacenar_datos.ingresar(campo.lower().replace(' ','_'), valor)
    almacenar_datos.prefijo(mon_sym)
    print 'Valor {} -> {}'.format(campo, almacenar_datos)
    almacenar_datos.ingresar(campo.lower().replace(' ','_')+'_pct', porcentaje)
    almacenar_datos.sufijo('%')
    print 'Porcenaje {} -> {}'.format(campo, almacenar_datos)
    
    print

    print '>>  Definimos PLAZO de hipoteca a 30 agnos'
    campo = 'Plazo Agnos'
    plazo_agno = ingresar_agno('plazo_hipoteca')
    if not plazo_agno:
        print 'Saliendo del programa'
        return
    almacenar_datos.ingresar(campo.lower().replace(' ','_'), plazo_agno)
    almacenar_datos.sufijo('Agnos')### TODO
    print 'Valor {} -> {}'.format(campo, almacenar_datos)

    print

    print '>>  Definamos TASA DE INTERES'
    campo = 'Tasa Interes'
    tasa_interes = ingresar_tasa()
    if not tasa_interes:
        print 'error en main'
        return
    almacenar_datos.ingresar(campo.lower().replace(' ','_'), plazo_agnos)
    almacenar_datos.prefijo(mon_sym)
    print 'Valor {} -> {}'.format(campo, almacenar_datos)      


    print '\nContinuar con el programa...\n'    
    print 'Antes de salir fijate las variables que tenes!!!!!'
    print 'TODO: CIFRA INTERES'
    print dir()
    

if __name__ == '__main__':
    main()