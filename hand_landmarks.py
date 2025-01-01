#Computer Vision Applications based on MediaPipe Library by Google
import cv2
import mediapipe as mp

#https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/holistic.md
mp_holistic = mp.solutions.holistic

holistic_model = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

#https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
k = 5
while(k!= -1):
    camera = cv2.VideoCapture(k)
    ret,frame = camera.read()
    if ret == 1:
        break
    else:
        k = k - 1
        continue
if(k == -1):
    print("No camera found in the system")

while camera.isOpened() == True:
    ret,frame = camera.read()
    if ret == 0:
        print("Failure: Camera Interruption")
        break
    
    x = 1200
    y = 900

    frame = cv2.resize(frame, (x, y))
    results = holistic_model.process(frame)
    frame.flags.writeable = True

    mp_drawing.draw_landmarks(
	frame,
    results.right_hand_landmarks,
	mp_holistic.HAND_CONNECTIONS)

    mp_drawing.draw_landmarks(
	frame,
    results.left_hand_landmarks,
	mp_holistic.HAND_CONNECTIONS)

    flip_frame = cv2.flip(frame,1)

    cv2.putText(
        flip_frame, "Press the Escape key to exit", (int(x * 0.68), int(y * 0.96)), 
        cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA
    )
    cv2.imshow("Hand Landmarks Detection", flip_frame)

    if cv2.waitKey(5) & 0xFF == 27:
        camera.release()
        cv2.destroyAllWindows()
        break