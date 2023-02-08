from itertools import count



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
        self.copia_contador = next(self.contador)#ESTE: unico next()
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
                if isinstance(valor, float):#CHECK
                  valor = round(valor, 2)
                valor = str(valor).replace(' ', '_').replace('.', ',')
        self.dicture[key] = '{} {}'.format(valor, sufix)
        
    def __str__(self):
        key = self.ultimo_registro()
        for elemento in self.dicture.keys():
            if elemento == key:
                label = self.dicture[key]
        key = key.split('-')
        key = key[0].replace('z','')
        return 'regz{}: {}'.format(key, label)
