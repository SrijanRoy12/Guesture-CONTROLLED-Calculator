# 🖐 Gesture Controlled Calculator

A **touchless calculator** powered by **hand gestures**, using **Python**, **OpenCV**, and **MediaPipe**.  
Control all your calculations with just your fingers — no keyboard or mouse needed!

---

## 🚀 Features

- ✋ Real-time **hand tracking** using MediaPipe  
- 🧠 **Freeze gesture detection** for precise key input  
- 🔊 **Sound feedback** on every button press  
- 🔋 **Battery percentage** display  
- ⏱️ Live **system time** display  
- ✅ Smooth UI with responsive visual feedback  
- 🔐 Completely touch-free & fun to use!

---

## 🛠 Tech Stack

- **Python 3.x**
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- `playsound` for sound feedback
- `psutil` for battery monitoring
- `datetime` for clock display

---

## 📦 Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/gesture-calculator.git
   cd gesture-calculator
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe psutil playsound
Run the app

bash
Copy
Edit
python app.py
📁 Project Structure
csharp
Copy
Edit
gesture-calculator/
│
├── app.py                  # Main app file
├── gesture_calculator.py   # HandDetector class (MediaPipe logic)
├── utils.py                # UI drawing utilities
├── sound/                  # Keypress sound effects
│   └── mixkit-modern-technology-select-3124.wav
└── README.md
🎯 Future Improvements
Scientific calculator mode (log, sin, etc.)

Voice feedback using text-to-speech

Dark/light theme toggle

Gesture-based backspace and history navigation

Save calculation history to file
