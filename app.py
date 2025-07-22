import cv2
import time
import threading
import psutil
from datetime import datetime
from playsound import playsound
from gesture_calculator import HandDetector
from utils import draw_buttons

# SOUND: Play in background thread
def play_sound():
    threading.Thread(
        target=playsound,
        args=(r"D:\\gesture-calculator\\sound\\mixkit-modern-technology-select-3124.wav",),
        daemon=True
    ).start()

# Define buttons and labels
buttons = []
labels = ["7", "8", "9", "*",
          "4", "5", "6", "-",
          "1", "2", "3", "+",
          "C", "0", "=", "/",
          "(", ")", ".", "**"]

for i in range(5):  # 5 rows now (4x5)
    for j in range(4):
        index = i * 4 + j
        if index < len(labels):
            label = labels[index]
            x = j * 100 + 50
            y = i * 100 + 100
            buttons.append((x, y, 80, 80, label))

# App state
equation = ""
history = ""

# Detector + Camera
detector = HandDetector()
cap = cv2.VideoCapture(0)

# Freeze detection
prev_x, prev_y = 0, 0
still_start_time = None
still_threshold = 10
still_required_duration = 1  # second

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img, landmarks = detector.find_hand(img)

    hovered_button = None

    if landmarks:
        x, y = landmarks[8]  # Index fingertip
        movement = ((x - prev_x)**2 + (y - prev_y)**2)**0.5
        prev_x, prev_y = x, y

        cv2.circle(img, (x, y), 8, (255, 0, 255), -1)

        for button in buttons:
            bx, by, bw, bh, val = button
            if bx < x < bx + bw and by < y < by + bh:
                hovered_button = button
                cv2.rectangle(img, (bx, by), (bx + bw, by + bh), (0, 255, 0), 3)

                # Detect stillness
                if movement < still_threshold:
                    if still_start_time is None:
                        still_start_time = time.time()
                    elif time.time() - still_start_time >= still_required_duration:
                        play_sound()
                        if val == "C":
                            equation = ""
                            history = ""
                        elif val == "=":
                            try:
                                result = str(eval(equation))
                                history = equation + " = " + result
                                equation = result
                            except Exception:
                                history = "Error"
                                equation = ""
                        else:
                            equation += val
                        still_start_time = None
                else:
                    still_start_time = None
                break
        else:
            still_start_time = None
    else:
        still_start_time = None

    # Battery and Time
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else 0
    current_time = datetime.now().strftime("%H:%M:%S")
    status_text = f"Battery: {battery_percent}%   Time: {current_time}"
    cv2.putText(img, status_text, (50, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # UI Draw
    img = draw_buttons(img, buttons, hovered_button)
    cv2.rectangle(img, (50, 20), (450, 80), (255, 255, 255), -1)
    cv2.putText(img, equation, (60, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

    if history:
        cv2.putText(img, history, (60, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 1)

    cv2.imshow("🖐 Gesture Calculator", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
