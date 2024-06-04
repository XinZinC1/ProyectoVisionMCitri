import cv2
import os
import numpy as np

# Ruta de la carpeta con las imágenes
folder_path = r"C:\Users\Alumno\Documents\gogogo\MC\mcp1"

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
        new_filename = f"edited_{filename}"
        new_file_path = os.path.join(folder_path, new_filename)
        cv2.imwrite(new_file_path, image)
        
        print(f"Imagen editada: {new_filename}")