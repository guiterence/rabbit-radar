import face_recognition
import cv2
import numpy as np
import os

def detect_faces(image):
    """
    Detecta rostos em uma imagem e retorna as localizações dos rostos.
    
    Args:
        image (np.ndarray): A imagem na qual os rostos serão detectados.
        
    Returns:
        list: Lista de coordenadas dos rostos detectados na imagem.
    """
    # Carrega a imagem em um array numpy
    image_np = np.array(image)
    
    # Detecta os rostos na imagem
    face_locations = face_recognition.face_locations(image_np)
    return face_locations

def save_face_images(image, face_locations, output_dir="detected_faces"):
    """
    Salva os rostos detectados em arquivos de imagem.
    
    Args:
        image (np.ndarray): A imagem original.
        face_locations (list): Lista de coordenadas dos rostos.
        output_dir (str): Diretório onde as imagens dos rostos serão salvas.
        
    Returns:
        list: Lista dos caminhos dos arquivos de rosto salvos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    saved_faces = []
    for i, (top, right, bottom, left) in enumerate(face_locations):
        face_image = image[top:bottom, left:right]
        face_image_path = os.path.join(output_dir, f"face_{i}.jpg")
        cv2.imwrite(face_image_path, face_image)
        saved_faces.append(face_image_path)
    
    return saved_faces
