import sys
from itertools import count


###
#####   SALIENDO DEL PROGRAMA
###

sys.exit(0)



class Dicto:

    contador = count()
    copia_contador = 0
    dicto = {} # para almacenar solo datos
    dicture = {} # para almacenar formatos
    
    def __init__(self, name, coment=''):
        self.name = name #referencia al fichero o al tipo de variable
        self.coment = coment
        
    def ingresar(self, nombre, valor):
        nombre = nombre.replace(' ', '_')
        key_label = self.nombre_key_dicto(nombre_variable=nombre)
        self.dicto[key_label] = valor
        
        key_label = self.nombre_key_dicture(nombre_variable=nombre)# ESTA: es la ultima vez que se aplica nombre_key_dicture
        self.dicture[key_label] = '' 
        
    def nombre_key_dicto(self, nombre_variable):#METODO INTERNO
        self.copia_contador = next(self.contador)#ESTE: debería ser el único next() que uso y me quedo con la copia
        return 'z{}-{}-{}'.format(self.copia_contador, nombre_variable, self.name)
      
    def nombre_key_dicture(self, nombre_variable):
        return 'z{}-{}-{}'.format(self.copia_contador,nombre_variable, self.name)
        
    def ultimo_registro(self): #METODO INTERNO
        lista_ds = []
        for key in self.dicto.keys():
            key = key.split('-')
            key = key[0].replace('z','')
            try:
                key = int(key)
                lista_ds.append(key)
            except:
                pass
      
        key = str(max(lista_ds))
        key = 'z{}'.format(key)
        for keys in self.dicto.keys():
            if keys.startswith(key):
                key = keys
                break
        return key

    def prefijo(self, prefix):
      
        key = self.ultimo_registro()
        for elemento in self.dicto.keys():
            if elemento == key:
                valor = self.dicto[key]
                valor = self.formato_numerico(valor)
        self.dicture[key] = '{} {}'.format(prefix, valor)
    
    def formato_numerico(self, valor):
        valor = str(valor)
        longitud_valor = len(valor)

        resto_3 = longitud_valor % 3
        valor2 = valor[:resto_3]
        for i, numero in enumerate(valor[resto_3:]):
            if i == 0 and resto_3 != 0:
                valor2 += '.'
            elif i % 3 == 0 and i != 0:
                valor2 += '.'
            valor2 += numero
        return valor2

    def sufijo(self, sufix):
        key = self.ultimo_registro()
        for elemento in self.dicto.keys():
            if elemento == key:
                valor = self.dicto[key]
                valor = str(valor).replace(' ', '_').replace('.', ',')
        self.dicture[key] = '{} {}'.format(valor, sufix)
        
    def __str__(self):
        key = self.ultimo_registro()
        for elemento in self.dicture.keys():
            if elemento == key:
                label = self.dicture[key]
        return 'Mostrando ultimo registro: {}'.format(label)


        
valor_casa = 2200000
almacenar_valor = Dicto(name='hip_alquiler')

almacenar_valor.ingresar('valor_casa', valor_casa)
almacenar_valor.prefijo('¤')
print almacenar_valor


almacenar_valor.ingresar('desembolso', 500000)
almacenar_valor.prefijo('¤')
print almacenar_valor

almacenar_valor.ingresar('desembolso_pct', 4.0)
almacenar_valor.sufijo('%')
print almacenar_valor



sys.exit(0)
#problema de compatibilidad 2_7 3_10
        # buscar el valor de dicto, juntarlo con valor, y almacenarlo en dicture
        ####
        #### TENGO UN PROBLEMA: en 2_7 las keys del dict me la ordena por tamaño y en 3_10 por orden
        ####
        ## Vamos a usar los contadores
        ## poner las keys en una lista, 
        ## separar cada key por '-'
        ## quedarse con el primero
        ## hacer pop de 'd'
        ## hacer un try int
        ## quedarse con el valor maximo
        ## convertirlo a str y agregarle una 'z'
        ## iterar en keys() hasta .startswith()
        ## obtengo la key
        ##
        ####
lista_key = ['z4-cash_lifestyle-variable_hipoteca', 'z2-hip_alq_mes-variable_hipoteca', 'z1-mantenimeiento-variable_hipoteca',
'z0-valor_casa-variable_hipoteca','z3-valor_sumi-variable_hipoteca']

lista_ds = []
for key in lista_key:
    key = key.split('-')
    key = key[0].replace('z','')
    try:
        key = int(key)
        lista_ds.append(key) #Osado
    except:
        pass
      
key = str(max(lista_ds))
key = 'z{}'.format(key)

for keys in lista_key:
    if keys.startswith(key):
        print 'Hola mundo'
        key = keys
        break# FIN DE OBTENER LA KEY
      
for elemento in self.dicto.keys():
    if elemento == key:
        valor = self.dicto[key]
        valor = str(valor).replace(' ', '_')#asegurarse que no haya espacio en blanco 
        prefix = ''
      






sys.exit(0)
#Estructura de código creada para determinar el desembolso de capital para comprar una casa
def ingrsar_cifra():
    global cifra
    cifra = raw_input('Declarar cifra = ')
    
    if cifra.replace(",","") == cifra:
        if cifra.isdigit():
            if int(cifra) > 100:
                print '1- cifra expresada monetariamente'
            elif 0 <= int(cifra) <= 100:
                print '1- cifra expresada porcentualmente'
            else:
                print '1- primera condicion fallida'

        elif cifra.replace(".","").isdigit():
            if int(float(cifra)) > 100:
                print '2- cifra expresada monetariamente'
            elif 0 <= int(float(cifra)) <= 100:
                print '2- cifra expresada de forma porcentual'
            elif int(float(cifra)) == 0:
                print '2- cifra expresada de forma porcentual'
            else:
                print '2- segunda condicion fallida'
        
        elif cifra.replace(".","").replace("%","").isdigit():
            cifraux = cifra.replace(".","").replace("%","")
            if cifraux.count('.') == 0 and 0 <= int(cifraux) <= 100:
                print '3- cifra expresada de forma porcentual sin decimales'
            elif len(cifraux) > 2:
                print '3- cifra expresada de forma porcentual con decimales'
            else:
                print '3- tercera condicion fallida'
                
        else:
            print 'error etapa 1'

    elif cifra.count(',') > 0:
        if cifra.count(',') > 1:
            return 'No entiendo el numero'

        else:
            if cifra.replace(',','').isdigit(): 
                cifraux = cifra.replace(",",".")#check
                if int(float(cifraux)) > 0:
                    print '4- cifra expresada de forma monetaria'
                elif int(float(cifraux)) == 0:
                    print '4- cifra expresada de forma porcentual'
                else:
                    print '4- cuarta condicion fallida'

            elif cifra.replace(',','').replace('.','').isdigit():
                cifraux = cifra.replace('.','').replace(',','.')
                if int(float(cifraux)) > 0:
                    print '5- cifra expresada de forma monetaria'
                elif int(float(cifraux)) == 0:
                    print '5- cifra expresada de forma porcentual'
                else:
                    print '5- quinta condicion fallida'
                    
            elif cifra.replace(',','').replace('.','').replace('%','').isdigit():
                cifraux = cifra.replace(',','').replace('.','').replace('%','')
                if int(float(cifraux)) > 0:
                    print '6- cifra expresada de forma monetaria'
                elif int(float(cifraux)) == 0:
                    print '6- cifra expreado de forma porcentual'
                else:
                    print '6- sexta condicion fallida'

            else:
                print 'error etapa 2'