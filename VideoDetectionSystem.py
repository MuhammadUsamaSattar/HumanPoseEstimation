import cv2
import mediapipe as mp
import math
from VideoFeed import Video_Feed
import time

LEFT_ARM_INDEXES = [11, 13, 15]    #Index for landmarks in medpiapipe for joint locations
RIGHT_ARM_INDEXES = [12, 14, 16]

class Video_Detection_System():
    def __init__(self, capture_feed):
        self.video_feed = []
        for i in range(len(capture_feed)):
            self.video_feed.append(Video_Feed(capture_feed[i]))
        self.mpDraw = mp.solutions.drawing_utils
        self.actual_ratio = 0.44
        

    def run_iter(self, video_feed):
        video_feed.set_parameters_current()
        if video_feed.results.pose_landmarks:
            w, h, c = video_feed.frame.shape
            self.mpDraw.draw_landmarks(video_feed.frame, video_feed.results.pose_landmarks, video_feed.mpPose.POSE_CONNECTIONS)


    def run(self):
        while(c.cap.isOpened() for c in self.video_feed):
            for i in range(len(self.video_feed)):
                self.run_iter(self.video_feed[i])
                cv2.imshow('frame'+str(i),self.video_feed[i].frame)
            if self.video_feed[0].results.pose_landmarks != None:
                #print("Ratio:",(self.video_feed[0].results.pose_landmarks.landmark[11].x-self.video_feed[0].results.pose_landmarks.landmark[12].x)/(self.video_feed[0].results.pose_landmarks.landmark[24].y-self.video_feed[0].results.pose_landmarks.landmark[12].y))
                self.calculate_arm_angles(LEFT_ARM_INDEXES, self.video_feed)
            cv2.waitKey(1)
        
        cap.release()
        cv2.destroyAllWindows()


    def calculate_arm_angles(self, keys, video_feeds):
        print("Joint angles:")

        for i in range(len(video_feeds)):
            print('Shoulder joint:',self.calc_local_angle(video_feeds[i].results.pose_landmarks.landmark[keys[0]], video_feeds[i].results.pose_landmarks.landmark[keys[1]], video_feeds[i].frame.shape, video_feeds[i].results.pose_landmarks.landmark))
            print("Elbow joint:",self.calc_local_angle(video_feeds[i].results.pose_landmarks.landmark[keys[1]], video_feeds[i].results.pose_landmarks.landmark[keys[2]], video_feeds[i].frame.shape, video_feeds[i].results.pose_landmarks.landmark), '\n')


    def calc_local_angle(self, point1, point2, camera_matrix, landmarks): #Calculates the angle between -180 and 180 between point1 and point2 using point1 as the origin
        d_x = self.calc_actual_length(self.calc_human_angle(self.calc_ratio(landmarks), self.actual_ratio),point2.x-point1.x)
        d_y = point1.y-point2.y
        angle = abs(math.atan(((d_y)*camera_matrix[0])/((d_x)*camera_matrix[1]))*(180/math.pi))

        if angle != 0:
            if (point1.y-point2.y) > 0:
                if (point2.x-point1.x) > 0:
                    angle = angle
                else:
                    angle = 180 - angle
            else:
                if (point2.x-point1.x) > 0:
                    angle = 0 - angle
                else:
                    angle = -180 + angle

        return angle

    #def calc_global_angle(self, point1, point2, upper_body_size, ratio, camera_view):
    #    if camera_view == 'side':
    #        angle = asin((point2.y - point1.y)/sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2))
    #    elif camera_view == 'top':
    #        angle = 

    def calc_actual_length(self, theta, length):
        return length/(math.sin(theta))

    def calc_human_angle(self, current_ratio, actual_ratio):
        return math.acos(current_ratio/actual_ratio)

    def calc_ratio(self, landmarks):
        ratio = (landmarks[11].x-landmarks[12].x)/(landmarks[24].y-landmarks[12].y)

        return ratio