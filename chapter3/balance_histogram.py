import cv2
import numpy
import matplotlib.pyplot as plt

#read and split image
img = cv2.imread("img.jpg")
print(img)
print(cv2.split(img))
b,g,r = cv2.split(img)

def gen_histogram(channel):    
    histogram = [0]*256
    for line in channel:
        for pixel in line:
            histogram[pixel]+=1
    return histogram
    
def cal_cumulative_his(histogram):
    tmp = 0
    cumulative=[0]*256
    for i, count in enumerate(histogram):
        tmp += histogram[i] 
        cumulative[i]+=tmp
    return cumulative

def get_cdf(cumulative,histogram,channel):
    total = len(channel) * len(channel[0])
    return [count/total for count in histogram]

# def get_final_his(cumulative,cdf,histogram):
#     return [round(cdf[i]*cumulative[i]) for i,count in enumerate(histogram)]
def replace_new_pixel_vaule(cumulative,cdf,histogram,channel):
    return [ [round(cdf[j]*256)  for j in i]for i in channel]
def balance(channel):
    histogram =  gen_histogram(channel)
    cumulative = cal_cumulative_his(histogram)
    return cumulative
    cdf = get_cdf(cumulative,histogram,channel)
    print("cdf la: ",cdf)
    new_img = replace_new_pixel_vaule(cumulative,cdf,histogram, channel)
    return gen_histogram(new_img)
    # return get_final_his(cumulative,cdf,histogram)

his_g = gen_histogram(g)
his_g_balanced = balance(g)
plt.plot(his_g)

plt.plot(his_g_balanced)
plt.show()