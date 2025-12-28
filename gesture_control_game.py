import cv2
import mediapipe as mp
import numpy as np
import random

# =============== CONFIG ===============
SCREEN_W, SCREEN_H = 1280, 720
NUM_PLANES = 5
CROSSHAIR_RADIUS = 40
LOCK_THRESHOLD = CROSSHAIR_RADIUS  # same radius for lock

# =============== Init Hand Tracking ===============
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# =============== Init Dummy Planes ===============
planes = []
for _ in range(NUM_PLANES):
    x = random.randint(100, SCREEN_W - 100)
    y = random.randint(100, SCREEN_H // 2)
    speed = random.randint(2, 5)
    planes.append([x, y, speed])

# =============== Start Camera ===============
cap = cv2.VideoCapture(0)
cap.set(3, SCREEN_W)
cap.set(4, SCREEN_H)

# =============== Game Loop ===============
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # =============== Default crosshair at center ===============
    cx, cy = SCREEN_W // 2, SCREEN_H // 2

    # =============== If hand detected, update crosshair ===============
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Use wrist or index finger tip
            lm = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            cx = int(lm.x * SCREEN_W)
            cy = int(lm.y * SCREEN_H)

    # =============== Draw crosshair ===============
    cv2.circle(frame, (cx, cy), CROSSHAIR_RADIUS, (0, 255, 0), 2)
    cv2.line(frame, (cx - 20, cy), (cx + 20, cy), (0, 255, 0), 2)
    cv2.line(frame, (cx, cy - 20), (cx, cy + 20), (0, 255, 0), 2)

    # =============== Move & draw planes ===============
    for plane in planes:
        plane[0] -= plane[2]  # move left
        if plane[0] < -50:
            plane[0] = SCREEN_W + random.randint(50, 200)
            plane[1] = random.randint(50, SCREEN_H // 2)
            plane[2] = random.randint(2, 5)

        # Draw plane as a simple circle
        cv2.circle(frame, (plane[0], plane[1]), 20, (255, 0, 0), -1)

        # Check lock: if plane inside crosshair
        dist = np.linalg.norm(np.array([plane[0], plane[1]]) - np.array([cx, cy]))
        if dist < LOCK_THRESHOLD:
            cv2.putText(frame, "FIRE!", (plane[0] - 20, plane[1] - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # Here you can add bullet logic / sound etc.

    cv2.imshow("Hand Gesture Gun Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
