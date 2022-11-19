import json

import biblioteca
from modelos.genero import Genero


class Artista:

    def __init__(self, id:str, nombre:str, tipo:str, genero:Genero):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__genero = genero

    #Comandos
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerTipo(self, tipo:str):
        self.__tipo = tipo

    def establecerGenero(self, genero:Genero):
        self.__genero = genero

    #Consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerTipo(self):
        return self.__tipo

    def obtenerGenero(self):
        return self.__genero

    def obtenerCanciones(self):
        canciones = []
        for c in biblioteca.Biblioteca.obtenerCanciones():
            if self == c.obtenerArtista():
                canciones.append(c)
        return canciones

    def obtenerAlbumes(self):
        albumes = []
        for a in biblioteca.Biblioteca.obtenerAlbumes():
            if self == a.obtenerArtista():
                albumes.append(a)
        return albumes

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": self._mapearCanciones()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "tipo": self.obtenerTipo(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "albumes": self._mapearAlbumes(),
            "canciones": self._mapearCanciones()
        }

    def _mapearAlbumes(self):
        albumes = self.obtenerAlbumes()
        albumesMapa = map(
            lambda a: {"nombre": a.obtenerNombre(), "anio": a.obtenerAnio()}, albumes)
        return list(albumesMapa)

    def _mapearCanciones(self):
        canciones = self.obtenerCanciones()
        cancionesMapa = map(lambda c: c.obtenerNombre(), canciones)
        return list(cancionesMapa)

    def __eq__(self, other):
        return self.__id == other.obtenerId()