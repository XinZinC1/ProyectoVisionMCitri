import cv2
import os

# Ruta de la carpeta con las imágenes
folder_path = r"C:\Users\Alumno\Documents\gogogo\SANO\sn\hpf\hpf1"

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
        new_filename = f"edited_{filename}"
        new_file_path = os.path.join(folder_path, new_filename)
        cv2.imwrite(new_file_path, gradient)
        
        print(f"Imagen editada: {new_filename}")