from flask import Blueprint, request, jsonify
from services.detection import detect_objects

detection_blueprint = Blueprint('detection', __name__)

@detection_blueprint.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if not image:
        return jsonify({"error": "No image provided"}), 400
    
    result = detect_objects(image)
    return jsonify(result)
