from display import Display
import cv2

W, H = 1920 // 2, 1080 // 2


def process_frame(img):
    img = cv2.resize(img, (W, H))
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
