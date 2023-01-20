import numpy as np
import cv2 as cv 

template = cv.imread("templateImages/G.jpg", 0)
input_image = cv.imread("inputImage/A2.jpg", 0)

input_image = cv.resize(input_image, template.shape)
cv.imshow("input_image", input_image)

_, mask_input_image = cv.threshold(input_image, 10, 255, cv.THRESH_BINARY)
cv.imshow("mask_input_image", mask_input_image)

kernel = np.ones((2,2),dtype="uint8")

dilated_masked_input_image = cv.dilate(mask_input_image, kernel, iterations=1)
cv.imshow("dilated_mask_input_image", dilated_masked_input_image)

contours, hierarchy = cv.findContours(mask_input_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(contours)
# contours = cv.drawContours(input_image, [contours[1]], -1, (0, 0, 255), 10)
# contours of reference image

reference_image = cv.bitwise_and(dilated_masked_input_image, dilated_masked_template)
cv.imshow("reference image", reference_image)

contours_reference_image, hierarchy = cv.findContours(reference_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("area in reference image", cv.contourArea(contours_reference_image[1]))

a = b = list()
print(contours[1])

for i in contours[1]:
    a.append(i[0, 0])
    b.append(i[0, 1])

a.sort()
b.sort()

print(a)
print(b)

top_left_corner_of_rectangle = (a[0], b[0])
bottom_right_corner_of_rectangle = (a[-1], b[-1])

input_image = cv.rectangle(input_image, top_left_corner_of_rectangle, bottom_right_corner_of_rectangle, (0, 0, 255), 5)
cv.imshow("Contours", input_image)

print(contours)

cv.waitKey(0)
cv.destroyAllWindows()