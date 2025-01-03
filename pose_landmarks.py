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

    if results.pose_landmarks != 0:
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        
        landmark_part = results.pose_landmarks
        mediapipe_init.landmark_position("Pose", landmark_part, x, y)
    
    # if results.face_landmarks != 0:
    #     mp_drawing.draw_landmarks(
    #     frame, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)

    #     landmark_part = results.pose_landmarks
    #     mediapipe_init.landmark_position("Face", landmark_part, x, y)
    #mediapipe_init.display_camera("Pose and Face", frame, x, y)

    mediapipe_init.display_camera("Pose", frame, x, y)

    if(mediapipe_init.process_camera(camera) == 0):
        break
    