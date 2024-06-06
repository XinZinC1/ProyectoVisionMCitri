from PIL import Image, ImageEnhance, ImageOps
import random
import cv2
import os
import numpy as np

# Función para aplicar random horizontal flipping
def flip_image():
    image_folder = r'C:\Users\aguir\Documentos\MC1\HOJAS'
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            flipped_image = ImageOps.mirror(image)
            flipped_image.save(os.path.join(image_folder, '1' + os.path.basename(image_path)))
def apply_hpf_filter():
    folder_path = r"C:\Users\aguir\Documentos\MC1\HOJAS"
    # Itera sobre los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Construye la ruta completa del archivo
            file_path = os.path.join(folder_path, filename)
            
            # Abre la imagen
            image = cv2.imread(file_path)
            
            # Aplica el filtro paso alto
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            image = cv2.filter2D(image, -1, kernel)
            
            # Guarda la imagen editada con un nuevo nombre
            new_filename = f"4{filename}"
            new_file_path = os.path.join(folder_path, new_filename)
            cv2.imwrite(new_file_path, image)

def adjust_image():
    folder_path = r"C:\Users\aguir\Documentos\MC1\HOJAS"
    output_folder1=r"C:\Users\aguir\Documentos\MC1\AJUSTE"
    # Parámetros de edición
    brightness_factor = 1.25  # Ajusta el brillo (1.0 = sin cambios)
    contrast_factor = 1.05  # Ajusta el contraste (1.0 = sin cambios)
    highlights_factor = 1.05  # Ajusta las altas luces (1.0 = sin cambios)
    shadows_factor = 1.05 # Ajusta las sombras (1.0 = sin cambios)
    sharpness_factor = 0.15  # Ajusta la nitidez (1.0 = sin cambios)

    # Itera sobre los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Construye la ruta completa del archivo
            file_path = os.path.join(folder_path, filename)
            
            # Abre la imagen
            image = Image.open(file_path)
            
            # Ajusta el brillo
            brightness_enhancer = ImageEnhance.Brightness(image)
            image = brightness_enhancer.enhance(brightness_factor)
            
            # Ajusta el contraste
            contrast_enhancer = ImageEnhance.Contrast(image)
            image = contrast_enhancer.enhance(contrast_factor)
            
            # Ajusta las altas luces
            highlights_enhancer = ImageEnhance.Brightness(image)
            image = highlights_enhancer.enhance(highlights_factor)
            
            # Ajusta las sombras
            shadows_enhancer = ImageEnhance.Brightness(image)
            image = shadows_enhancer.enhance(shadows_factor)
            
            # Ajusta la nitidez
            sharpness_enhancer = ImageEnhance.Sharpness(image)
            image = sharpness_enhancer.enhance(sharpness_factor)
            
            # Guarda la imagen editada con un nuevo nombre
            new_filename = f"3{filename}"
            new_file_path = os.path.join(output_folder1, new_filename)
            image.save(new_file_path)



# Ejecuta las funciones secuencialmente
flip_image()
apply_hpf_filter()
adjust_image()
print("Fotos editadas.")
