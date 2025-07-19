# vehicle_timer.py

def calculate_signal_time(vehicle_counts):
    """
    Calculate signal time based on vehicle counts.

    Args:
        vehicle_counts (dict): A dictionary like {'car': x, 'motorcycle': y, 'truck': z}

    Returns:
        int: Calculated time in seconds (min 15, max 90)
    """
    cars = vehicle_counts.get('car', 0)
    motorcycles = vehicle_counts.get('motorcycle', 0)
    trucks = vehicle_counts.get('truck', 0)

    # Custom weighted formula
    time_seconds = (3 * cars) + (2 * motorcycles) + (5 * trucks)

    # Clamp the value between 15 and 90 seconds
    return max(15, min(time_seconds, 90))
