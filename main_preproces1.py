from PIL import Image, ImageEnhance, ImageOps
import random
import cv2
import os
import numpy as np
from tqdm import tqdm
from time import sleep


# Función para aplicar random horizontal flipping
def flip_image():
    carpeta = r'HOJAS'
    for filename in os.listdir(carpeta):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            ruta = os.path.join(carpeta, filename)
            imagen = Image.open(ruta)
            imagen_flip = ImageOps.mirror(imagen)
            imagen_flip.save(os.path.join(carpeta, 'flip_' + os.path.basename(ruta)))
def apply_hpf_filter():
    carpeta_imagenes = r"HOJAS"
    # Itera sobre los archivos en la carpeta
    for filename in os.listdir(carpeta_imagenes):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Construye la ruta completa del archivo
            ruta = os.path.join(carpeta_imagenes, filename)
            
            # Abre la imagen
            imagen = cv2.imread(ruta)
            
            # Aplica el filtro paso alto
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            imagen = cv2.filter2D(imagen, -1, kernel)
            
            # Guarda la imagen editada con un nuevo nombre
            nombre_imagen = f"hpf_{filename}"
            nuevo_ruta = os.path.join(carpeta_imagenes, nombre_imagen)
            cv2.imwrite(nuevo_ruta, imagen)

def adjust_image():
    carpeta_imagenes = r"HOJAS"
    carpeta_final=r"AJUSTE"
    # Parámetros de edición
    brillo = 1.25  # Ajusta el brillo (1.0 = sin cambios)
    contraste = 1.05  # Ajusta el contraste (1.0 = sin cambios)
    altas_luces = 1.05  # Ajusta las altas luces (1.0 = sin cambios)
    sombras = 1.05 # Ajusta las sombras (1.0 = sin cambios)
    nitidez = 0.15  # Ajusta la nitidez (1.0 = sin cambios)

    # Itera sobre los archivos en la carpeta
    for filename in os.listdir(carpeta_imagenes):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Construye la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta_imagenes, filename)
            
            # Abre la imagen
            imagen = Image.open(ruta_archivo)
            
            # Ajusta el brillo
            ajuste_brillo = ImageEnhance.Brightness(imagen)
            imagen = ajuste_brillo.enhance(brillo)
            
            # Ajusta el contraste
            ajuste_contraste = ImageEnhance.Contrast(imagen)
            imagen = ajuste_contraste.enhance(contraste)
            
            # Ajusta las altas luces
            ajuste_altasluces = ImageEnhance.Brightness(imagen)
            imagen = ajuste_altasluces.enhance(altas_luces)
            
            # Ajusta las sombras
            ajuste_sombra = ImageEnhance.Brightness(imagen)
            imagen = ajuste_sombra.enhance(sombras)
            
            # Ajusta la nitidez
            ajuste_nitidez = ImageEnhance.Sharpness(imagen)
            imagen = ajuste_nitidez.enhance(nitidez)
            
            # Guarda la imagen editada con un nuevo nombre
            nuevo_nombre = f"edit_{filename}"
            nueva_ruta = os.path.join(carpeta_final, nuevo_nombre)
            imagen.save(nueva_ruta)

# Ejecuta las funciones secuencialmente
for i in tqdm(range(1)):
    flip_image()
    sleep(0.1)
    print(" Horizontal flip aplicado.")
for i in tqdm(range(1)):
    apply_hpf_filter()
    sleep(0.1)
    print(" HPF aplicado.")
for i in tqdm(range(1)):
    adjust_image()
    sleep(0.1)
    print(" Ajuste de imagenes culminado.")
