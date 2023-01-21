import cv2
import mediapipe as mp

class Video_Feed():
    def __init__(self, capture_feed):
        self.cap = capture_feed
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()


    def set_parameters_current(self):
        self.ret, self.frame = self.cap.read()
        self.frame = cv2.resize(self.frame, (640,360))

        self.imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(self.imgRGB)