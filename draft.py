import cv2
import os
import numpy as np
import easyocr

# Не получилось сделать это автоматически в классе VideoHandler :(

# frame_id = int(input())
frame_id = 108

cap = cv2.VideoCapture("videos/video_2024-05-19_15-28-12.mp4")

os.makedirs(os.path.dirname("e:\\projects_py\\py_charm\\open_cv_project\\result.jpg"), exist_ok=True)

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
ret, frame = cap.read()
cv2.imwrite("result.jpeg", frame)

reader = easyocr.Reader(["en"], gpu=False)
name_file = reader.readtext("result.jpeg")
print(name_file)
# cap.release()
# cv2.destroyAllWindows()