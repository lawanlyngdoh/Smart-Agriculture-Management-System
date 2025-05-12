import cProfile
import alert_module

def profile_alert_generation():
    # Simulate a realistic workload
    test_data = [
        {"moisture": 20, "temperature": 25},  # Low Moisture
        {"moisture": 35, "temperature": 25},  # No Alert
        {"moisture": 30, "temperature": 45},  # High Temperature
        {"moisture": 25, "temperature": 50},  # High Temperature
        {"moisture": 15, "temperature": 30},  # Low Moisture
    ]
    for data in test_data:
        print(alert_module.generate_alert(data))  # Ensure function is being called

if __name__ == "__main__":
    # Run and save the profiling data
    cProfile.run("profile_alert_generation()", "alert_profiling_results.prof")