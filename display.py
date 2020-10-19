import sdl2.ext
import cv2
import numpy

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


