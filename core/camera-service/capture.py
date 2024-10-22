import cv2
import requests
import os
from config import Config

YOLO_ENDPOINT = Config.YOLO_DATABASE_URL

def capture_and_send_frames():
    cap = cv2.VideoCapture(0)  # Ajuste conforme a câmera do sistema

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        _, img_encoded = cv2.imencode('.jpg', frame)
        response = requests.post(YOLO_ENDPOINT, files={'image': img_encoded.tobytes()})
        
        if response.status_code == 200:
            result = response.json()
            # Analisar a resposta e verificar se há objetos perigosos detectados.
            if result.get("dangerous_object_detected"):
                send_alert("Objeto perigoso detectado!")

    cap.release()
    cv2.destroyAllWindows()

def send_alert(message):
    webhook_url = Config.WEBHOOK_URL
    payload = {"content": message}
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Erro ao enviar mensagem para o webhook: {err}")

if __name__ == "__main__":
    capture_and_send_frames()

