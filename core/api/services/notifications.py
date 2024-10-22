import requests
import os

def send_alert(message):
    """
    Envia uma mensagem de alerta para um canal configurado via webhook.
    
    Args:
        message (str): A mensagem a ser enviada no alerta.
        
    Returns:
        response (dict): Resposta da solicitação ao serviço de webhook.
    """
    webhook_url = os.getenv("WEBHOOK_URL", "https://discord.com/api/webhooks/1297745494558117899/3Z7z5CnzzxOgjceYTlf60tR3bhHTwgWa0OLG-O2G8RXFaRBTwBhueCzpPwxAsWzgi-SV")
    if not webhook_url:
        raise ValueError("Webhook URL not configured. Please set the WEBHOOK_URL environment variable.")

    payload = {
        "content": message
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Levanta um erro para códigos de resposta HTTP 4xx/5xx.
        return {"status": "success", "response": response.json()}
    except requests.exceptions.HTTPError as err:
        print(f"Erro ao enviar mensagem para o webhook: {err}")
        return {"status": "error", "error": str(err)}
