# controller.py
from emergency_detector import detect_emergency_vehicle
from vehicle_counter import count_vehicles

def decide_traffic_signal(videos):
    durations = {}
    emergency_detected = {}

    # Step 1: Check for emergency vehicle and count traffic for each direction
    for direction, path in videos.items():
        emergency_detected[direction] = detect_emergency_vehicle(path)
        durations[direction] = count_vehicles(path)

    print("\n🧠 Traffic Decision Logic Running...")
    
    # Step 2: Emergency priority
    for direction, detected in emergency_detected.items():
        if detected:
            print(f"\n🚨 Emergency vehicle detected in {direction} direction.")
            return direction, durations[direction] + 15  # +15 sec priority

    # Step 3: Choose direction with max traffic
    selected_direction = max(durations, key=durations.get)
    base_duration = durations[selected_direction]

    # Adjust duration based on traffic
    if base_duration >= 15:
        signal_time = 60
    elif base_duration >= 10:
        signal_time = 45
    elif base_duration >= 5:
        signal_time = 30
    else:
        signal_time = 15

    print(f"\n🚦 Opening signal for {selected_direction} ({base_duration} vehicles) for {signal_time} seconds.")
    return selected_direction, signal_time
