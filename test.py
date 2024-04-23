import cv2
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import imutils
import easyocr

class VideoHandler():
    def __init__(self, url):
        self.cap = cv2.VideoCapture(0)
    def show_video(self):
        max_cont = -1
        counter = 0
        count_flag = 0
        while True:
            flag, img = self.cap.read()
            if img is not None:
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img_canny = cv2.Canny(img_gray, 10, 250)
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
                closed = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel)

                contours = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
                # contours = imutils.grab_contours(contours)

                for cont in contours:
                    counter += 1
                    # сглаживание и определение количества углов
                    sm = cv2.arcLength(cont, True)
                    apd = cv2.approxPolyDP(cont, 0.02 * sm, True)
                    if len(cont) >= 1000:
                        max_cont = max(len(cont), max_cont)
                        count_flag = counter
                        # cv2.imwrite("result.jpeg", img)

                    # выделение контуров
                    if len(apd) == 4:
                        cv2.drawContours(img_canny, [apd], -1, (0, 255, 0), 2)

                cv2.imshow("res", img_canny)

                if cv2.waitKey(10) and keyboard.is_pressed('q'):
                    break

        print(max_cont, count_flag)
        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    url = "videos/video_without_turn.mp4" # input()
    VideoHandler(url).show_video()