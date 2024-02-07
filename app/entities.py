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