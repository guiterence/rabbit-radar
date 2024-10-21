from flask import Blueprint, request, jsonify
from services.detection import detect_objects

detection_blueprint = Blueprint('detection', __name__)

@detection_blueprint.route('/detect', methods=['POST'])
def detect():
    image = request.files['image'].read()
    results = detect_objects(image)
    return jsonify(results)
