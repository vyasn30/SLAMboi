import sdl2.ext
import cv2
import numpy

class FeatureExtractor(object):
    GX = 4 // 2
    GY = 2 // 2

    def __init__(self):
        self.orb = cv2.ORB_create(100)
        self.last = None
        self.bf = cv2.BFMatcher()

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)

        self.last = {"kps": kps, "des": des}
        print(des)
        if self.last is not None:
            matches = self.bf.match(des, self.last["des"])
            print(matches)

        return kps, des, matches


class Display(object):
    def __init__(self, W, H):
        self.W = W
        self.H = H
        # self.window = sdl2.ext.Window("Slam", size=(W, H))
        # # self.window.show()


    def paint(self, img):
        cv2.imshow('0', img)

        sdl2.ext.init()
        window = sdl2.ext.Window("test", size=(self.W, self.H))
        # window.show()
        windowSurf = sdl2.SDL_GetWindowSurface(window.window)
        windowArray = sdl2.ext.pixels3d(windowSurf.contents)

        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                # print("Quitting")
                exit(0)

        img = numpy.insert(img, 3, 255, axis=2)  # add alpha
        img = numpy.rot90(img)  # rotate dims

        numpy.copyto(windowArray, img)
        window.refresh()


