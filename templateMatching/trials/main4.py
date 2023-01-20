import numpy as np
import cv2 as cv

def main(template, input_image):
    # template loadin
    original_grayscaled_template = cv.imread(template, 0)
    cv.imshow("Original Grayscaled Template", original_grayscaled_template)

    # input image loading
    original_grayscaled_input_image = cv.imread(input_image, 0)
    resized_grayscaled_input_image = cv.resize(original_grayscaled_input_image, original_grayscaled_template.shape)
    cv.imshow("Original Grayscaled Template", resized_grayscaled_input_image)

    # getting cropped input image & template
    cropped_input_image = crop(resized_grayscaled_input_image, (2,2))
    cropped_template = crop(original_grayscaled_template, (2,2))

    if cropped_input_image.size > cropped_template.size:
        

    elif cropped_input_image.size < cropped_template.size:
        pass

    else :
        pass 

    # XOR
    xor_output = ""
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def crop(img, kernel_size):
    
    kernel = np.ones(kernel_size, dtype="uint8")

    # creating a mask
    _, mask_img = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
    cv.imshow(f"mask {img})",mask_img)

    # morphology
    dilated_masked_img = cv.dilate(mask_img,kernel, iterations=1)
    cv.imshow(f"dilated mask {img}", dilated_masked_img)

    # contours
    _, contours, hierarchy = cv.findContours(dilated_masked_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # getting top left corner, width, height
    x, y, w, h = cv.boundingRect(contours)

    # creating a blank image
    blank_image = np.ones((w + 10, h + 10), dtype="uint8")

    # final cropping
    cropped_img = dilated_masked_img[(y-5):(y+h+5), (x-5):(x+w+5)]
    cv.imshow(f"cropped {img}", cropped_img)


    return cropped_img

if __name__ == "__main__":

    main("template/G.jpg", "inputImage/A2.jpg")