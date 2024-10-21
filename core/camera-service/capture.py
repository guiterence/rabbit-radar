import cv2
import requests

YOLO_API_URL = "http://yolo-database:5001/predict"

def capture_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame.")
            break

        _, img_encoded = cv2.imencode('.jpg', frame)
        files = {'file': ('frame.jpg', img_encoded.tobytes(), 'image/jpeg')}
        try:
            response = requests.post(YOLO_API_URL, files=files)
            print(f"Detecções: {response.json()}")
        except Exception as e:
            print(f"Erro ao enviar imagem para a detecção: {e}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_frames()
