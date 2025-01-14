from flask import Flask
from api.routes.detection import detection_blueprint
from api.routes.notifications import notifications_blueprint
from api.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Registrando as rotas da API
app.register_blueprint(detection_blueprint, url_prefix='/detection')
app.register_blueprint(notifications_blueprint, url_prefix='/notifications')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
