# alert_module.py

from datetime import datetime

class Alert:
    def __init__(self, alert_type, severity):
        self.alert_type = alert_type
        self.severity = severity
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.alert_id = "ALERT-5678"

    def display_alert(self):
        return f"{self.alert_id}: {self.alert_type} - {self.severity} at {self.timestamp}"

def get_sensor_data():
    return {"moisture": 18, "temperature": 45}

def generate_alert(data):
    if data["moisture"] is not None and data["moisture"] < 30:
        return Alert("Low Soil Moisture", "High").display_alert()
    elif data["temperature"] is not None and data["temperature"] > 40:
        return Alert("High Temperature", "Critical").display_alert()
    return "No Alert"