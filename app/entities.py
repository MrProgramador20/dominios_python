class carro():

    #crear metodo constructor
    def __init__(self, placa, tipo_vehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipo_vehiculo 
    
    
class cliente():
    
    #metodo constructor cliente 
    def __init__(self, nombre, edad, genero, documento, celular, licencia, lista_carros):
    
        self.nombre = nombre
        self.edad = edad
        self.genero = genero 
        self.documento = documento
        self.celular = celular 
        self.licencia = licencia
        self.lista_carros = lista_carros
        
    def addCar(self, car):
        self.lista_carros.append(car)
        
    def listCar(self):
        for  i in self.lista_carros:
             print('Carro con placas: ' + i.placa )

class cupo():
    
    def __init__(self, letra):
        self.letra = letra
        
class pago():
    
    def __init__(self, fecha_inicio, hora_inicio, fecha_fin, hora_fin, valor, carro, cupo, empleado):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor 
        self.carro = carro
        self.cupo = cupo
        self.empleado = empleado

class empleado():
    
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

