import cv2

def start_camera():
    cap = cv2.VideoCapture(0)  # Use 0 for default webcam

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break

        # Display the live feed
        cv2.imshow('Webcam Feed', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Test when running standalone
if __name__ == "__main__":
    start_camera()
