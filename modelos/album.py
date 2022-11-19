import json

import biblioteca

class Album:

    def __init__(self, id:str, nombre:str, anio:int, genero:str, artista:str, canciones:[]):
        self.__id = id
        self.__nombre = nombre
        self.__anio = anio
        self.__genero = genero
        self.__artista = artista
        self.__canciones = canciones

    #Comandos
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerAnio(self, anio:int):
        self.__anio = anio

    def establecerGenero(self, genero:str):
        self.__genero = genero

    def establecerArtista(self, artista:str):
        self.__artista = artista

    #Consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerAnio(self):
        return self.__anio

    def obtenerGenero(self):
        return biblioteca.Biblioteca.buscarGenero(self.__genero)

    def obtenerArtista(self):
        return biblioteca.Biblioteca.buscarArtista(self.__artista)

    def obtenerCanciones(self):
        canciones = []
        for c in biblioteca.Biblioteca.obtenerCanciones():
            for can in self.__canciones:
                if can['id'] == c.obtenerId():
                    canciones.append(c)
        return canciones

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "anio": self.obtenerAnio(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "canciones": self._mapearCanciones()
        }

    def _mapearCanciones(self):
        canciones = self.obtenerCanciones()
        cancionesMapa = map(lambda c: c.obtenerNombre(), canciones)
        return list(cancionesMapa)

    def __eq__(self, other):
        return self.__id == other.obtenerId()