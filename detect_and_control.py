import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time

# Serial setup (optional)
try:
    ser = serial.Serial('COM5', 115200)  # Replace 'COM3' with your ESP32 port
    time.sleep(2)
except:
    ser = None
    print("Serial not connected. Arm will only simulate.")

# Arm configuration (shorter lengths)
L1 = 60   # Shorter length for upper arm
L2 = 60   # Shorter length for forearm

def inverse_kinematics(x, y):
    D = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if np.abs(D) > 1:
        return None
    theta2 = np.arctan2(np.sqrt(1 - D**2), D)
    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    return np.degrees(theta1), np.degrees(theta2)

cap = cv2.VideoCapture(0)

fig, ax = plt.subplots()
ax.set_xlim(-L1-L2-20, L1+L2+20)
ax.set_ylim(-L1-L2-20, L1+L2+20)
arm_line, = ax.plot([], [], 'o-', lw=4)

# Starting at [0, 0] degrees (fully horizontal to the right)
target_pos = [L1 + L2, 0]

def update(frame):
    global target_pos
    ret, frame = cap.read()
    if not ret:
        return arm_line,
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        if area > 300:
            (x, y), radius = cv2.minEnclosingCircle(largest)
            center = (int(x), int(y))
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
            cv2.putText(frame, f"Tracking ({int(x)}, {int(y)})", (center[0]+10, center[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            # Map frame coordinates to arm space
            frame_center = (frame.shape[1]//2, frame.shape[0]//2)
            dx = center[0] - frame_center[0]
            dy = frame_center[1] - center[1]
            scale = 0.5  # Smaller scale factor for tighter arm movements
            target_pos = [dx * scale, dy * scale]

    # Show webcam feed with tracking
    cv2.imshow('Webcam Tracking', frame)
    if cv2.waitKey(1) == 27:
        plt.close()

    # Arm simulation
    angles = inverse_kinematics(target_pos[0], target_pos[1])
    if angles:
        theta1, theta2 = angles
        x1 = L1 * np.cos(np.radians(theta1))
        y1 = L1 * np.sin(np.radians(theta1))
        x2 = x1 + L2 * np.cos(np.radians(theta1 + theta2))
        y2 = y1 + L2 * np.sin(np.radians(theta1 + theta2))
        arm_line.set_data([0, x1, x2], [0, y1, y2])

        if ser:
            ser.write(f"{int(theta1)},{int(theta2)}\n".encode())
    else:
        arm_line.set_data([0, L1, L1+L2], [0, 0, 0])  # Fallback: fully horizontal

    return arm_line,

ani = animation.FuncAnimation(fig, update, interval=50)
plt.show()

cap.release()
cv2.destroyAllWindows()
if ser:
    ser.close()
