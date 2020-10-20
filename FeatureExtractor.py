import cv2
import numpy as np


class FeatureExtractor(object):
    GX = 4 // 2
    GY = 2 // 2

    def __init__(self):
        self.orb = cv2.ORB_create()
        self.last = None
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)
        #
        # self.last = {"kps": kps, "des": des}

        ret = []
        # print(des)
        if self.last is not None:

            matches = self.bf.knnMatch(des, self.last["des"], k=2)
            print(matches)
            for m, n in matches:
                if m.distance < 0.75*n.distance:
                    ret.append((kps[m.queryIdx], self.last["kps"][m.trainIdx]))

        self.last = {"kps": kps, "des": des}

        return ret