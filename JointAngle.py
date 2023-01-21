import math

class JointAngle:
    def __init__(self, camera_size):
        self.camera_x = camera_size[0]
        self.camera_y = camera_size[1]


    def calcPixelFraction(self, objpixel_min, objpixel_max, camera_y):
        pixel_fraction = (objpixel_max-objpixel_min)/(camera_y)

        return pixel_fraction

    def calcVFOV(self, actual_length, distance, pixel_fraction): #actual legnth is the real length of the object. pixelfraction is the fraction of pixels taken by the refernce object compared to total.
        VFOV = 2*math.atan((actual_length/pixel_fraction)/(2*distance))

        return FOV

    def calcDistance(self, actual_length, pixel_fraction, VFOV):#actual length is person's legnth, this will have to be set beforehand in code.
        object_angle = VFOV * pixel_fraction
        print(object_angle*180/math.pi)
        distance = actual_length/math.tan(object_angle)

        return distance

    def calc_Angle(self, point1, point2): #Calculates the angle between -180 and 180 between point1 and point 2 using point1 as the origin
        point2.y = 1 - point2.y
        point1.y = 1 - point1.y

        angle = abs(math.atan(((point2.y-point1.y)*self.camera_y)/((point2.x-point1.x)*self.camera_x))*(180/math.pi))

        if angle != 0:
            if (point2.y-point1.y) > 0:
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