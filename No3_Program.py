import numpy as np
import cv2
from tqdm import tqdm

ExpNumber = 1

#These thresholds were empirically determined
threshold_1 = 433
threshold_2 = 990
threshold_3 = 4095

#identification to import images
Image_number_0min = 1001
Image_number_1 = 1002
Treat_No = 2
ID = 'High'
Minute = 1
allowed_pixel = 1

#"FITC" as Fluo-4 AM, "Red" as MitoSOX Red
Color = str('FITC')

for i in tqdm(range(1001, 1033)):

    img = cv2.imread("FITC_" + str(i) + ".tif", cv2.IMREAD_UNCHANGED)

    img_Gauss = cv2.GaussianBlur(img,(3,3),0)
    ret, img_bin = cv2.threshold(img_Gauss, threshold_1, 4095, cv2.THRESH_BINARY)
    array = FindCenter(img_Gauss, img, threshold_1, 2)
    np.savetxt('Result_No' +str(ExpNumber)+ '_FITC_' + str(i) + '.csv', array, delimiter=',', fmt="%s")

for i in tqdm(range(1001, 1033)):

    img = cv2.imread("RED_" + str(i) + ".tif", cv2.IMREAD_UNCHANGED)

    img_Gauss = cv2.GaussianBlur(img,(3,3),0)
    ret, img_bin = cv2.threshold(img_Gauss, threshold_2, 4095, cv2.THRESH_BINARY)
    array = FindCenter(img_Gauss, img, threshold_2, 2)
    np.savetxt('Result_No' +str(ExpNumber)+ '_RED_' + str(i) + '.csv', array, delimiter=',', fmt="%s")

for i in tqdm(range(2001, 2033)):

    img = cv2.imread("FITC_" +str(i)+ ".tif", cv2.IMREAD_UNCHANGED)

    img_Gauss = cv2.GaussianBlur(img,(3,3),0)
    ret, img_bin = cv2.threshold(img_Gauss, threshold_1, 4095, cv2.THRESH_BINARY)
    array = FindCenter(img_Gauss, img, threshold_1, 2)
    np.savetxt('Result_No' +str(ExpNumber)+ '_FITC_' + str(i) + '.csv', array, delimiter=',', fmt="%s")

for i in tqdm(range(2001, 2033)):

    img = cv2.imread("RED_" +str(i)+ ".tif", cv2.IMREAD_UNCHANGED)

    img_Gauss = cv2.GaussianBlur(img,(3,3),0)
    ret, img_bin = cv2.threshold(img_Gauss, threshold_2, 4095, cv2.THRESH_BINARY)
    array = FindCenter(img_Gauss, img, threshold_2, 2)
    np.savetxt('Result_No' + str(ExpNumber) + '_RED_' + str(i) + '.csv', array, delimiter=',', fmt="%s")


img_0min = open('Result_No' +str(ExpNumber)+ '_' + Color + '_' +str(Image_number_0min)+ '.csv', 'r')
img_0min = np.loadtxt(img_0min, delimiter=",")
img_1 = open('Result_No' +str(ExpNumber)+ '_' + Color + '_' +str(Image_number_1)+ '.csv', 'r')
img_1 = np.loadtxt(img_1, delimiter=",")

no_laser_img_0min = open('Result_No' +str(ExpNumber)+ '_' + Color + '_' +str(Image_number_0min+1000)+ '.csv', 'r')
no_laser_img_0min = np.loadtxt(no_laser_img_0min, delimiter=",")
no_laser_img_1 = open('Result_No' +str(ExpNumber)+ '_' + Color + '_' +str(Image_number_1+1000)+ '.csv', 'r')
no_laser_img_1 = np.loadtxt(no_laser_img_1, delimiter=",")

Array = []
Array = FindSameCell(img_0min, img_1, allowed_pixel)
Array = ConvertPixel(Array)
np.savetxt('Analysis_Result_No' + str(ExpNumber) + '_' + Color + '_' + str(ID) + '_No' + str(Treat_No) + '_' + str(Minute) + 'min_Array.csv', Array, delimiter=',', fmt="%s")
Array_sorted = DataSort(Array, threshold_3)
np.savetxt('Analysis_Result_No' + str(ExpNumber) + '_' + Color + '_' + str(ID) + '_No' + str(Treat_No) + '_' + str(Minute) + 'min.csv', Array_sorted, delimiter=',', fmt="%s")
