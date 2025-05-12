from unittest.mock import patch
import alert_module
import re

# Test 1: Low Soil Moisture Alert

def test_low_soil_moisture_alert():
    with patch("alert_module.get_sensor_data", return_value={"moisture": 20, "temperature": 28}):
        alert = alert_module.generate_alert(alert_module.get_sensor_data())
        assert "Low Soil Moisture" in alert
        assert re.match(r"ALERT-\d{4}: Low Soil Moisture - High at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", alert)

# Test 2: High Temperature Alert

def test_high_temperature_alert():
    with patch("alert_module.get_sensor_data", return_value={"moisture": 30, "temperature": 45}):
        alert = alert_module.generate_alert(alert_module.get_sensor_data())
        assert "High Temperature" in alert
        assert re.match(r"ALERT-\d{4}: High Temperature - Critical at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", alert)

# Test 3: No Alert Condition

def test_no_alert_condition():
    with patch("alert_module.get_sensor_data", return_value={"moisture": 35, "temperature": 25}):
        alert = alert_module.generate_alert(alert_module.get_sensor_data())
        assert alert == "No Alert"

# Test 4: Fluctuating Sensor Input

def test_fluctuating_sensor_input():
    readings = [
        {"moisture": 35, "temperature": 25},  # No Alert
        {"moisture": 20, "temperature": 25},  # Low Moisture
        {"moisture": 30, "temperature": 45},  # High Temperature
        {"moisture": 35, "temperature": 25}   # No Alert again
    ]
    for reading in readings:
        with patch("alert_module.get_sensor_data", return_value=reading):
            alert = alert_module.generate_alert(alert_module.get_sensor_data())
            assert isinstance(alert, str)

# Test 5: Sensor Failure Case

def test_sensor_failure_case():
    with patch("alert_module.get_sensor_data", return_value={"moisture": None, "temperature": 30}):
        alert = alert_module.generate_alert(alert_module.get_sensor_data())
        assert alert == "No Alert"  # Assuming no alert for invalid data
