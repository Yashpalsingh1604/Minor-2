# controller.py

from emergency_detector import detect_emergency_vehicle
from vehicle_counter import count_vehicles_all_directions
from vehicle_timer import calculate_signal_time

def decide_traffic_signal(videos):
    print("\n🧠 Running Traffic Signal Decision Logic...")

    # Step 1: Get vehicle counts and emergency status for all directions
    vehicle_counts = count_vehicles_all_directions(videos)
    emergency_status = {dir: detect_emergency_vehicle(path) for dir, path in videos.items()}

    signal_plan = {}

    # Step 2: Compute base time for each direction
    for direction in ['north', 'east', 'south', 'west']:
        counts = vehicle_counts.get(direction, {})
        base_time = calculate_signal_time(counts)

        if emergency_status.get(direction):
            base_time += 15
            print(f"🚨 Emergency vehicle detected in {direction.upper()}! Giving extra priority.")

        signal_plan[direction] = base_time

    # Step 3: Sort directions clockwise starting from emergency or max traffic
    clockwise_order = ['north', 'east', 'south', 'west']

    # Prioritize emergency direction
    start_dir = next((d for d in clockwise_order if emergency_status.get(d)), None)

    if not start_dir:
        # Else pick the one with max time
        start_dir = max(signal_plan, key=signal_plan.get)

    start_idx = clockwise_order.index(start_dir)
    ordered_dirs = clockwise_order[start_idx:] + clockwise_order[:start_idx]

    print("\n🛑 Final Signal Timings:")
    for dir in ordered_dirs:
        print(f"➡ {dir.upper()}: {signal_plan[dir]} seconds")

    return signal_plan  # full plan for all 4 directions
