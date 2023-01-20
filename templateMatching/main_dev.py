import numpy as np
import cv2 as cv

def main(template, input_image):

    #
    template = cv.imread(template, 0)
    
    #
    input_image = cv.imread(input_image, 0)
    input_image = cv.resize(input_image, template.shape)
    cv.imshow("input image", input_image)

    kernel = np.ones((2,2), dtype="uint8") 

    # input_image = cv.erode(input_image, kernel, iterations=1)
    # cv.imshow("eroded input image", input_image)

    # creating mask of template
    _, mask_template = cv.threshold(template, 10, 255, cv.THRESH_BINARY)
    cv.imshow("mask_template", mask_template)

    contours, _ = cv.findContours(mask_template, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv.boundingRect(contours[1])

    # blank_image = np.ones((w + 10, h + 10), dtype= "uint8")

    mask_template = mask_template[(y-5): (y+h+5), (x-5): (x+w+5)]
    cv.imshow("modified input image", mask_template)

    # # creating mask of input image
    # mask_input_image = cv.adaptiveThreshold(input_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 100, 1) #?
    # cv.imshow("Adapt Thresh", mask_input_image)

    # 
    _, mask_input_image = cv.threshold(input_image, 50, 255, cv.THRESH_BINARY)
    cv.imshow("mask_input_image", mask_input_image)
    
    #
    if mask_input_image[0, 0] == 0:
        mask_input_image = cv.bitwise_not(mask_input_image)
        cv.imshow("reverse", mask_input_image)

    else :
        pass

    contours, _ = cv.findContours(mask_input_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv.boundingRect(contours[1])

    if len(contours) > 10:
        mask_input_image = cv.GaussianBlur(input_image, (55, 55), 0)
        cv.imshow("input image 1", mask_input_image)

        #
        if mask_input_image[0, 0] == 0:
            mask_input_image = cv.bitwise_not(mask_input_image)
            cv.imshow("reverse", mask_input_image)

        else :
            pass

        contours, _ = cv.findContours(mask_input_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        x, y, w, h = cv.boundingRect(contours[0])

    else :
        pass
    
    mask_input_image = mask_input_image[(y-5): (y+h+5), (x-5): (x+w+5)]
    cv.imshow("modified input image", mask_input_image)

    x, y = mask_template.shape

    mask_input_image = cv.resize(mask_input_image, (y, x))
    # mask_input_image = cv.GaussianBlur(mask_input_image, (55, 55), 0)

    # cv.imshow("a", eroded_masked_input_image)
    cv.imshow("b", mask_template)
    cv.imshow("c", mask_input_image)
    # xor test
    xor_output = cv.bitwise_xor(mask_template, mask_input_image)
    cv.imshow("xor output", xor_output)

    # xor test
    no_of_white_pixels = np.sum(xor_output == 255)
    print(no_of_white_pixels)
    xor_test = True
    threshold = 2000

    if (no_of_white_pixels > threshold):
        xor_test = False
    else :
        pass

    # result
    if xor_test == True:
        print("char detected")

    else :
        print("char not detected")

    # #
    # and_output = cv.bitwise_and(mask_template, eroded_masked_input_image) 
    # cv.imshow("and output", and_output)

    # contours, _ = cv.findContours(and_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # print(contours)

    # for c in contours:
    #     print(c)

    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main("templates/A.jpg", "inputImage/A2.jpg")
