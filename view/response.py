import datetime

class CustomResponse:
    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.time = datetime.datetime.now().isoformat()
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "time": self.time,
            "data": self.data
        }
