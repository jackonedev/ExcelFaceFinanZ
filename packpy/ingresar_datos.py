from itertools import count

def main():
    global contador_principal, contador_secundario_numerico
    
    contador_principal = count(1)
    contador_secundario_numerico = count(1)

main()

def ingresar_bool():#TODO: en desuso
    """
    #    print( 'Alquilas?')
    #    alquila = ingresar_bool()
    #    print( 'Alquila = {}'.format(bool(alquila)))
    """
    x_bool = count(1)
    x_bool_limit = 3  
    
    print( '< 1: Si >    < 0: No >'    )
    ingreso = input('>> ')
    if not (ingreso == '1' or ingreso == '0'):
        chance = next(x_bool) + 1
        print( 'Intento {} de {}'.format(chance, x_bool_limit))
        ingreso = input('>> ')

    if chance == x_bool_limit:
        print( 'Intento agotados\n')
        return
    print()
    return ingreso


def ingresar_numerico(label):#TODO: Decorators
    """
    Utilizado en 02_tabla_seccion_inferior.py
    Utilizado en 04_tabla_seccion_superior.py
    """
    global contador_secundario_numerico
    x_while = count(1)
    x_while_limit = 5

    print( '{}) "{}" debe ser un numero'.format(next(contador_secundario_numerico), label))
    ingreso = input('declaro = ')
    ingreso = ingreso.replace('.','')
    while not ingreso.isdigit():
        chance = next(x_while) + 1
        print( 'Intento {} de {}'.format(chance, x_while_limit))
        ingreso = input('Vuelva a ingresar "{}" = '.format(label))
        
        if chance == x_while_limit:
            print( 'Intentos agotados\n')
            return
    print()
    return int(ingreso)

def ingresar_cifra():
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
    cifra = input('Declarar cifra = ')
    
    if cifra.replace(",","") == cifra:
        if cifra.isdigit():
            if int(cifra) > 100:
                print( '1- cifra expresada monetariamente')
                return False, int(cifra)
            elif 0 <= int(cifra) <= 100:
                print( '1- cifra expresada porcentualmente')
                return True, float(cifra)/100
            else:
                print( '1- primera condicion fallida')
                return False, None

        elif cifra.replace(".","").isdigit():
            if cifra.count('.') > 1:
                print( '2- cifra expresada monetariamente')
                return False, int(cifra.replace(".",""))
            if int(float(cifra)) > 100:
                print( '2- cifra expresada monetariamente')
                return False, int(cifra.replace(".",""))
            elif 0 < int(float(cifra)) <= 100:
                print( '2- cifra expresada de forma porcentual')
                return True, float(cifra)/100
            elif int(float(cifra)) == 0:
                print( '2- cifra expresada de forma porcentual')
                return True, float(cifra)
            else:
                print( '2- segunda condicion fallida')
                return False, None
        
        elif cifra.replace(".","").replace("%","").isdigit():
            cifraux = cifra.replace(".","").replace("%","")
            if cifraux.count('.') == 0 and 0 <= int(cifraux) <= 100:
                #ERROR: 0.2% -> 0.02
                print( '3- cifra expresada de forma porcentual sin decimales')
                return True, float(cifraux)/100
            elif len(cifraux) > 2:
                print( '3- cifra expresada de forma porcentual con decimales')
                return True, float(cifra.replace('%',''))/100#TODO: toma como valor aceptable 101%
            else:#TODO: ESTOY ACA, PERO VOY A PROBAR '20.6' se me ocurre arreglar el exceso de decimales con un len al string y tomarlo para el round-loque importa es la posicion del punto 20.6, no es lo mismo que 2.06 
                print( '3- tercera condicion fallida')
                return False, None
                
        else:
            print( 'error etapa 1')

    elif cifra.count(',') > 0:
        if cifra.count(',') > 1:
            return 'No entiendo el numero'

        else:
            if cifra.replace(',','').isdigit(): 
                cifraux = cifra.replace(",",".")
                if int(float(cifraux)) > 0:
                    if int(float(cifraux)) > 1000: #TODO: de vuelta tener en cuenta si es para tontos, porque la logica que fuerza es margen intelectual que quito en otra variable - borra esta mierda
                        print( '4- cifra expresada de forma monetaria')
                        return False, int(float(cifraux))
                    
                    elif 0 < int(float(cifraux)) < 100:
                        print( '4- cifra expresada de forma porcentual entre 0 y 100')
                        return True, float(cifraux)/100

                elif int(float(cifraux)) == 0:
                    print( '4- cifra expresada de forma porcentual')
                    return True, float(cifraux)
                else:
                    print( '4- cuarta condicion fallida')
                    return False, None

            elif cifra.replace(',','').replace('.','').isdigit():
                cifraux = cifra.replace('.','').replace(',','.')
                if int(float(cifraux)) > 0:
                    print( '5- cifra expresada de forma monetaria')
                    return False, int(float(cifraux))
                elif int(float(cifraux)) == 0:
                    print( '5- cifra expresada de forma porcentual')
                    return True, float(cifraux)/100 #CHECK: input as: 2.100,6 no sense
                else:
                    print( '5- quinta condicion fallida')
                    return False, None
                    
            elif cifra.replace(',','').replace('.','').replace('%','').isdigit():
                cifraux = cifra.replace('.','').replace(',','.').replace('%','')
                if int(float(cifraux)) > 0:
                    if int(float(cifraux)) > 100:
                        print( '6- No tiene logica un numero tan grande con el valor %')
                    elif 0 < int(float(cifraux)) <= 100:
                        print( '6- cifra expresada de forma porcentual entre 0 y 100')
                        return True, float(cifraux)/100
                elif int(float(cifraux)) == 0:
                    print( '6- cifra expreado de forma porcentual')
                    return True, float(cifraux)
                else:
                    print( '6- sexta condicion fallida')
                    return False, None

            else:
                print( 'error etapa 2')


def ingresar_agno():
    global agno
    agno = input('Declarar agno = ')
    if agno.isdigit():
        if 5 <= int(agno) < 50:
            return int(agno)
        else:
            print ('No entiendo el numero')
            return
    else:
        print ('No entiendo el numero')
        return