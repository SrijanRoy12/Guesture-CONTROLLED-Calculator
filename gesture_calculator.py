import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, detection_confidence=0.8):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=detection_confidence
        )
        self.draw = mp.solutions.drawing_utils

    def find_hand(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        landmarks = []
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                for lm in handLms.landmark:
                    h, w, _ = img.shape
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
        return img, landmarks
