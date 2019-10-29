import numpy as np
import cv2
import tqdm

def FindCenter(img_gauss, img_raw, threshold, kernel):
    array = []
    for x in range(kernel, img_gauss.shape[0]-kernel):
        for y in range(kernel, img_gauss.shape[1]-kernel):
            if threshold <= img_gauss[x, y] < 4095 and img_gauss[x, y] == np.max(img_gauss[x - kernel:x + kernel, y - kernel:y + kernel]):
                array.append([x, y, img_raw[x, y]])
    return array

def FindSameCell(array_0min, array_1min, pixel):
    array = []
    adjust = 1.0
    array_0 = array_0min
    array_1 = array_1min
    len_0 = array_0.shape[0]
    len_1 = array_1.shape[0]
    for x_0 in tqdm(range(0, len_0)):
        for x_1 in range(0, len_1):
            if array_1[x_1, 0] - 1 * pixel <= array_0[x_0, 0] <= array_1[x_1, 0] + 1 * pixel and array_1[x_1, 1] - 1 * pixel <= array_0[x_0, 1] <= array_1[x_1, 1] + 1 * pixel:
                if 0.7 < array_1[x_1, 2] * adjust / array_0[x_0, 2] < 1.3:
                    array.append([array_0[x_0, 0], array_0[x_0, 1], array_1[x_1, 2] * adjust / array_0[x_0, 2]])
    array = np.array(array)
    return array
