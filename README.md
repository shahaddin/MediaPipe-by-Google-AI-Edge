# MediaPipe-by-Google-AI-Edge

The following code is the live implementation of Hand Landmarker and Pose Landmarker using the MediaPipe Library with a camera.

## 1. Hand Landmaker

The MediaPipe Hand Landmarker task lets you detect the landmarks of the hands in an image. You can use this task to locate key points of hands and render visual effects on them. This task operates on image data with a machine learning (ML) model as static data or a continuous stream and outputs hand landmarks in image coordinates, hand landmarks in world coordinates, and handedness(left/right hand) of multiple detected hands.

Configuration Options:
|  Option Name  |  Description  |  Value Range	| Default Value |
| ------------- | ------------- | ------------- | ------------- |
| min_hand_detection_confidence  | The minimum confidence score for the hand detection to be considered successful in palm detection model.  | 0.0 - 1.0  | 0.5  |
| min_tracking_confidence  | The minimum confidence score for the hand tracking to be considered successful. This is the bounding box IoU threshold between hands in the current frame and the last frame. In Video mode and Stream mode of Hand Landmarker, if the tracking fails, Hand Landmarker triggers hand detection. Otherwise, it skips the hand detection.	  | 0.0 - 1.0  | 0.5  |


The hand landmark model bundle detects the keypoint localization of 21 hand-knuckle coordinates within the detected hand regions. The model was trained on approximately 30K real-world images, as well as several rendered synthetic hand models imposed over various backgrounds.
![image](https://github.com/user-attachments/assets/428856cb-239f-45a9-b23f-f66ba8d2c197)
0 - wrist  
1 - thumb_cmc  
2 - thumb_mcp  
3 - thumb_ip  
4 - thumb_tip  
5 - index_finger_mcp  
6 - index_finger_pip  
7 - index_finger_dip  
8 - index_finger_tip  
9 - middle_finger_mcp  
10 - middle_finger_pip  
11 - middle_finger_dip  
12 - middle_finger_tip  
13 - ring_finger_mcp  
14 - ring_finger_pip  
15 - ring_finger_dip  
16 - ring_finger_tip  
17 - pinky_mcp  
18 - pinky_pip  
19 - pinky_dip  
20 - pinky_tip  
  
## 2. Pose Landmaker

The MediaPipe Pose Landmarker task lets you detect landmarks of human bodies in an image or video. You can use this task to identify key body locations, analyze posture, and categorize movements. This task uses machine learning (ML) models that work with single images or video. The task outputs body pose landmarks in image coordinates and in 3-dimensional world coordinates.

Configuration Options:
|  Option Name  |  Description  |  Value Range	| Default Value |
| ------------- | ------------- | ------------- | ------------- |
| min_pose_detection_confidence	  | The minimum confidence score for the pose detection to be considered successful.	  | Float [0.0,1.0]  | 0.5  |
| min_tracking_confidence	  | The minimum confidence score for the pose tracking to be considered successful.	  | Float [0.0,1.0]  | 0.5  |


The pose landmarker model tracks 33 body landmark locations, representing the approximate location of the following body parts:
![image](https://github.com/user-attachments/assets/564f55b7-3894-43e4-a533-68bcef39ae68)
0 - nose  
1 - left eye (inner)  
2 - left eye  
3 - left eye (outer)  
4 - right eye (inner)  
5 - right eye  
6 - right eye (outer)  
7 - left ear  
8 - right ear  
9 - mouth (left)  
10 - mouth (right)  
11 - left shoulder  
12 - right shoulder  
13 - left elbow  
14 - right elbow  
15 - left wrist  
16 - right wrist  
17 - left pinky  
18 - right pinky  
19 - left index  
20 - right index  
21 - left thumb  
22 - right thumb  
23 - left hip  
24 - right hip  
25 - left knee  
26 - right knee  
27 - left ankle  
28 - right ankle  
29 - left heel  
30 - right heel  
31 - left foot index  
32 - right foot index  

