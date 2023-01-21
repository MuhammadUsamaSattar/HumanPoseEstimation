import cv2
from VideoDetectionSystem import Video_Detection_System



cap = [cv2.VideoCapture(r'F:\Usama\Academics\NUST\Projects\FYP\HumanPoseEstimation\Data\4.mp4')]
VDS = Video_Detection_System(cap)

VDS.run()