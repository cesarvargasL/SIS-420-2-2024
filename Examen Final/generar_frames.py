import cv2
from PIL import Image

# fps: frames por segundo- las images se guardan cada 8 frames
# with: el ancho de la imagen  resolución de la imagen
# height: el alto de la imagen
def extract_frames(video_path, output_folder, fps=8, width=230, height=210):
    # Cargar el video
    cap = cv2.VideoCapture(video_path)

    # Verificar si el video se ha abierto correctamente
    if not cap.isOpened():
        print("Error: No se puede abrir el video.")
        return

    # Obtener la tasa de frames por segundo del video
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(video_fps / fps)
    
    # Contador para el número de frames extraídos
    frame_count = 0
    saved_frame_count = 2964
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            # Redimensionar el frame con interpolación de alta calidad
            resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LANCZOS4)

            # Guardar el frame como imagen JPG con alta calidad
            # Importe, cambiar el nombre de la imagen para que no se repita o remplace la anterior ejem: cebolla1_{saved_frame_count:04d} por cada video
            
            output_path = f"{output_folder}/5_bolivianos_{saved_frame_count:04d}.jpg" # <--- Cambiar el nombre de la imagen
            image = Image.fromarray(cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB))
            image.save(output_path, "JPEG", quality=95)  # Ajustar la calidad a 95
            print(f"Guardado: {output_path}")
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print("Extracción de frames completada.")

# Parámetros de entrada
video_path = r"D:\CESAR\Universidad\7mo semestre\SIS 420\monedas\5_bolis.mp4" # Cambiar la ruta del video, a la que se desea extraer los frames
output_folder = r"D:\CESAR\Universidad\7mo semestre\SIS 420\repositorio\Examen Final\dataset\datos\5_bolivianos" # Cambiar la carpeta de salida, a la que se gurdarán los frames

# Llamar a la función para extraer los frames
extract_frames(video_path, output_folder)


