import mediapipe_init
import cv2
import mediapipe as mp

camera = mediapipe_init.initialize_camera()
mp_holistic, holistic_model, mp_drawing = mediapipe_init.initialize_holistic()

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

    mediapipe_init.display_camera(frame, x, y)

    if(mediapipe_init.process_camera(camera) == 0):
        break
