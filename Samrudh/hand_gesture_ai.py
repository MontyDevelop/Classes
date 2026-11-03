import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open the default camera
cap = cv2.VideoCapture(0)

# Function to detect simple hand gestures
def detect_gesture(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
    fingers = []

    # Check which fingers are open
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Thumb (horizontal check)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.insert(0, 1)  # Thumb open
    else:
        fingers.insert(0, 0)  # Thumb closed

    total_fingers = fingers.count(1)

    # Define gestures
    if total_fingers == 0:
        return "Fist ✊"
    elif total_fingers == 5:
        return "Open Palm ✋"
    elif fingers == [0, 1, 1, 0, 0]:
        return "Victory ✌️"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up 👍"
    else:
        return f"{total_fingers} Fingers"

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame from camera. Exiting.")
        break

    # Flip the image horizontally for a selfie view
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture_name = "No Hand Detected"

    # Process landmarks
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            gesture_name = detect_gesture(handLms)

    # Display gesture
    cv2.putText(frame, gesture_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    # Show the output
    cv2.imshow("Hand Gesture Recognition", frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
