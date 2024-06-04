from PIL import Image, ImageEnhance
import os

# Ruta de la carpeta con las imágenes
ruta_folder = r"D:\VisualStudioCode\VisionCMCitri\MC001"
#folder_path = os.path.dirname(__file__)

# Ruta de la carpeta para guardar las imágenes editadas
ruta_folder_editado = os.path.join("D:\VisualStudioCode\VisionCMCitri\MCProcesadas", "edited_images")

# Crear la carpeta de salida si no existe
if not os.path.exists(ruta_folder_editado):
    os.makedirs(ruta_folder_editado)

# Parámetros de edición
factor_brillo = 1.25  # Ajusta el brillo (1.0 = sin cambios)
factor_contraste = 1.05  # Ajusta el contraste (1.0 = sin cambios)
factor_luces = 1.05  # Ajusta las altas luces (1.0 = sin cambios)
factor_sombras = 1.05 # Ajusta las sombras (1.0 = sin cambios
factor_nitidez = 0.15  # Ajusta la nitidez (1.0 = sin cambios)

# Itera sobre los archivos en la carpeta
for archivo_base in os.listdir(ruta_folder):
    if archivo_base.endswith(".jpg") or archivo_base.endswith(".png"):
        # Construye la ruta completa del archivo
        ruta_archivo = os.path.join(ruta_folder, archivo_base)
        
        # Abre la imagen
        imagen_base = Image.open(ruta_archivo)
        
        # Ajusta el brillo
        ajuste_brillo = ImageEnhance.Brightness(imagen_base)
        imagen_base = ajuste_brillo.enhance(factor_brillo)
        
        # Ajusta el contraste
        ajuste_contraste = ImageEnhance.Contrast(imagen_base)
        imagen_base = ajuste_contraste.enhance(factor_contraste)
        
        # Ajusta las altas luces
        ajuste_luces = ImageEnhance.Brightness(imagen_base)
        imagen_base = ajuste_luces.enhance(factor_luces)
        
        # Ajusta las sombras
        ajuste_sombras = ImageEnhance.Brightness(imagen_base)
        imagen_base = ajuste_sombras.enhance(factor_sombras)
        
        # Ajusta la nitidez
        ajuste_nitidez = ImageEnhance.Sharpness(imagen_base)
        imagen_base = ajuste_nitidez.enhance(factor_nitidez)
        
        # Guarda la imagen editada con un nuevo nombre
        nuevo_nombre_archivo = f"edited_{archivo_base}"
        nuevo_ruta_archivo = os.path.join(ruta_folder, nuevo_nombre_archivo)
        imagen_base.save(nuevo_ruta_archivo)
        
        print(f"Imagen editada: {nuevo_nombre_archivo}")