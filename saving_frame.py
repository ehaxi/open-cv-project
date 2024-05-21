import cv2
import easyocr
import os

def file_writer():
    frame_id = int(input())

    cap = cv2.VideoCapture("videos/video_2024-05-19_15-28-12.mp4")

    os.makedirs(os.path.dirname("e:\\projects_py\\py_charm\\open_cv_project\\result.jpg"), exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = cap.read()
    cv2.imwrite("result.jpeg", frame)

def text_reader():
    reader = easyocr.Reader(["en", "ru"], gpu=False)
    name_file = reader.readtext("result.jpeg", detail=0)
    frame = cv2.imread("result.jpeg")
    cv2.imwrite(f"{name_file[0]}.jpeg", frame)

if __name__ == '__main__':
    file_writer()
    text_reader()