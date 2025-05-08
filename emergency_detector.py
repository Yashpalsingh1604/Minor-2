import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load only once
model = load_model("C:\\Users\\acer\\OneDrive\\Desktop\\Trafficesystem\\Trafficesystem\\emergency_vehicle_detector.h5")
target_size = (128, 128)

def detect_emergency_vehicle(video_path):
    cap = cv2.VideoCapture(video_path)
    emergency_detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, target_size)
        input_frame = resized_frame / 255.0
        input_frame = np.expand_dims(input_frame, axis=0)

        prediction = model.predict(input_frame, verbose=0)
        if prediction[0] > 0.5:
            emergency_detected = True
            break

    cap.release()
    return emergency_detected
