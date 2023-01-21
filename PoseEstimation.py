import cv2
from VideoDetectionSystem import Video_Detection_System



cap = [cv2.VideoCapture(r'1.mp4')]
VDS = Video_Detection_System(cap)

VDS.run()