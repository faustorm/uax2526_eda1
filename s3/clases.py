import time

class Persona:
    def __init__(self,nombre,ano, estudios = [], documento = None, tipo_documento = None):
        self.nombre = nombre
        self.ano_nacimiento = ano
        self.edad = time.year - self.ano
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.estudios = estudios

    def saludar(self):
        saludo = f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
        print(saludo)

    def get_documento(self):
        if documento == None or tipo_documento == None:
            return False
        else:
            return { "documento": documento, "tipo_documento": tipo_documento}
    
    def print_documento(self):
        if documento == None or tipo_documento == None:
            print(f"No hay información sobre el documento de {self.nombre}")
        else:
            print(f"El {self.tipo_documento} de {self.nombre} es {self.documento}")
        
    def add_estudio(self, estudio):
        self.estudios.append(estudio)
        print(f"{estudio} añadido con éxito")
    
    def print_estudios(self):
        print(", ".join(self.estudios))