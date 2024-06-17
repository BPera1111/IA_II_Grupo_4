import subprocess
try:
    import tensorflow as tf
except ImportError as err:
    subprocess.check_call(['pip', 'install', 'tensorflow'])
    subprocess.check_call(['pip', 'install', 'Pillow'])
    import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os
import random

# Rutas de las carpetas
source_dir = "images"

train_dir = source_dir + "/train/"
test_dir = source_dir + "/test/"

# Clases (nombres de las subcarpetas)
classes = ["up", "down", "right"]

# Crea los directorios de entrenamiento y prueba si no existen
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Crea los directorios de entrenamiento y prueba si no existen
os.makedirs(train_dir + classes[0], exist_ok=True)
os.makedirs(train_dir + classes[1], exist_ok=True)
os.makedirs(train_dir + classes[2], exist_ok=True)
os.makedirs(test_dir + classes[0], exist_ok=True)
os.makedirs(test_dir + classes[1], exist_ok=True)
os.makedirs(test_dir + classes[2], exist_ok=True)

# Proporción de imágenes para entrenamiento y prueba
train_ratio = 0.8

# Parámetros para el modelo
batch_size = 32
image_size = (400, 600)
input_shape = image_size + (1,)  # Tamaño de la imagen con un solo canal para escala de grises

# Función para cargar imágenes y convertirlas a escala de grises
def load_and_preprocess_image(file_path, target_size):
    img = load_img(file_path, color_mode='grayscale', target_size=target_size)
    img_array = img_to_array(img)
    return img_array / 255.0  # Normaliza los valores de píxeles entre 0 y 1

# Iterar sobre las subcarpetas
for class_name in classes:
    # Ruta de la subcarpeta de origen
    source_class_dir = os.path.join(source_dir, class_name)
    
    # Obtener la lista de imágenes en la subcarpeta de origen
    images = os.listdir(source_class_dir)
    
    # Mezclar aleatoriamente las imágenes
    random.shuffle(images)
    
    # Calcular el número de imágenes para entrenamiento
    num_train_images = int(len(images) * train_ratio)
    
    # Iterar sobre las imágenes para entrenamiento
    for img_name in images[:num_train_images]:
        # Ruta de la imagen de origen
        src_img_path = os.path.join(source_class_dir, img_name)
        # Ruta de destino para la imagen de entrenamiento
        dest_train_path = os.path.join(train_dir + class_name, f"{img_name}")
        # Mover la imagen a la carpeta de entrenamiento y renombrarla
        img_array = load_and_preprocess_image(src_img_path, image_size)
        tf.keras.preprocessing.image.save_img(dest_train_path, img_array)
    
    # Iterar sobre las imágenes para prueba
    for img_name in images[num_train_images:]:
        # Ruta de la imagen de origen
        src_img_path = os.path.join(source_class_dir, img_name)
        # Ruta de destino para la imagen de prueba
        dest_test_path = os.path.join(test_dir + class_name, f"{img_name}")
        # Mover la imagen a la carpeta de prueba y renombrarla
        img_array = load_and_preprocess_image(src_img_path, image_size)
        tf.keras.preprocessing.image.save_img(dest_test_path, img_array)#dest_train_path

