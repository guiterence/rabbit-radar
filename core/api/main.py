from flask import Flask, Response, render_template
from routes.detection import detection_blueprint
from routes.notifications import notifications_blueprint
import cv2
import requests
import json

app = Flask(__name__)

# URL da API do YOLO
YOLO_API_URL = 'http://yolo-database:5001/detect'

def generate_frames():
    # Acesse a câmera (0 é o índice da câmera padrão)
    cap = cv2.VideoCapture(0)
    
    # Verifique se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao acessar a câmera")
        exit()
    
    # Loop para capturar cada frame
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame")
            break

        # Codifique o frame em formato JPEG
        _, img_encoded = cv2.imencode('.jpg', frame)
        
        # Construa o payload para enviar à API
        payload = {'image': img_encoded.tobytes()}
        headers = {'Content-Type': 'application/octet-stream'}
        
        try:
            # Faça a requisição POST para a API do YOLO
            response = requests.post(YOLO_API_URL, data=payload, headers=headers)
            
            # Verifique a resposta
            if response.status_code == 200:
                result = json.loads(response.text)
                print(f"Resultado da Detecção: {result}")
                # Aqui você pode desenhar as detecções no frame usando os resultados retornados
                for detection in result.get('detections', []):
                    x, y, w, h = detection['x'], detection['y'], detection['width'], detection['height']
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                print(f"Erro na API: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Erro ao enviar o frame para a API: {str(e)}")
            break

        # Codifica o frame modificado para exibição em uma resposta HTTP
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Cria uma resposta do frame em formato JPEG para ser exibido no browser
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    # Libere a câmera
    cap.release()

# Rota para exibir o feed de vídeo
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Registrando as rotas da API
app.register_blueprint(detection_blueprint, url_prefix='/detection')
app.register_blueprint(notifications_blueprint, url_prefix='/notifications')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
