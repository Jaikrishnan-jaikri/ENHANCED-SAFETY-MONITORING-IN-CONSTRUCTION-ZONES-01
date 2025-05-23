from ultralytics import YOLO
import cvzone
import cv2
import math
from APP.models import DetectedSafety
import pygame
import time

# Running real-time from webcam
cap = cv2.VideoCapture(0)

model = YOLO('C:/Users/SPIRO-PYTHON/Downloads/oct/cv/ITPCV01 DONE/ITPCV01-FINAL CODE/DEPLOYMENT/PROJECT/APP/best.pt')
pygame.mixer.init()
# Reading the classes
classnames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
frame_number = 0
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)
    s1 = 0

    # Getting bbox, confidence, and class names information to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                scale=1.5, thickness=2)

                
                if classnames[Class] == "Hardhat":
                    
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Mask":
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "NO-Hardhat":
                    play_audio("E:/SARAVANAN-2024-2025/NEW TITLES-2024/OPENCV AND YOLOV8/ITPCV01 DONE/DEPLOYMENT/PROJECT/APP/notification.mp3")
                    print("Confidence --->",confidence)
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "NO-Mask":
                    play_audio("E:/SARAVANAN-2024-2025/NEW TITLES-2024/OPENCV AND YOLOV8/ITPCV01 DONE/DEPLOYMENT/PROJECT/APP/notification.mp3")
                    print("Confidence --->",confidence)
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "NO-Safety Vest":
                    play_audio("E:/SARAVANAN-2024-2025/NEW TITLES-2024/OPENCV AND YOLOV8/ITPCV01 DONE/DEPLOYMENT/PROJECT/APP/notification.mp3")
                    print("Confidence --->",confidence)
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Person":
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Safety Cone":
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Safety Vest":
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "machinery":
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "vehicle":
                    play_audio("E:/SARAVANAN-2024-2025/NEW TITLES-2024/OPENCV AND YOLOV8/ITPCV01 DONE/DEPLOYMENT/PROJECT/APP/notification.mp3")
                    print("Confidence --->",confidence)
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    detected_safety = DetectedSafety(
                        frame_number=frame_number,
                        class_name=classnames[Class],
                        confidence=confidence,
                        coordinates=coordinates
                    )
                    detected_safety.save()

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                
                    
                    
                else:
                    print("No Data")
                    
            else:
                    print("No Data")
                    

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()