from tabla_seccion_superior import main
from packpy.elegir_formato import elegir_moneda_sistema
import time
import pandas as pd

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
    # time.sleep(0.4)
    time.sleep(0.4)
    print ('\nCHECKEO DEL VALOR DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicto)
    time.sleep(0.4)
    time.sleep(0.4)
    print ('\nCHECKEO DEL FORMATO DE LA VARIABLE')
    imprimir_variables(almacenamiento_datos.dicture)
    time.sleep(0.4)
    time.sleep(0.4)


    ## IMPORTANTE AL LECTOR:
    """Esta parte (tabla_seccion_inferior.py) fue el comienzo del desarrollo de TODO el código, y hay mucho que se va a implementar a continuación que debe ser removida he implementado dentro de los modulos importados"""
    # EJEMPLO: Ahora tengo que actualizar los valor de las estructuras_i, y volver a calcular el ahorro y el pct_Cash_Req/Mes
    # EJEMPLO: Le tengo que agregar "capital_inicial" = desembolso + notariado
    # EJEMPLO: Faltan de agregar variables como "PLAZO"

    exportar_pickle = False
    if exportar_pickle:
        import pickle
        with open('almacenamiento_datos.pickle', 'wb') as handle:
            pickle.dump(almacenamiento_datos, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('almacenamiento_datos.pickle', 'rb') as handle:
            file_loaded = pickle.load(handle)

        # search for type list values in file_loaded.dicto.keys()
        df = []
        for llave in file_loaded.dicto:
            if isinstance(file_loaded.dicto[llave], list):
                df.append({llave: file_loaded.dicto[llave]})
                print (f'{llave}: list')

    print ('\nARRANCANDO PARTE 2 DE LA DEMO:')

    from tabla_seccion_inferior import main


    estructura_alquiler, estructura_compra = main()

    estructura_alquiler['capital_inicial'] = buscar_valor('desembolso', almacenamiento_datos.dicto) + buscar_valor('notariado', almacenamiento_datos.dicto)
    estructura_compra['capital_inicial'] = estructura_alquiler['capital_inicial']

    label_notariado = buscar_valor('notariado_pct', almacenamiento_datos.dicto)
    label_desembolso = buscar_valor('desembolso_pct', almacenamiento_datos.dicto)

    label_notariado = f'notariado {label_notariado} %'
    label_desembolso = f'desembolso {label_desembolso} %'

    estructura_compra[label_notariado] = - buscar_valor('notariado', almacenamiento_datos.dicto)
    estructura_compra[label_desembolso] = - buscar_valor('desembolso', almacenamiento_datos.dicto)
    estructura_alquiler[label_notariado] = 0
    estructura_alquiler[label_desembolso] = 0

    estructura_compra['Hip/Alquiler_Mensual'] = - int(cuota)
    estructura_compra['Ahorros_Mensuales'] = int(estructura_compra['Sueldo_Mensual'] - cuota - estructura_compra['Gastos_Mantenimiento'] - estructura_compra['Gastos_Suministros'] - estructura_compra['Cash_Lifestyle'])
    estructura_compra['pct_Cash_Req/Mes'] = int((float(estructura_compra['Sueldo_Mensual']) - float(estructura_compra['Ahorros_Mensuales'])) / float(estructura_compra['Sueldo_Mensual']) *100)
    estructura_alquiler['pct_Cash_Req/Mes'] = int(estructura_alquiler['pct_Cash_Req/Mes'] *100)

    # SUPUESTO: que le podes sacar x4 de interes que cobra el banco #TODO: agregar un input al usuario
    estructura_compra['interes_anual'] = buscar_valor('tasa_interes', almacenamiento_datos.dicto)
    estructura_alquiler['interes_anual'] = estructura_compra['interes_anual']  * 4
    estructura_alquiler['valor_casa'] = buscar_valor('valor_casa', almacenamiento_datos.dicto)
    estructura_compra['valor_casa'] = buscar_valor('valor_casa', almacenamiento_datos.dicto)

    #TODO: REDONDEAR PCT_CASH_REQ_MES

    time.sleep(1)
    print ('\nCHECKEO DEL COMPRAR')
    for elemento in estructura_compra:
        print (elemento, estructura_compra[elemento])
    time.sleep(1)
    print ('\nCHECKEO DEL ALQUILAR')
    for elemento in estructura_alquiler:
        print (elemento, estructura_alquiler[elemento])
    time.sleep(1)

    # CREANDO DATAFRAMES
    hipoteca = pd.Series(estructura_compra.values(), estructura_compra.keys())
    alquiler = pd.Series(estructura_alquiler.values(), estructura_alquiler.keys())

    tabla_input = pd.DataFrame({
        'Hipoteca': hipoteca,
        'Alquiler': alquiler
    })

    tabla_input.loc['interes_anual','Hipoteca'] *= -1
    orden_variables = ['valor_casa', 'capital_inicial', 
    label_desembolso, label_notariado, 'interes_anual',
    'Sueldo_Mensual', 'Hip/Alquiler_Mensual', 'Ahorros_Mensuales',
    'Gastos_Mantenimiento', 'Gastos_Suministros', 'pct_Cash_Req/Mes', 'Cash_Lifestyle'
    ]

    tabla_input = tabla_input.reindex(index=orden_variables)
    new_rows = []
    for row in list(tabla_input.index):
        new_rows.append(row.replace('_',' ').title())

    tabla_input.to_excel('Input_ZARTEX_TOOL.xlsx')


    pago_intereses = buscar_valor('pago_interes', almacenamiento_datos.dicto)
    amortizacion = buscar_valor('amortizacion', almacenamiento_datos.dicto)
    saldo = buscar_valor('saldo', almacenamiento_datos.dicto)

    ahorro_mensual_hipoteca = tabla_input.loc['Ahorros Mensuales','Hipoteca']
    ahorro_mensual_alquiler = tabla_input.loc['Ahorros Mensuales','Alquiler']

    lista_amha = []
    lista_amaa = []
    lista_cuota = []

    diccionario_DEMO = {}
    for i in range(0, len(pago_intereses)+1):
        if i == 0:
            print ('Deuda total inicial: € {}'.format(almacenamiento_datos.formato_numerico(buscar_valor('valor_casa', almacenamiento_datos.dicto) - buscar_valor('desembolso', almacenamiento_datos.dicto))))
            print ('Cuota mensual hipoteca: € {}'.format(almacenamiento_datos.formato_numerico(buscar_valor('cuota', almacenamiento_datos.dicto))))
            continue
        
        numero_cuota = str(i)
        if i < 10:
            numero_cuota = '0' + str(i)
        lista_cuota.append('Cuota nº ' + numero_cuota)
        lista_amaa.append('€ ' + almacenamiento_datos.formato_numerico(int(ahorro_mensual_alquiler*i)))
        lista_amha.append('€ ' + almacenamiento_datos.formato_numerico(int(ahorro_mensual_hipoteca*i)))


    diccionario_DEMO['Cuota'] = lista_cuota
    diccionario_DEMO['Ahorro "Alquiler"'] = lista_amaa
    diccionario_DEMO['Ahorro "Hipoteca"'] = lista_amha
    diccionario_DEMO['Pago de Interés'] = pago_intereses
    diccionario_DEMO['Ahorro CASA'] = amortizacion
    diccionario_DEMO['Deuda Restante'] = saldo


    df_columns = diccionario_DEMO.keys()
    df_index = range(len(diccionario_DEMO['Cuota']))
    df = pd.DataFrame(diccionario_DEMO, index=df_index, columns=df_columns)

    df.to_csv('TABLA_RESUMEN_CUOTAS_FUTURAS.csv')


if __name__ == '__main__':
    main2()
    print ('Muchas gracias por usar el programa.')
    print ('Programa finalizado exitosamente')