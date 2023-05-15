import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
def main():
    cap = cv2.VideoCapture(0)

    # Curl counter variables
    counter = 0 
    stage = None
    poseBool = False
    poseString = ''
    leftHorizontal = False
    rightHorizontal = False
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                shoulderR = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbowR = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wristR = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                
                # Calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)
                angleR = calculate_angle(shoulderR, elbowR, wristR)


                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                
                # Curl counter logic

                min_val = min(shoulder[1], elbow[1], wrist[1]) * 0.7
                max_val = max(shoulder[1], elbow[1], wrist[1]) * 1.3

                if min_val <= shoulder[1] <= max_val and min_val <= elbow[1] <= max_val and min_val <= wrist[1] <= max_val:
                    leftHorizontal = True
                else:
                    leftHorizontal = False
                    
                min_valR = min(shoulderR[1], elbowR[1], wristR[1]) * 0.7
                max_valR = max(shoulderR[1], elbowR[1], wristR[1]) * 1.3

                if min_valR <= shoulderR[1] <= max_valR and min_valR <= elbowR[1] <= max_valR and min_valR <= wristR[1] <= max_valR:
                    rightHorizontal = True
                else:
                    rightHorizontal = False

                if (abs(180 - angle) < 30):# and leftHorizontal:
                    poseString = 'left turn'
                elif (abs(90 - angle) < 30) and wrist[1] >= elbow[1]:
                    poseString = 'stop '
                elif (abs(90 - angle) < 30) and wrist[1] <= elbow[1]:
                    poseString = 'right turn '
                elif (abs(180 - angleR) < 30):# and rightHorizontal:
                    poseString = 'right turn'
                else:
                    poseString = 'neutral'

                if angle > 160:
                    stage = "down"
                if angle < 30 and stage =='down':
                    stage="up"
                    counter +=1
                    print(counter)
                        
            except:
                pass

            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
            cv2.putText(image, poseString, 
                        (10,60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

if __name__ == "__main__":
    main()