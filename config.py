import os

class Config:
    # Configurações gerais
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    # Configurações do serviço de detecção
    YOLO_DATABASE_URL = os.getenv("YOLO_DATABASE_URL", "http://yolo-database:5001")
    CAMERA_SERVICE_URL = os.getenv("CAMERA_SERVICE_URL", "http://camera-service:5002")

    # Configurações de Notificação
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://discord.com/api/webhooks/1297745494558117899/3Z7z5CnzzxOgjceYTlf60tR3bhHTwgWa0OLG-O2G8RXFaRBTwBhueCzpPwxAsWzgi-SV")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
