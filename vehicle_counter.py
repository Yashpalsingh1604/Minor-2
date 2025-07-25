import supervision as sv
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8x.pt")
CLASS_NAMES_DICT = model.model.names
SELECTED_CLASSES = ['car', 'motorcycle', 'truck']
SELECTED_CLASS_IDS = [
    {v: k for k, v in CLASS_NAMES_DICT.items()}[cls] for cls in SELECTED_CLASSES
]

def count_vehicles_all_directions(video_paths):
    """
    Counts vehicles in all four directions (north, east, south, west).

    Args:
        video_paths (dict): Dictionary with direction as key and video path as value.
            Example: {'north': 'north.mp4', 'south': 'south.mp4', ...}

    Returns:
        dict: Vehicle count per class for each direction.
    """
    direction_counts = {}

    for direction, path in video_paths.items():
        generator = sv.get_video_frames_generator(path)
        byte_tracker = sv.ByteTrack(
            track_activation_threshold=0.25,
            lost_track_buffer=30,
            minimum_matching_threshold=0.8,
            frame_rate=30,
            minimum_consecutive_frames=3
        )

        counted_ids = set()
        vehicle_counts = {cls: 0 for cls in SELECTED_CLASSES}

        for frame in generator:
            results = model(frame, verbose=False)[0]
            detections = sv.Detections.from_ultralytics(results)
            detections = detections[np.isin(detections.class_id, SELECTED_CLASS_IDS)]
            detections = byte_tracker.update_with_detections(detections)

            for class_id, tracker_id in zip(detections.class_id, detections.tracker_id):
                if tracker_id not in counted_ids:
                    counted_ids.add(tracker_id)
                    cls_name = CLASS_NAMES_DICT[class_id]
                    if cls_name in vehicle_counts:
                        vehicle_counts[cls_name] += 1

        direction_counts[direction] = vehicle_counts

    return direction_counts
