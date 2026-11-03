import cv2
import datetime
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    cv2.putText(frame, timestamp, (10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    current_time = time.time()


    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save face image
        filename = f"spy_{img_counter}_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
        img_counter += 1
        time.sleep(5)


    cv2.imshow('SpyCam (Press Q to Quit)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
