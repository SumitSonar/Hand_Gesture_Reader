# Hand Gesture Controlled Video Effects
## Overview
This project uses OpenCV and MediaPipe to apply real-time video effects based on hand gestures detected via a webcam. Different hand gestures (number of fingers raised) trigger different visual effects such as grayscale, zoom, sharpen, and reset.

## Features
Real-time hand tracking using MediaPipe

Gesture-based effect selection

Live video processing with OpenCV

✅ Five different effects:

1. One Finger → Grayscale

2. Two Fingers → Zoom In

3. Three Fingers → Zoom Out

4. Four Fingers → Sharpen

5. Five Fingers → Reset

## Requirements
Make sure you have Python installed along with the following dependencies:

```
pip install opencv-python mediapipe numpy
```
## Usage
Run the script:

```
python hand_gesture_effects.py
```
Ensure your webcam is connected.

Use hand gestures to control the effects.

Press 'q' to exit the program.

## How It Works
Captures video from the webcam.

Detects hand landmarks using MediaPipe Hands.

Counts the number of raised fingers.

Maps the count to a predefined effect.

Applies the effect to the video feed.

Displays the modified video with an overlay showing the active effect.

## Customization
Modify the effect_map dictionary in the script to change gesture mappings.

Add new effects by extending the apply_effect() function.

## Troubleshooting
If the camera doesn’t start, check if another application is using it.

Ensure you have the correct permissions for camera access.

If gesture detection is inconsistent, improve lighting conditions.

## License
This project is open-source and can be freely modified and distributed.
