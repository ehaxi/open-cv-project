import cv2
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import imutils
import easyocr
import os

class VideoHandler():
    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(0)
    def show_video(self):
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        thresh = 40
        counter = 0
        max_cont = -1
        count_flag = 0

        while True:
            ret, frame = self.cap.read()

            if frame is not None:
                roi = frame[50:720, 300:1000]
                counter += 1

                frame_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                frame_gray = cv2.filter2D(frame_gray, -1, kernel)
                _, frame_thresh = cv2.threshold(frame_gray, thresh, 255, cv2.THRESH_BINARY)

                contours, _ = cv2.findContours(frame_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for cnt in contours:
                    area = cv2.contourArea(cnt)

                    if len(cnt) >= max_cont:
                        max_cont = len(cnt)
                        count_flag = counter

                    if area > 400:
                        rect = cv2.minAreaRect(cnt)
                        box = cv2.boxPoints(rect)
                        box = np.intp(box)

                        print(f"Angle: {round(rect[2], 2)}")
                        cv2.drawContours(roi, [box],0, (0, 255, 0), 2)

                cv2.imshow("mask", frame)

                if cv2.waitKey(10) and keyboard.is_pressed('q'):
                    break

            else:
                break

        print('\n', count_flag)

        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    url = "videos/video_without_turn.mp4" # input()
    VideoHandler(url).show_video()