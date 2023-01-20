import numpy as np
import cv2 as cv

template = cv.imread('templateImages/1.jpg', 0)
frame = cv.imread("inputImage/image1_G.jpg", 0)
height, width = template.shape
cv.imshow("Frame", frame)
cv.imshow("Template", template)

img2 = frame.copy()

result = cv.matchTemplate(frame, template, cv.FONT_HERSHEY_SIMPLEX)
_, _, min_loc, max_loc = cv.minMaxLoc(result)

print(min_loc, max_loc)

location = max_loc
bottom_right = (location[0] + width, location[1]+height)
cv.rectangle(img2, location, bottom_right, (0, 0, 255), 5 )

cv.imshow("Matching", img2)

cv.waitKey(0)
cv.destroyAllWindows()