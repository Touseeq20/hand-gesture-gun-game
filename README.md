# ✋ Hand Gesture Gun Control Game

An interactive computer vision game where you control a virtual crosshair and shoot targets using hand gestures.

## 🎯 Features

- **Gesture Control**: Use your index finger tip to move the crosshair in real-time.
- **Hand Tracking**: Powered by MediaPipe for smooth, high-precision hand landmark detection.
- **Dynamic Targets**: Multiple "planes" (targets) move across the screen with varying speeds.
- **Lock-On System**: Virtual "FIRE!" mechanism that triggers when the crosshair is centered on a target.
- **Camera Calibration**: Automatically adjusts to your screen resolution and camera feed.

## 📋 Requirements

- Python 3.8+
- OpenCV
- MediaPipe
- NumPy

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Touseeq20/hand-gesture-gun-game.git
cd hand-gesture-gun-game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the game:
```bash
python gesture_control_game.py
```

2. Controls:
   - **Move Hand**: Point your index finger at the camera to move the crosshair.
   - **Shoot**: Hover the crosshair over the blue targets to "FIRE!".
   - **Quit**: Press 'q' to exit.

## 🔧 How It Works

1. **Hand Tracking**:
   - MediaPipe Hands solution extracts 21 hand landmarks.
   - The coordinates of the INDEX_FINGER_TIP are mapped to the screen resolution.

2. **Game Mechanics**:
   - The crosshair (green circle) follows your finger.
   - Blue circles (planes) move from right to left at random speeds and heights.
   - Euclidean distance is calculated between the crosshair and each plane.
   - If distance < `LOCK_THRESHOLD`, a visual "FIRE!" feedback is triggered.

## 📝 Technical Details

- **Framework**: MediaPipe Hands (Static Image Mode: False, Max Hands: 1)
- **Visualization**: OpenCV Drawing Utilities
- **Target Logic**: Randomized list-based movement system.

## 📦 Dependencies

- opencv-python
- mediapipe
- numpy

## 👤 Author

**Touseeq Ahmed**
- GitHub: [@Touseeq20](https://github.com/Touseeq20)
