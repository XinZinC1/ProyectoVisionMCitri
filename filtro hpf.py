from PIL import Image, ImageEnhance, ImageOps
import random
import cv2
import os
import numpy as np

def apply_sobel_filter():
    folder_path = r"C:\Users\aguir\Documentos\MC1\HOJAS"
    output_folder1=r"C:\Users\aguir\Documentos\MC1\si\SOBEL"
    # Itera sobre los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Construye la ruta completa del archivo
            file_path = os.path.join(folder_path, filename)
            
            # Abre la imagen
            image = cv2.imread(file_path)
            
            # Aplica el filtro de Sobel para detectar bordes verticales
            vertical_sobel = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
            
            # Aplica el filtro de Sobel para detectar bordes horizontales
            horizontal_sobel = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)
            
            # Combina los resultados para obtener la imagen con bordes detectados
            gradient = cv2.bitwise_or(vertical_sobel, horizontal_sobel)
            
            # Guarda la imagen editada con un nuevo nombre
            new_filename = f"_{filename}"
            new_file_path = os.path.join(output_folder1, new_filename)
            cv2.imwrite(new_file_path, gradient)
# Función para aplicar redimensionamiento
def resize_image():
    image_folder = r'C:\Users\aguir\Documentos\MC1\ROTACION'
    destination_folder = r'C:\Users\aguir\Documentos\MC1\REDIMENSION'
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            new_width = random.randint(100, width)
            new_height = random.randint(100, height)
            resized_image = image.resize((new_width, new_height))
            resized_image.save(os.path.join(destination_folder, '_' + os.path.basename(image_path)))

# Función para aplicar random cropping
def crop_image():
    image_folder = r'C:\Users\aguir\Documentos\MC1\REDIMENSION'
    destination_folder = r'C:\Users\aguir\Documentos\MC1\CROP'
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            x = random.randint(0, width - 100)
            y = random.randint(0, height - 100)
            cropped_image = image.crop((x, y, x + 100, y + 100))
            cropped_image.save(os.path.join(destination_folder, 'e' + os.path.basename(image_path)))
def rotate_image():
    image_folder = r'C:\Users\aguir\Documentos\MC1\HOJAS'
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            angle = random.randint(0, 360)
            rotated_image = image.rotate(angle)
            rotated_image.save(os.path.join(image_folder, '2' + os.path.basename(image_path)))

apply_sobel_filter()
#resize_image()
#crop_image() 

#rotate_image()