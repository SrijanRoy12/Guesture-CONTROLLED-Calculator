import cv2

def draw_buttons(img, button_list, hovered=None):
    for button in button_list:
        x, y, w, h, text = button
        color = (200, 200, 200) if button != hovered else (100, 255, 100)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 50), 2)
        cv2.putText(img, text, (x + 20, y + 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
    return img
