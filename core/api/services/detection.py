import cv2
import torch
from PIL import Image

def detect_objects(image):
    # Carregar o modelo YOLO
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    
    # Carregar a imagem
    img = Image.open(image)
    
    # Realizar a detecção
    results = model(img)
    
    # Processar os resultados para retornar apenas as informações relevantes
    detected_objects = results.pandas().xyxy[0].to_dict(orient='records')
    return detected_objects
