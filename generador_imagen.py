"""
Jahiron Mateo Guzman
Matricula: 20221569
Temporada II - Practica
"""

#Librerias necesarias:

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def generador_img():

    """Esta funcion basica crea una imagen a la cual va aplicando transformaciones
    para luego guardarlas de manera individual con los diferentes pasos aplicados.

    Utiliza solo un valor de entrada para crear una matriz cuadrada.
    """

    dimensiones = int(input("Introduce el valor para tu matriz cuadrada: "))

    #Creacion de imagen vacia con fondo negro:
    mi_recuadro = np.ones((dimensiones, dimensiones, 3), np.uint8)
    cuadro_vacio = cv.imwrite("Imagen_blanco.png", mi_recuadro)


    #Creacion de lineas y forams en la imagen:
    cv.line(mi_recuadro, (0, 0), (500, 500), (255, 0, 0), 5)
    cv.rectangle(mi_recuadro, (110, 200), (410, 300), (0, 255, 0), 3)
    cv.circle(mi_recuadro, (250, 250), 40, (0, 0, 225), 8)
    imagen_formas = cv.imwrite("Imagen_formas.png", mi_recuadro)

    #Texto en las imagenes:
    font = cv.FONT_HERSHEY_PLAIN  # tipografia de letra
    cv.putText(mi_recuadro, "Creado por Jahiron Mateo G.", (50, 400), font, 1.3, (0, 255, 255), 2, cv.LINE_AA)
    imagen_texto =  imagen_formas = cv.imwrite("Imagen_texto.png", mi_recuadro)

    #Escala de grises:
    gris = cv.cvtColor(mi_recuadro, cv.COLOR_BGR2GRAY)
    imagen_escala_grises = cv.imwrite("Imagen_escala_gris.png", gris)

    #Expansion de imagen al doble:
    imagen_r = cv.resize(mi_recuadro, ((dimensiones*2), (dimensiones*2)), interpolation=cv.INTER_LINEAR)
    imagen_x2 = cv.imwrite("Imagen_increment_x2.png", imagen_r)

    #Rotacion de imagen:

    (altur, ancho) = mi_recuadro.shape[:2]  # 10
    centro = (ancho // 2, altur // 2)

    rotacion = cv.getRotationMatrix2D(centro, 45, 1)
    rotada = cv.warpAffine(mi_recuadro, rotacion, (600, 600))
    imagen_rotada_45 = cv.imwrite("Rotacion_45_grados.png", rotada)


    return (cuadro_vacio,
            imagen_formas,
            imagen_texto,
            imagen_escala_grises,
            imagen_x2,
            imagen_rotada_45)


generador_img()






