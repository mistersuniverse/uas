import numpy as np
import cv2 as cv 


def main(template, input_image):

    # loading template
    template = cv.imread(template, 0)
    cv.imshow("template", template)

    # loading input image
    input_image = cv.imread(input_image, 0)
    input_image = cv.resize(input_image, template.shape)
    cv.imshow("input_image", input_image)

    # creating mask of template
    _, mask_template = cv.threshold(template, 10, 255, cv.THRESH_BINARY)
    cv.imshow("mask_template", mask_template)

    # creating mask of input image
    _, mask_input_image = cv.threshold(input_image, 10, 255, cv.THRESH_BINARY)
    cv.imshow("mask_input_image", mask_input_image)

    # kernel for morphology
    kernel = np.ones((2,2),dtype="uint8")

    # morphology in template
    dilated_masked_template = cv.dilate(mask_template, kernel, iterations=1)
    cv.imshow("dilated_mask_input_image", dilated_masked_template)

    # morphology in input image
    dilated_masked_input_image = cv.dilate(mask_input_image, kernel, iterations=1)
    cv.imshow("dilated_mask_input_image", dilated_masked_input_image)

    # contours of reference image
    contours_input_image, hierarchy = cv.findContours(dilated_masked_input_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("area in reference image", cv.contourArea(contours_input_image[1]))

    # creating union of mask to compare the area between input image & template
    reference_image = cv.bitwise_and(dilated_masked_input_image, dilated_masked_template)
    cv.imshow("reference image", reference_image)

    # contours of reference image
    contours_reference_image, hierarchy = cv.findContours(reference_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("area in reference image", cv.contourArea(contours_reference_image[1]))

    x, y, w, h = cv.boundingRect(contours_input_image[1])

    # print(contours_reference_image[1])
    # a = b = list()
    # for i in contours_input_image[1]:
    #     print(i[0, 0], i[0, 1])
    #     a.append(i[0, 0])
    #     b.append(i[0, 1])

    # a.sort()
    # b.sort()

    # print(a[: 50])
    # print(b[: 50])

    # drawing a rectangle in the roi
    top_left_corner_of_rectangle = (x - 5, y - 5)
    bottom_right_corner_of_rectangle = (x + w + 5, y + h + 5)

    input_image = cv.rectangle(input_image, top_left_corner_of_rectangle, bottom_right_corner_of_rectangle, (0, 0, 255), 5)
    cv.imshow("Contours", input_image)
    
    # top_left_corner_of_rectangle = (x - 5, y - 5)
    # bottom_right_corner_of_rectangle = (x + w + 5, y + h + 5)
    blank_image = np.ones((w + 10, h + 10), dtype= "uint8")
    cv.imshow("blank image", blank_image)

    blank_image = input_image[(y-5): (y+h+5), (x-5): (x+w+5)]
    cv.imshow("blank image", blank_image)
    
    # contours of template
    contours_template, hierarchy = cv.findContours(dilated_masked_template, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("area in template", cv.contourArea(contours_template[1]))

    # comparing area of template & reference image; True if characters have same area
    if cv.contourArea(contours_reference_image[1]) - cv.contourArea(contours_template[1]) == 0:
        print('char detected') 

    else :
        print('char not detected')

    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main("templates/A.jpg", "inputImage/H1.jpg")