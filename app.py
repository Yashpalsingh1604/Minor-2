# app.py
from controller import decide_traffic_signal

videos = {
    "north": "c:/Users/acer/OneDrive/Desktop/Trafficesystem/Trafficesystem/videos/north.mp4",
    "south": "c:/Users/acer/OneDrive/Desktop/Trafficesystem/Trafficesystem/videos/south.mp4",
    "east": "c:/Users/acer/OneDrive/Desktop/Trafficesystem/Trafficesystem/videos/east.mp4",
    "west": "c:/Users/acer/OneDrive/Desktop/Trafficesystem/Trafficesystem/videos/west.mp4"
}

direction, time_sec = decide_traffic_signal(videos)
print(f"\n✅ Signal opened for {direction.upper()} direction for {time_sec} seconds.")
