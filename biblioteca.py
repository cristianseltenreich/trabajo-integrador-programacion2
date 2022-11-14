# librerias
import os
import json

# modelos
from modelos.artista import Artista
from modelos.banda import Banda
from modelos.cancion import Cancion
from modelos.album import Album
from modelos.genero import Genero


class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    __artistas = []
    __canciones = []
    __albumes = []
    __generos = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    def obtenerArtistas(orden=None, reverso=False):
        artistas = Biblioteca.__artistas
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'tipo':
                pass
        return artistas

    def obtenerCanciones(orden=None, reverso=False):
        canciones = Biblioteca.__canciones
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
        return canciones

    def obtenerAlbumes(orden=None, reverso=False):
        albumes = Biblioteca.__albumes
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
            elif orden == 'anio':
                pass
        return albumes

    def obtenerGeneros(orden=None, reverso=False):
        generos = Biblioteca.__generos
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
        return generos
    
    def buscarArtista(id):
        artistas = Biblioteca.__artistas
        artista = None
        for a in artistas:
            if a['id'] == id:
                artista = Banda(a['id'], a['nombre'], a['tipo'], a['integrantes'], Biblioteca.buscarGenero(a['genero']))
        return artista

    def buscarCancion(id):
        canciones = Biblioteca.__canciones
        cancion = None
        for c in canciones:
            if c['id'] == id:
                cancion = Cancion(c['id'], c['nombre'], c['artista'])
        return cancion
    
    def buscarAlbum(id):
        albumes = Biblioteca.__albumes
        album = None
        for a in albumes:
            if a['id'] == id:
                album = Album(a['id'], a['nombre'], a['anio'], a['genero'], a['artista'], a['canciones'])
        return album

    def buscarGenero(id):
        generos = Biblioteca.__generos
        genero = None
        for g in generos:
            if g['id'] == id:
                genero = Genero(g['id'], g['nombre'])
        return genero
    
    def __parsearArchivoDeDatos():
        with open(Biblioteca.__archivoDeDatos, 'r') as f:
            data = json.load(f)
        return data

    def __convertirJsonAListas(lista):
        Biblioteca.__artistas = lista['artistas']
        Biblioteca.__canciones = lista['canciones']
        Biblioteca.__albumes = lista['albumes']
        Biblioteca.__generos = lista['generos']