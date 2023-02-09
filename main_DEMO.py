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

    time.sleep(0.4)
    print ('\nFINALIZANDO PARTE 1 DE LA DEMO:')
    time.sleep(0.4)
    print ('\nCHECKEO DEL VALOR DE LA VARIABLE')
    time.sleep(0.4)
    imprimir_variables(almacenamiento_datos.dicto)
    time.sleep(0.4)
    print ('\nCHECKEO DEL FORMATO DE LA VARIABLE')
    time.sleep(0.4)
    imprimir_variables(almacenamiento_datos.dicture)
    time.sleep(0.4)


main2()
