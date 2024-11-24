import os
import shutil
import random

def split_dataset_by_class(base_folder, train_folder, test_folder, test_ratio=0.2):
    # Crear carpetas de entrenamiento y prueba si no existen
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Obtener todas las clases (carpetas) en la carpeta base
    classes = [d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))]

    for cls in classes:
        cls_folder = os.path.join(base_folder, cls)
        images = [f for f in os.listdir(cls_folder) if f.endswith('.jpg')]

        # Barajar las imágenes
        random.shuffle(images)

        # Calcular el número de imágenes para el conjunto de prueba
        test_size = int(len(images) * test_ratio)

        # Crear carpetas de clase en train y test
        os.makedirs(os.path.join(train_folder, cls), exist_ok=True)
        os.makedirs(os.path.join(test_folder, cls), exist_ok=True)

        # Mover imágenes al conjunto de prueba
        for img in images[:test_size]:
            shutil.move(os.path.join(cls_folder, img), os.path.join(test_folder, cls, img))

        # Mover el resto de las imágenes al conjunto de entrenamiento
        for img in images[test_size:]:
            shutil.move(os.path.join(cls_folder, img), os.path.join(train_folder, cls, img))

    print(f"Imágenes movidas a {train_folder} y {test_folder}")

# Parámetros de entrada
base_folder = r"D:\CESAR\Universidad\7mo semestre\SIS 420\repositorio\Examen Final\dataset\datos"
train_folder = r"D:\CESAR\Universidad\7mo semestre\SIS 420\repositorio\Examen Final\dataset\train"
test_folder = r"D:\CESAR\Universidad\7mo semestre\SIS 420\repositorio\Examen Final\dataset\test"

# Llamar a la función para separar las imágenes
split_dataset_by_class(base_folder, train_folder, test_folder)