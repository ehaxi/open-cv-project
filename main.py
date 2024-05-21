import cv2
import keyboard
import numpy as np
import math

class VideoHandler():
    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(url)
    def show_video(self):
        hsv_min = np.array((101, 30, 60), np.uint8)
        hsv_max = np.array((255, 255, 255), np.uint8)
        counter = 0
        max_cont = -1
        count_flag = 0
        arr_lap = []
        arr_frame = []

        while True:
            ret, frame = self.cap.read()

            if frame is not None:
                counter += 1

                laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()
                arr_lap.append(laplacian)
                arr_frame.append(counter)

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
                thresh = cv2.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
                contours0, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for cnt in contours0:

                    rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
                    box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
                    box = np.intp(box)  # округление координат
                    center = (int(rect[0][0]), int(rect[0][1]))
                    area = int(rect[1][0] * rect[1][1])  # вычисление площади

                    # вычисление координат двух векторов, являющихся сторонам прямоугольника
                    edge1 = np.intp((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                    edge2 = np.intp((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                    # выясняем какой вектор больше
                    usedEdge = edge1
                    if cv2.norm(edge2) > cv2.norm(edge1):
                        usedEdge = edge2
                    reference = (1, 0)  # горизонтальный вектор, задающий горизонт

                    # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
                    angle = 180.0 / math.pi * math.acos((reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (
                                cv2.norm(reference) * cv2.norm(usedEdge)))

                    if area > 6500:
                        cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)  # рисуем прямоугольник
                        cv2.circle(frame, center, 5, (0, 255, 0), 2)  # рисуем маленький кружок в центре прямоугольника
                        # выводим в кадр величину угла наклона
                        cv2.putText(frame, "%d" % int(angle), (center[0] + 20, center[1] - 20),
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow("mask", frame)

                if cv2.waitKey(10) and keyboard.is_pressed('q'):
                    break

            else:
                break

        print(arr_frame[arr_lap.index(max(arr_lap))])

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    url = "videos/video_2024-05-19_15-28-12.mp4" # input()
    VideoHandler(url).show_video()