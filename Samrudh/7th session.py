# open CV

import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# For reading an image
# image = cv2.imread("people.jpg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Cute CAT", gray_image)



# read a video
# cap = cv2.VideoCapture("people_pass.mp4")

# using webcam
cap = cv2.VideoCapture(0)

# detect the face

while True:
    ret, frame = cap.read()
    if not ret:
        break


    video_data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(video_data, scaleFactor=1.1, minNeighbors=5)
    for (x,y, w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Face Detection: frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()



# For creating shapes
# cv2.rectangle(image, (50,50), (300,100), (0,0,255),5)
#
# # To put a text on an image
# cv2.putText(image, "MY Cat", (60,40), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0,0), 2)

# cv2.imshow("Cute CAT", image)
# cv2.waitKey(0)