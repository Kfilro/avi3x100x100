import cv2
import numpy as np
from google.colab import files

text = 'I am Ksenia'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
thickness = 1
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.putText(img, text, (5, 50), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

output = cv2.VideoWriter('running_text.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, (100, 100))

for i in range(100):
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_width = text_size[0]
    text_height = text_size[1]
    start_point = ( -int(text_width * ( (i) / 100))  + 50, 50)

    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.putText(img, text,  start_point, font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)


    end_point = (start_point[0] + text_width, start_point[1] + text_height)
    output.write(img)

output.release()
files.download('running_text.avi')
