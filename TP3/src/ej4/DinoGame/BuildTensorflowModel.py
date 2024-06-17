import subprocess
try:
    import tensorflow as tf
except ImportError as err:
    subprocess.check_call(['pip', 'install', 'tensorflow'])
    subprocess.check_call(['pip', 'install', 'Pillow'])
    import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


import os
import random
import matplotlib.pyplot as plt

# Rutas de las carpetas
source_dir = "images"

train_dir = source_dir + "/train/"
test_dir = source_dir + "/test/"

# Clases (nombres de las subcarpetas)
classes = ["0-up", "1-down", "2-right"]

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
image_size = (200, 200)
input_shape = image_size + (1,)  # Tamaño de la imagen con un solo canal para escala de grises

# Función para cargar imágenes y convertirlas a escala de grises
def load_and_preprocess_image(file_path, target_size):
    img = load_img(file_path, color_mode='grayscale', target_size=target_size)
    img_array = img_to_array(img)
    return img_array #/ 255.0  # Normaliza los valores de píxeles entre 0 y 1

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
        tf.keras.preprocessing.image.save_img(dest_test_path, img_array)

# Crear generadores de datos
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',
    color_mode='grayscale',)  # Se especifica el modo de color escala de grises

validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
    test_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',
    color_mode='grayscale')  # Se especifica el modo de color escala de grises

# ========================== Construir el modelo ==========================================
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(len(classes), activation='softmax')
])
# ==========================================================================================


# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss',min_delta=0.001, patience=3, 
                               restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model.h5.keras', save_best_only=True, 
                                   monitor='val_loss')

history = model.fit(
    train_generator,
    #steps_per_epoch=train_generator.samples // BATCH_SIZE,
    validation_data=validation_generator,
    #validation_steps=validation_generator.samples // BATCH_SIZE,
    epochs=20,
    callbacks=[early_stopping, model_checkpoint]
)

loss, accuracy = model.evaluate(validation_generator)
print(f'Loss: {loss}, Accuracy: {accuracy}')

model.save('tensorflow_nn.h5')

#Los modelos eran demasiado pesados para github