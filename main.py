from display import Display
import cv2
import numpy as np
from FeatureExtractor import  FeatureExtractor


W, H = 1920 // 2, 1080 // 2


        # sx = img.shape[0]//self.GX
        # sy = img.shape[1]//self.GY
        #
        # akp = []
        #
        # for ry in range(0, img.shape[0], sy):
        #     for rx in range(0, img.shape[0], sx):
        #         img_chunk = img[ry:ry+sy , rx:rx+sx]
        #         kp = self.orb.detect(img_chunk, None)
        #         for p in kp:
        #             p.pt = (p.pt[0] + rx, p.pt[1]+ry)
        #             akp.append(p)
        #
        # return akp


fe = FeatureExtractor()


def process_frame(img):
    img = cv2.resize(img, (W, H))
    matches = fe.extract(img)

    for pt1, pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1.pt)
        u2, v2 = map(lambda x: int(round(x)), pt2.pt)

        cv2.circle(img, (u1, v2), color=(0, 255, 0), radius=3)
        cv2.line(img, (u1,v1), (u2,v2), color=(255,0,0))
    # print("in process_frame")
    disp = Display(W, H)
    # print("created disp")
    disp.paint(img)


cap = cv2.VideoCapture("test.mp4")
# print("Captured video")
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        process_frame(frame)
        # print("Calling process_frame")

    else:
        break
