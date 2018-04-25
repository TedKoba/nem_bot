import datetime

class manage_time:
    def __init__(self):
        self.current_time = datetime.datetime.utcnow()
    def get_minutes(self):
        return self.current_time.minute

    def get_hour(self):
        return self.current_time.hour
