import cv2
import mediapipe as mp

def initialize_camera():
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
    
    return camera


def initialize_holistic():
    #https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/holistic.md
    return mp.solutions.holistic, mp.solutions.holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5), mp.solutions.drawing_utils


def display_camera(name, frame, x, y):
    flip_frame = cv2.flip(frame,1)
    cv2.putText(
        flip_frame, "Press the Escape key to exit", (int(x * 0.68), int(y * 0.96)), 
        cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow(f"{name} Landmark Detection", flip_frame)
    return None

#Displaying Coordinates Idea:
#https://medium.com/geekculture/computer-vision-using-mediapipe-c0933b743cf5
def landmark_position(name, landmark_part, x, y):
    i = 0
    for landmark in landmark_part.landmark:
            coordinate_x, coordinate_y = int(landmark.x * x), int(landmark.y * y)
            print(f"{name} Landmark {i}: (x: {coordinate_x}, y: {coordinate_y})")
            i = i + 1

def process_camera(camera):
    if cv2.waitKey(5) & 0xFF == 27:
        camera.release()
        cv2.destroyAllWindows()
        return 0
    return 1
