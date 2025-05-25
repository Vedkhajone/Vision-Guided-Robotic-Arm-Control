# 🤖 Vision-Guided Robotic Arm Control
This project combines **computer vision** and **inverse kinematics** to control a two-link **robotic arm** in real time using a webcam and ESP32! The Python program tracks a red object and maps its position to servo angles, visualizing the arm’s movement using matplotlib and controlling actual servos via serial communication.
## 📸 Demo
https://github.com/user-attachments/assets/f5a9a32b-f621-4b41-80bd-97ab4723f8dd

## 🚀 Features
- 🔴 Real-time object tracking with OpenCV
- 📐 Inverse kinematics for a 2-link robotic arm
- 📊 Live visualization with matplotlib
- 🔗 Serial communication to control ESP32-connected servos
- 🦾 Compact design for small-scale screens and environments
- 🎥 Supports mirrored webcam view correction



## 🛠️ Hardware Requirements
- 🧠 ESP32 board
- 🔩 2 Servo motors (e.g., SG90)
- 🔌 Jumper wires, breadboard
- 📷 Webcam (USB)
- 💻 Windows/Linux/Mac with Python installed

## 🧑‍💻 Software Requirements
- Python 
- OpenCV
- NumPy
- Matplotlib
- PySerial

## 📦 Installation & Setup
1️⃣ Clone this repository:
```bash
git clone https://github.com/yourusername/vision-guided-robotic-arm.git
cd vision-guided-robotic-arm
```
2️⃣ Install Python dependencies:
```bash
pip install opencv-python numpy matplotlib pyserial
```

3️⃣ Upload ESP32 code

Open code/esp32_servo_control.ino in Arduino IDE or PlatformIO.
Select your ESP32 board and upload the code.
The ESP32 reads angles sent over serial and controls servos.

4️⃣ Run Python script
```bash
python code/arm_control.py
```
## ⚙️ ESP32 Code Highlights
- esp32_servo_control.ino:
- Listens for serial data from Python.
- Parses angle commands (e.g., 30,45\n).
- Moves two servo motors to the specified angles.

## 📝 Wiring Diagram
🔗 Coming soon: detailed wiring diagram with ESP32 pinout and servo connections!

## 🔥 How It Works
- Step 1: Webcam captures frames.
- Step 2: OpenCV detects red-colored object (HSV mask).
- Step 3: Converts object position to arm coordinates.
- Step 4: Inverse kinematics computes joint angles.
- Step 5: Python visualizes arm movement and sends angles to ESP32.
- Step 6: ESP32 adjusts servos in real-time!

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Acknowledgments
Built with ❤️ by Vedhanshu Khajone

## 🚀 Ready to contribute?
Feel free to fork, star ⭐, and submit pull requests!

#🔗 Let's make robotics fun and easy! 🦾🚀
