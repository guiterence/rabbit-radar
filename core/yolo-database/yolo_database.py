from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np

app = Flask(__name__)

# Carregar o modelo YOLO ao iniciar o serviço
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada."}), 400

    file = request.files['file']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    # Fazer a detecção utilizando o modelo
    results = model(img)
    detections = results.pandas().xyxy[0].to_dict(orient='records')
    
    return jsonify({"detections": detections})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
