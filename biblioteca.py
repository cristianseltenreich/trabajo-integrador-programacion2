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
                artistas = sorted(artistas, key=lambda a: a['nombre'], reverse=reverso)
            elif orden == 'tipo':
                artistas = sorted(artistas, key=lambda a: a['tipo'], reverse=reverso)
        return artistas

    def obtenerCanciones(orden=None, reverso=False):
        canciones = Biblioteca.__canciones
        if isinstance(orden, str):
            if orden == 'nombre':
                canciones = sorted(canciones, key=lambda c: c['nombre'], reverse=reverso)
            elif orden == 'artista':
                canciones = sorted(canciones, key=lambda c: c['artista'], reverse=reverso)
        return canciones

    def obtenerAlbumes(orden=None, reverso=False):
        albumes = Biblioteca.__albumes
        if isinstance(orden, str):
            if orden == 'nombre':
                albumes = sorted(albumes, key=lambda a: a['nombre'], reverse=reverso)
            elif orden == 'artista':
                albumes = sorted(albumes, key=lambda a: a['artista'], reverse=reverso)
            elif orden == 'anio':
                albumes = sorted(albumes, key=lambda a: a['anio'], reverse=reverso)
        return albumes

    def obtenerGeneros(orden=None, reverso=False):
        generos = Biblioteca.__generos
        if isinstance(orden, str):
            if orden == 'nombre':
                generos = sorted(generos, key=lambda a: a.obtenerNombre(), reverse=reverso)
        return generos
    
    def buscarArtista(id:str):
        artistas = Biblioteca.__artistas
        artista = None
        for a in artistas:
            if a['id'] == id:
                if a['tipo'] == "banda":
                    artista = Banda(a['id'], a['nombre'], a['tipo'], a['integrantes'], Biblioteca.buscarGenero(a['genero']))
                if a['tipo'] == "banda":
                    artista = Artista(a['id'], a['nombre'], a['tipo'], Biblioteca.buscarGenero(a['genero']))
        return artista

    def buscarCancion(id):
        canciones = Biblioteca.__canciones
        cancion = None
        for c in canciones:
            if c['id'] == id:
                cancion = Cancion(c['id'], c['nombre'], c['artista'])
        return cancion
    
    def buscarAlbum(id:str):
        albumes = Biblioteca.__albumes
        album = None
        for a in albumes:
            if a['id'] == id:
                album = Album(a['id'], a['nombre'], a['anio'], a['genero'], a['artista'], a['canciones'])
        return album
    def obtenerAlbumDeCancion(id):
        albumes = Biblioteca.__albumes
        album = None
        for a in albumes:
            for c in a['canciones']:
                if id == c['id']:
                    album = Album(a['id'], a['nombre'], a['anio'], a['genero'], a['artista'], a['canciones'])
        return album

    def buscarGenero(id:str):
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

