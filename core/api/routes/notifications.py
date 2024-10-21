from flask import Blueprint, request
from services.notifications import send_alert

notifications_blueprint = Blueprint('notifications', __name__)

@notifications_blueprint.route('/notify', methods=['POST'])
def notify():
    data = request.json
    response = send_alert(data)
    return response, 200
