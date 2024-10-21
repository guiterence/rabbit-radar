class DetectionModel:
    def __init__(self, object_type, confidence, timestamp):
        self.object_type = object_type
        self.confidence = confidence
        self.timestamp = timestamp
