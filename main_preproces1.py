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
            file_path = os.path.join(carpeta_imagenes, filename)
            
            # Abre la imagen
            image = Image.open(file_path)
            
            # Ajusta el brillo
            brightness_enhancer = ImageEnhance.Brightness(image)
            image = brightness_enhancer.enhance(brillo)
            
            # Ajusta el contraste
            contrast_enhancer = ImageEnhance.Contrast(image)
            image = contrast_enhancer.enhance(contraste)
            
            # Ajusta las altas luces
            highlights_enhancer = ImageEnhance.Brightness(image)
            image = highlights_enhancer.enhance(altas_luces)
            
            # Ajusta las sombras
            shadows_enhancer = ImageEnhance.Brightness(image)
            image = shadows_enhancer.enhance(sombras)
            
            # Ajusta la nitidez
            sharpness_enhancer = ImageEnhance.Sharpness(image)
            image = sharpness_enhancer.enhance(nitidez)
            
            # Guarda la imagen editada con un nuevo nombre
            new_filename = f"edit_{filename}"
            new_file_path = os.path.join(carpeta_final, new_filename)
            image.save(new_file_path)



# Ejecuta las funciones secuencialmente
for i in tqdm(range(1)):
    flip_image()
    sleep(0.001)
    print(" Horizontal flip aplicado.")
for i in tqdm(range(1)):
    apply_hpf_filter()
    sleep(0.001)
    print(" HPF aplicado.")
for i in tqdm(range(1)):
    adjust_image()
    sleep(0.001)
    print(" Ajuste de imagenes culminado.")
