from modelos.artista import Artista
from modelos.genero import Genero


class Banda(Artista):

    def __init__(self, id:str, nombre:str, tipo:str, genero:Genero, integrantes:[]):
        super().__init__(id,nombre,tipo,genero)
        self.__integrantes = integrantes

    #Comandos
    def establecerIntegrantes(self, integrantes:[]):
        self.__integrantes = integrantes

    #comandos
    def obtenerIntegrantes(self):
        return self.__integrantes

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": len(self.obtenerCanciones()),
            "integrantes": len(self.obtenerIntegrantes())
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": self._mapearCanciones(),
            "integrantes": self.obtenerIntegrantes()
        }