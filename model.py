import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hand Detector
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to apply video effects
def apply_effect(frame, effect):
    h, w, _ = frame.shape
    
    if effect == "grayscale":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif effect == "sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(frame, -1, kernel)
    elif effect == "zoom_in":
        scale = 1.5
    elif effect == "zoom_out":
        scale = 0.5
    elif effect == "reset":
        return frame
    
    # Zoom Logic
    new_h, new_w = int(h * scale), int(w * scale)
    resized = cv2.resize(frame, (new_w, new_h))
    crop_h, crop_w = min(new_h, h), min(new_w, w)
    start_h, start_w = (new_h - crop_h) // 2, (new_w - crop_w) // 2
    return resized[start_h:start_h+h, start_w:start_w+w]

# Function to count raised fingers
def count_fingers(hand_landmarks):
    fingers = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    finger_up = 0

    # Thumb check (more reliable)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x:  # Thumb pointing up
        finger_up += 1

    # Check other fingers
    for tip in fingers:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_up += 1

    return finger_up

# Start capturing video
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Mirror the image
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        finger_count = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_count = count_fingers(hand_landmarks)

        # Mapping finger count to effects
        effect_map = {1: "grayscale", 2: "zoom_in", 3: "zoom_out", 4: "sharpen", 5: "reset"}
        effect = effect_map.get(finger_count, "reset")

        # Apply Effect
        output = apply_effect(frame, effect)
        if effect == "grayscale":
            output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

        # Display effect name
        cv2.putText(output, f"Effect: {effect}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Hand Gesture Control", output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()