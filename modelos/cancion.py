import json

import biblioteca


class Cancion:

    def __init__(self, id:str, nombre:str, artista:str):
        self.__id = id
        self.__nombre = nombre
        self.__artista = artista

    #Comandos
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecerArtista(self, artista:str):
        self.__artista = artista

    #Consultas
    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerArtista(self):
        return biblioteca.Biblioteca.buscarArtista(self.__artista)

    def obtenerAlbum(self):
        return biblioteca.Biblioteca.obtenerAlbumDeCancion(self.__id)

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "artista": self.obtenerArtista().obtenerNombre(),
            "album": self.obtenerAlbum().obtenerNombre()
        }
        
    def convertirAJSONFull(self):
        return self.convertirAJSON()

    def __eq__(self, other):
        return self.__id == other.obtenerId()