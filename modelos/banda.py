from modelos.artista import Artista


class Banda(Artista):

    def __init__(self, id:str, nombre:str, tipo:str, genero:str, integrantes:[]):
        super().__init__(id,nombre,tipo,genero)
        self.__integrantes = integrantes

    #Comandos
    def establecerIntegrantes(self, integrantes:[]):
        self.__integrantes = integrantes

    #comandos
    def obtenerIntegrantes(self):
        return self.__integrantes