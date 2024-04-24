import cv2
import os

# Не получилось сделать это автоматически в классе VideoHandler :(

frame_id = int(input())

cap = cv2.VideoCapture("videos/video_without_turn.mp4")

os.makedirs(os.path.dirname("e:\\projects_py\\py_charm\\open_cv_project\\result.jpg"), exist_ok=True)

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id + 7)
ret, frame = cap.read()
cv2.imwrite("result.jpeg", frame)

cap.release()
cv2.destroyAllWindows()