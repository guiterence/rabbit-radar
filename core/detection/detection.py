import torch
import cv2
from PIL import Image
import numpy as np

def load_model():
    """Carrega o modelo YOLO."""
    # Exemplo usando o modelo YOLOv5
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Ajuste para o modelo desejado
    return model

def detect_objects(model, image_path):
    """Detecta objetos em uma imagem."""
    img = Image.open(image_path)  # Carregar a imagem
    results = model(img)          # Fazer a detecção
    
    # Processar os resultados
    detected_objects = results.pandas().xyxy[0].to_dict(orient='records')
    return detected_objects

if __name__ == "__main__":
    model = load_model()
    image_path = "input_image.jpg"  # Exemplo: substitua pelo caminho da imagem que deseja analisar
    detections = detect_objects(model, image_path)
    print("Objetos detectados:", detections)
