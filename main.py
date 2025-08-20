"""
Subway Surfers Hand Control - Fast Swipe Optimized
--------------------------------------------------
Controls:
- Swipe Left  → Move Left   (←)
- Swipe Right → Move Right  (→)
- Swipe Up    → Jump        (↑)
- Swipe Down  → Duck        (↓)
"""

import cv2
import mediapipe as mp
import pyautogui
import time

# ===== CONFIG =====
SWIPE_THRESHOLD = 30   # Lowered threshold for faster response
COOLDOWN = 0.15        # Smaller cooldown for quick moves

# ===== Mediapipe Setup =====
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

def press_key(key):
    """Simulate key press"""
    pyautogui.press(key)
    print(f"👉 Action: {key.upper()}")

def main():
    cap = cv2.VideoCapture(0)
    prev_x, prev_y = None, None
    last_time = 0

    print("🎮 Fast Swipe Subway Surfers Control")
    print("Swipe Left = ← | Swipe Right = → | Swipe Up = ↑ | Swipe Down = ↓")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Mirror view
        h, w, c = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]

            # Draw landmarks
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Use index fingertip only (landmark 8)
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)
            cv2.circle(frame, (x, y), 10, (0, 255, 0), cv2.FILLED)

            if prev_x is not None and prev_y is not None:
                dx = x - prev_x
                dy = y - prev_y
                now = time.time()

                if now - last_time > COOLDOWN:
                    # Detect horizontal swipe
                    if abs(dx) > abs(dy):
                        if dx > SWIPE_THRESHOLD:
                            press_key("right")
                            last_time = now
                        elif dx < -SWIPE_THRESHOLD:
                            press_key("left")
                            last_time = now
                    else:
                        if dy < -SWIPE_THRESHOLD:
                            press_key("up")
                            last_time = now
                        elif dy > SWIPE_THRESHOLD:
                            press_key("down")
                            last_time = now

            prev_x, prev_y = x, y

        cv2.imshow("Fast Swipe Control - Subway Surfers", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    main()
