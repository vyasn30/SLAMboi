from display import Display
import cv2
import numpy as np

W, H = 1920 // 2, 1080 // 2


class FeatureExtractor(object):
    GX = 4//2
    GY = 2//2
    def __init__(self):
        self.orb = cv2.ORB_create(100)

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in feats]
        des = self.orb.compute(img, kps)

        return kps, des
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
    kps, des = fe.extract(img)

    for p in kps:
        u,v = map (lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u,v), color=(0, 255, 0), radius=4)

    print("in process_frame")
    disp = Display(W, H)
    print("created disp")
    disp.paint(img)


cap = cv2.VideoCapture("test.mp4")
print("Captured video")
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        process_frame(frame)
        print("Calling process_frame")

    else:
        break
