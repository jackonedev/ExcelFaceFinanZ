from tabla_seccion_superior import main
from packpy.elegir_formato import elegir_moneda_sistema
import time

def buscar_valor(valor, dicc):#TODO: meter dentro de packpy
    for llave in dicc:#TODO: almacenamiento datos es una variable global
        if llave.count(valor) == 1:
            valor = dicc[llave]
            return valor

def calcular_cuota(dicc):
    valor_casa = buscar_valor('valor_casa', dicc)
    desembolsos = buscar_valor('desembolso', dicc)
    monto_financiado = valor_casa - desembolsos
    interes_mensual = buscar_valor('tasa_interes', dicc) / 12 / 100
    cantidad_cuotas = buscar_valor('plazo_año', dicc) * 12

    return (monto_financiado * interes_mensual)/(1-(1+interes_mensual)**(cantidad_cuotas*(-1)))

def tabla_cuotas(dicc, imprimir=False):
    saldo = buscar_valor('valor_casa', dicc) - buscar_valor('desembolso', dicc)
    cantidad_cuotas = buscar_valor('plazo_año', dicc) * 12
    interes_mensual = buscar_valor('tasa_interes', dicc) / 12 / 100
    cuota = calcular_cuota(dicc)
    lista_banco, lista_ahorro, lista_saldo = [], [], []
    for i in range(1, cantidad_cuotas+1):
            pago_interes = saldo * interes_mensual
            amortizacion = cuota - pago_interes
            saldo -= amortizacion
            if imprimir:
                if i < 10:
                    i = '0'+str(i)
                print (f'>>  cuota: {i} | pago_interes: {round(pago_interes, 1)} | amortizacion: {round(amortizacion, 1)} | nuevo_saldo: {round(saldo, 1)}')
            lista_banco.append(int(pago_interes))
            lista_ahorro.append(int(amortizacion))
            lista_saldo.append(int(saldo))
    return {'pago_interes': lista_banco, 'amortizacion': lista_ahorro, 'saldo': lista_saldo}

def imprimir_variables(dicc):
    for llave in dicc:
        label = llave.split('-')[1]
        if isinstance(dicc[llave], list):
            print (f'{label}: list')
        else:
            print (f'{label}: {dicc[llave]}')


def main2():
    mon_sym = elegir_moneda_sistema()

    print ('\nARRANCANDO PARTE 1 DE LA DEMO:')
    almacenamiento_datos = main()
    print ('\nCHECKEO DEL VALOR DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicto)
    print ('\nCHECKEO DEL FORMATO DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicture)
    input ('Presione enter para continuar...')
    print ('\nCALCULO DE LA CUOTA FIJA')
    cuota = calcular_cuota(almacenamiento_datos.dicto)
    almacenamiento_datos.ingresar('cuota', int(cuota))
    almacenamiento_datos.prefijo(mon_sym)
    print (almacenamiento_datos)
    print ('\nCALCULO Y DESCARGA DE TABLA DE CUOTAS FUTURAS')
    dicc = tabla_cuotas(almacenamiento_datos.dicto, imprimir=False)
    for llave in dicc:
        almacenamiento_datos.ingresar(llave, dicc[llave])
        almacenamiento_datos.lista(prefix=mon_sym)

    print ('\nFINALIZANDO PARTE 1 DE LA DEMO:')
    time.sleep(0.4)
    time.sleep(0.4)
    print ('\nCHECKEO DEL VALOR DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicto)
    time.sleep(0.4)
    time.sleep(0.4)
    print ('\nCHECKEO DEL FORMATO DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicture)
    time.sleep(0.4)
    time.sleep(0.4)
    print ('\nEXPORTANDO EN CSV LA TABLA DE CUOTAS FUTURAS: (no implementado)')
    #TODO: llevar a pandas.DataFrame y exportar a csv
    #TODO: si los values son list, y las list tienen mismo len, devolver DataFrame
    print ('\nARRANCANDO PARTE 2 DE LA DEMO:')


    ## IMPORTANTE AL LECTOR:
    """Esta parte fue el comienzo del desarrollo de TODO el código, y hay mucho que se va a implementar a continuación que debe ser removida he implementado dentro de los modulos importados"""
    from tabla_seccion_inferior import main
    estructura_alquiler, estructura_compra = main()#TODO: aplicar almacenar datos
    # EJEMPLO: Ahora tengo que actualizar los valor de las estructuras_i, y volver a calcular el ahorro y el pct_Cash_Req/Mes
    # EJEMPLO: Le tengo que agregar "capital_inicial" = desembolso + notariado

    estructura_alquiler['capital_inicial'] = buscar_valor('desembolso', almacenamiento_datos) + buscar_valor('notariado', almacenamiento_datos)
    estructura_compra['capital_inicial'] = estructura_alquiler['capital_inicial']

    label_notariado = buscar_valor('notariado_pct', almacenamiento_datos)
    label_desembolso = buscar_valor('desembolso_pct', almacenamiento_datos)

    estructura_compra[f'notariado {label_notariado} %'] = - buscar_valor('notariado', almacenamiento_datos)
    estructura_compra[f'desembolso {label_desembolso} %'] = - buscar_valor('desembolso', almacenamiento_datos)
    estructura_alquiler[f'notariado {label_notariado} %'] = 0
    estructura_alquiler[f'desembolso {label_desembolso} %'] = 0
    
    estructura_compra['Hip/Alquiler_Mensual'] = - cuota
    estructura_compra['Ahorros_Mensuales'] += estructura_alquiler['Hip/Alquiler_Mensual'] - cuota
    estructura_compra['pct_Cash_Req/Mes'] = int((float(estructura_compra['Sueldo_Mensual']) - float(estructura_compra['Ahorros_Mensuales'])) / float(estructura_compra['Sueldo_Mensual']) *100)
    estructura_alquiler['pct_Cash_Req/Mes'] = int(estructura_alquiler['pct_Cash_Req/Mes'] *100)
    
    # SUPUESTO: que le podes sacar x4 de interes que cobra el banco #TODO: agregar un input al usuario
    estructura_compra['interes_anual'] = buscar_valor('tasa_interes', almacenamiento_datos)
    estructura_alquiler['interes_anual'] = estructura_compra['interes_anual']  * 4
    estructura_alquiler['valor_casa'] = buscar_valor('valor_casa', almacenamiento_datos)
    estructura_compra['valor_casa'] = buscar_valor('valor_casa', almacenamiento_datos)


    time.sleep(1)
    print ('\nCHECKEO DEL COMPRAR')
    for elemento in estructura_compra:
        print (elemento, estructura_compra[elemento])
    time.sleep(1)
    print ('\nCHECKEO DEL ALQUILAR')
    for elemento in estructura_alquiler:
        print (elemento, estructura_alquiler[elemento])
    time.sleep(1)

    # CREANDO DATAFRAME CON LOS RESULTADOS

     # EXPORTANDO TODO EN EXCEL
main2()
