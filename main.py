import cv2
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import imutils
import easyocr

class VideoHandler():
    def __init__(self, url):
        self.cap = cv2.VideoCapture(url)
    def show_video(self):

        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        while True:
            ret, frame = self.cap.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_gray = cv2.GaussianBlur(frame_gray, (1, 1), 0)
            frame_gray = cv2.filter2D(frame_gray, -1, kernel)

            # cv2.imshow("frame", frame)
            cv2.imshow("mask", frame_gray)

            if cv2.waitKey(10) and keyboard.is_pressed('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    url = "videos/video_without_turn.mp4" # input()
    VideoHandler(url).show_video()