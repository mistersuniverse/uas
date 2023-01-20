import numpy as np
import cv2 as cv 
import glob2

def crop():
    pass

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
    # mask_input_image = cv.adaptiveThreshold(input_image, 255, cv.ADAPTIVE_THRESH_GUASSIAN_C, cv.THRESH_BINARY, 50, 5)
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

    # contours of input image
    contours_input_image, hierarchy = cv.findContours(dilated_masked_input_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    x, y, w, h = cv.boundingRect(contours_input_image[1])

    # drawing a rectangle in the roi
    top_left_corner_of_rectangle = (x - 5, y - 5)
    bottom_right_corner_of_rectangle = (x + w + 5, y + h + 5)

    # input_image = cv.rectangle(input_image, top_left_corner_of_rectangle, bottom_right_corner_of_rectangle, (0, 0, 255), 5)
    cv.imshow("Contours", input_image)
    
    # top_left_corner_of_rectangle = (x - 5, y - 5)
    # bottom_right_corner_of_rectangle = (x + w + 5, y + h + 5)

    blank_image = np.ones((w + 10, h + 10), dtype= "uint8")

    modified_input_image = dilated_masked_input_image[(y-5): (y+h+5), (x-5): (x+w+5)]
    cv.imshow("modified input image", modified_input_image)

    # contours of template image
    contours_template, hierarchy = cv.findContours(dilated_masked_template, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    x, y, w, h = cv.boundingRect(contours_template[1])
    
    blank_image = np.ones((w + 10, h + 10), dtype= "uint8")

    modified_template = dilated_masked_template[(y-5): (y+h+5), (x-5): (x+w+5)]
    cv.imshow("modified template", modified_template)
    
    x, y = modified_input_image.shape 
    blank_image = cv.resize(modified_template, (y, x))
    print(modified_template.shape)
    print(blank_image.shape)
    print(modified_input_image.shape)

    cv.imshow("input image 2", blank_image) 
    # creating union of mask to compare the area between input image & template
    reference_image = cv.bitwise_and(modified_input_image, blank_image)
    cv.imshow("reference image", reference_image)

    # contours of reference image
    contours_reference_image, hierarchy = cv.findContours(reference_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("area in reference image", cv.contourArea(contours_reference_image[1])) 

    # contours of modified template
    contours_modified_template, hierarchy = cv.findContours(blank_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("area in modified template", cv.contourArea(contours_modified_template[1]))

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

    x = cv.contourArea(contours_reference_image[1])
    y = cv.contourArea(contours_modified_template[1])

    # threshold = ((x-y)/y)
    # print(threshold)
    # # comparing area of template & reference image; True if characters have same area
    # if threshold < 0.2:
    #     print('char detected') 

    # else :
    #     print('char not detected')

    xor_output = cv.bitwise_xor(modified_input_image, blank_image)
    cv.imshow("xor_output", xor_output) 

    # result =     
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":

    # input_image_paths = glob2.glob("inputImage/*.jpg")
    # template_paths = glob2.glob("templateImages/*.jpg")

    # for input_images in input_image_paths:
    #     for template in template_paths:

    #         print("template : {}; input images : {}".format(template, input_images))
    #         main(template, input_images)
    # 
    main("templates/G.jpg", "inputImage/A2.jpg")                                                                                                                                                   