# app.py

from controller import decide_traffic_signal

videos = {
    "north": "videos/north.mp4",
    "south": "videos/south.mp4",
    "east": "videos/east.mp4",
    "west": "videos/west.mp4"
}

signal_plan = decide_traffic_signal(videos)

print("\n✅ Traffic light schedule:")
for direction, seconds in signal_plan.items():
    print(f"Open signal for {direction.upper()} direction for {seconds} seconds.")
