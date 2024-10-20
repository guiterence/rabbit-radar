import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message):
    """Envia uma mensagem para o Slack usando um webhook."""
    if not SLACK_WEBHOOK_URL:
        print("Slack Webhook URL não configurada.")
        return

    payload = {"text": message}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Mensagem enviada para o Slack com sucesso!")
    except requests.exceptions.HTTPError as err:
        print(f"Erro ao enviar mensagem para o Slack: {err}")

def notify_security(detected_objects):
    """Envia uma notificação para a equipe de segurança sobre os objetos detectados."""
    message = f"Alerta de segurança: Objetos detectados - {detected_objects}"
    send_slack_message(message)

if __name__ == "__main__":
    # Exemplo de uso
    detected_objects = [
        {"name": "pistol", "confidence": 0.85, "x": 100, "y": 200},
        {"name": "knife", "confidence": 0.92, "x": 150, "y": 250},
    ]
    notify_security(detected_objects)
