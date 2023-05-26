import cv2
import os

def preprocess_images(input_folder, output_folder, target_resolution):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener la lista de imágenes en la carpeta de entrada
    image_files = os.listdir(input_folder)

    for image_file in image_files:
        # Cargar la imagen
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            # Si la imagen no se puede cargar, pasar a la siguiente
            continue

        # Eliminar imágenes defectuosas (puedes agregar tus propios criterios de filtrado aquí)

        # Reescalar la imagen
        image = cv2.resize(image, target_resolution)

        # Verificar el formato de canales y convertir a RGB si es necesario
        if image.shape[2] != 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Guardar la imagen preprocesada en la carpeta de salida
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, image)

    print("Preprocesamiento de imágenes completado.")

# Ejemplo de uso
input_folder = "C:\MI-CARRERA\Semestre 6\SIS421_\FotosDestino"
output_folder = "C:\MI-CARRERA\Semestre 6\SIS421_\FotosRGB"
target_resolution = (800, 600)

preprocess_images(input_folder, output_folder, target_resolution)
