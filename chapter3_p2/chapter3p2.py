import cv2
import numpy
from random import randint
from copy import deepcopy
# read and split image
NOISE_PERCENT = 30

SOBEL_FILTER=[[1,0,-1],
            [2,0,-2],
            [1,0,-1]]

HORIZONTAL_FILTER=[[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]]

VERTICAL_FILTER=[[1 ,1 ,1],
                 [0 ,0 ,0],
                [-1,-1,-1]]

LAPLACIAN_FILTER=[[-1,-1,-1],
            [-1,8,-1],
            [-1,-1,-1]]

img = cv2.imread("chapter3_p2/img.jpg")
b, g, r = cv2.split(img)


############ START ADD PEPPER ##############


def add_pepper_noise(img, noise_percent=20):
    return numpy.array([[randint(0, 255) if (randint(1, noise_percent) == noise_percent) else pixel for pixel in line] for line in img])

############ END ADD PEPPER ##############


def get_value(mat, x, y):
    try:
        return mat[x][y]
    except:
        return 0



############ START MEDIAN ##############


def median_filter(img):
    def get_median(img, x, y):
        arr = [get_value(img, x-1, y-1), get_value(img, x-1, y), get_value(img, x-1, y+1), get_value(img, x, y-1), get_value(
            img, x, y), get_value(img, x, y+1), get_value(img, x+1, y-1), get_value(img, x+1, y), get_value(img, x+1, y+1)]
        arr.sort()
        return arr[4]

    img_cp = deepcopy(img)

    return numpy.array([[get_median(img_cp, x, y) for y, pixel in enumerate(line)] for x, line in enumerate(img)])
############ END MEDIAN ##############


############ START CONVOLUTION ##############
def convolution(mat, filter):
    padding = len(mat) - len(filter)

    def convol(mat, filter, x, y):
        return get_value(mat, x-1, y-1) * get_value(filter, (x-1)%3, (y-1)%3) + get_value(mat, x-1, y)*get_value(filter, (x-1)%3, y%3) + get_value(mat, x-1, y+1) * get_value(filter, (x-1)%3, (y+1)%3) + get_value(mat, x, y-1) * get_value(filter, x%3, (y-1)%3) + get_value(mat, x, y) * \
            get_value(filter, x%3, y%3) + get_value(mat, x, y+1)*get_value(filter, x%3, (y+1)%3) + get_value(mat, x+1, y-1) * get_value(filter,
                                                                                                                              (x+1)%3, (y-1)%3) + get_value(mat, x+1, y) * get_value(filter,( x+1)%3, y%3) + get_value(mat, x+1, y+1)*get_value(filter, (x+1)%3, (y+1)%3)

    mat_cp = deepcopy(mat)
    return numpy.array([[convol(mat_cp,filter, x, y) for y, pixel in enumerate(line)] for x, line in enumerate(mat)]) 
############ END CONVOLUTION ##############

def run_add_pepper_noise(b):
    cv2.imwrite('before_add_pepper.png', b)
    cv2.imwrite('after_add_pepper.png', add_pepper_noise(b, NOISE_PERCENT))

def run_sobel_filter(b):
    cv2.imwrite('before_sobel.png', b)
    cv2.imwrite('after_sobel.png', convolution(b, SOBEL_FILTER))

def run_vertical_filter(b):
    cv2.imwrite('before_verticval.png', b)
    cv2.imwrite('after_verticval.png', convolution(b, VERTICAL_FILTER))

def run_horizontal_filter(b):
    cv2.imwrite('before_horizontal.png', b)
    cv2.imwrite('after_horizontal.png', convolution(b, HORIZONTAL_FILTER))

def run_laplacian_filter(b):
    cv2.imwrite('before_laplacian.png', b)
    cv2.imwrite('after_laplacian.png', convolution(b, LAPLACIAN_FILTER))


def run_median_filter(b):
    added_noise = add_pepper_noise(b, NOISE_PERCENT)
    cv2.imwrite('before_median.png', add_pepper_noise(b, NOISE_PERCENT))
    cv2.imwrite('after_median.png', median_filter(
        add_pepper_noise(b, NOISE_PERCENT)))



# run_sobel_filter(b)
# run_vertical_filter(b)
# run_horizontal_filter(b)
# run_laplacian_filter(b)
# run_median_filter(add_pepper_noise(b))
# run_add_pepper_noise(b)



############### START XRAY ###############
xray = cv2.imread("chapter3_p2/xray.jpg")
bx, gx, rx = cv2.split(xray)

def add_images(a,b):
    return numpy.array([[round((a[x][y]+b[x][y])/2) for y, pixel in enumerate(line)] for x, line in enumerate(a)])
cv2.imwrite('xray/origin.png', bx)

b_fig_laplacian =  convolution(bx, LAPLACIAN_FILTER)
cv2.imwrite('xray/b_fig_laplacian.png', b_fig_laplacian)

c_fig = add_images(b_fig_laplacian,bx)
cv2.imwrite('xray/c_fig.png', c_fig)

d_fig_sobel = convolution(bx, SOBEL_FILTER)
cv2.imwrite('xray/d_fig_sobel.png', d_fig_sobel)


def average_image(img):
    def get_avg(img, x, y):
        arr = [[ get_value(img, x+i-2, y+j-2) for j in range(5)] for i in range(5)]
        return round((sum(sum(arr,[])) )/25  )  
    img_cp = deepcopy(img)
    return numpy.array([[get_avg(img_cp, x, y) for y, pixel in enumerate(line)] for x, line in enumerate(img)])

e_fig_avg = average_image(d_fig_sobel)
cv2.imwrite('xray/e_fig_avg.png', e_fig_avg)


# cv2.imwrite('xray/after_horizontal.png', laplacian)