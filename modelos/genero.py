import json


class Genero:

    def __init__(self, id:str, nombre:str):
        self.__id = id
        self.__nombre = nombre

    #Comandos
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    #Consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }

    def __eq__(self, other):
        return self.__id == other.obtenerId()