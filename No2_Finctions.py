import numpy as np
import cv2
from tqdm import tqdm


def ConvertPixel(array):
    new_array = []

    B0_1064 = 384.3
    B1_1064 = 0.1546
    B2_1064 = -0.0007934
    B3_1064 = 9.238*10**-7
    B4_1064 = -3.934*10**-10

    B0_1270 = 95.82
    B1_1270 = 0.02091
    B2_1270 = -4.679*10**-5

    for i in range(len(array)):
        x = 1250 * array[i][1]/742
        new_x = B0_1064 + B1_1064 * x + B2_1064 * x**2 + B3_1064 * x**3 + B4_1064 * x**4
        y = 1250 * array[i][0]/742
        new_y = B0_1270 + B1_1270 * y + B2_1270 * y**2
        new_array.append([new_x, new_y, array[i][2]])
    return new_array

def DataSort(array, threshold):
    global A1_x, A1_y, A2_x, A2_y, A3_x, A3_y, A4_x, A4_y, A5_x, A5_y, B1_x, B1_y, B2_x, B2_y, B3_x, B3_y, B4_y, B5_x, B5_y, C1_x, C1_y, C2_x, C2_y, C3_x, C4_y, C5_x, C5_y, D1_x, D1_y, D2_x, D2_y, D3_x, D4_y, D5_x, D5_y, E1_x, E1_y, E2_x, E2_y, E3_x, E4_y, E5_x, E5_y
    array_sorted = []
    length = len(array)
    for x in range(0, length):
        A1 = A2 = A3 = A4 = A5 = A6 = B1 = B2 = B3 = B4 = B5 = B6 = C1 = C2 = C3 = C4 = C5 = C6 = D1 = D2 = D3 = D4 = D5 = D6 = E1 = E2 = E3 = E4 = E5 = E6 = F1 = F2 = F3 = F4 = F5 = F6 = 0
        A1_x = A1_y = A2_x = A2_y = A3_x = A3_y = A4_x = A4_y = A5_x = A5_y = B1_x = B1_y = B2_x = B2_y = B3_x = B3_y = B4_x = B4_y = B5_x = B5_y = C1_x = C1_y = C2_x = C2_y = C3_x = C3_y = C4_x = C4_y = C5_x = C5_y = D1_x = D1_y = D2_x = D2_y = D3_x = D3_y = D4_x = D4_y = D5_x = D5_y = E1_x = E1_y = E2_x = E2_y = E3_x = E3_y = E4_x = E4_y = E5_x = E5_y = 0
        if array[x][0] == array[x-1][0] and array[x][1] == array[x-1][1]:
            continue
        else:
            if array[x][2] < threshold:
                if 250 + 30.0 * 4 < array[x][0] < 250 + 30.0 * 5 and 100 - 10 * 1 <= array[x][1] < 100 - 10 * 0:
                    A1 = array[x][2]
                    A1_x = array[x][0]
                    A1_y = array[x][1]
                elif 250 + 30.0 * 4 <= array[x][0] < 250 + 30.0 * 5 and 100 - 10 * 2 <= array[x][1] < 100 - 10 * 1:
                    A2 = array[x][2]
                    A2_x = array[x][0]
                    A2_y = array[x][1]
                elif 250 + 30.0 * 4 <= array[x][0] < 250 + 30.0 * 5 and 100 - 10 * 3 <= array[x][1] < 100 - 10 * 2:
                    A3 = array[x][2]
                    A3_x = array[x][0]
                    A3_y = array[x][1]
                elif 250 + 30.0 * 4 <= array[x][0] < 250 + 30.0 * 5 and 100 - 10 * 4 <= array[x][1] < 100 - 10 * 3:
                    A4 = array[x][2]
                    A4_x = array[x][0]
                    A4_y = array[x][1]
                elif 250 + 30.0 * 4 <= array[x][0] < 250 + 30.0 * 5 and 100 - 10 * 5 <= array[x][1] < 100 - 10 * 4:
                    A5 = array[x][2]
                    A5_x = array[x][0]
                    A5_y = array[x][1]
                elif 250 + 30.0 * 3 < array[x][0] < 250 + 30.0 * 4 and 100 - 10 * 1 <= array[x][1] < 100 - 10 * 0:
                    B1 = array[x][2]
                    B1_x = array[x][0]
                    B1_y = array[x][1]
                elif 250 + 30.0 * 3 <= array[x][0] < 250 + 30.0 * 4 and 100 - 10 * 2 <= array[x][1] < 100 - 10 * 1:
                    B2 = array[x][2]
                    B2_x = array[x][0]
                    B2_y = array[x][1]
                elif 250 + 30.0 * 3 <= array[x][0] < 250 + 30.0 * 4 and 100 - 10 * 3 <= array[x][1] < 100 - 10 * 2:
                    B3 = array[x][2]
                    B3_x = array[x][0]
                    B3_y = array[x][1]
                elif 250 + 30.0 * 3 <= array[x][0] < 250 + 30.0 * 4 and 100 - 10 * 4 <= array[x][1] < 100 - 10 * 3:
                    B4 = array[x][2]
                    B4_x = array[x][0]
                    B4_y = array[x][1]
                elif 250 + 30.0 * 3 <= array[x][0] < 250 + 30.0 * 4 and 100 - 10 * 5 <= array[x][1] < 100 - 10 * 4:
                    B5 = array[x][2]
                    B5_x = array[x][0]
                    B5_y = array[x][1]
                elif 250 + 30.0 * 2 < array[x][0] < 250 + 30.0 * 3 and 100 - 10 * 1 <= array[x][1] < 100 - 10 * 0:
                    C1 = array[x][2]
                    C1_x = array[x][0]
                    C1_y = array[x][1]
                elif 250 + 30.0 * 2 <= array[x][0] < 250 + 30.0 * 3 and 100 - 10 * 2 <= array[x][1] < 100 - 10 * 1:
                    C2 = array[x][2]
                    C2_x = array[x][0]
                    C2_y = array[x][1]
                elif 250 + 30.0 * 2 <= array[x][0] < 250 + 30.0 * 3 and 100 - 10 * 3 <= array[x][1] < 100 - 10 * 2:
                    C3 = array[x][2]
                    C3_x = array[x][0]
                    C3_y = array[x][1]
                elif 250 + 30.0 * 2 <= array[x][0] < 250 + 30.0 * 3 and 100 - 10 * 4 <= array[x][1] < 100 - 10 * 3:
                    C4 = array[x][2]
                    C4_x = array[x][0]
                    C4_y = array[x][1]
                elif 250 + 30.0 * 2 <= array[x][0] < 250 + 30.0 * 3 and 100 - 10 * 5 <= array[x][1] < 100 - 10 * 4:
                    C5 = array[x][2]
                    C5_x = array[x][0]
                    C5_y = array[x][1]
                elif 250 + 30.0 * 1 < array[x][0] < 250 + 30.0 * 2 and 100 - 10 * 1 <= array[x][1] < 100 - 10 * 0:
                    D1 = array[x][2]
                    D1_x = array[x][0]
                    D1_y = array[x][1]
                elif 250 + 30.0 * 1 <= array[x][0] < 250 + 30.0 * 2 and 100 - 10 * 2 <= array[x][1] < 100 - 10 * 1:
                    D2 = array[x][2]
                    D2_x = array[x][0]
                    D2_y = array[x][1]
                elif 250 + 30.0 * 1 <= array[x][0] < 250 + 30.0 * 2 and 100 - 10 * 3 <= array[x][1] < 100 - 10 * 2:
                    D3 = array[x][2]
                    D3_x = array[x][0]
                    D3_y = array[x][1]
                elif 250 + 30.0 * 1 <= array[x][0] < 250 + 30.0 * 2 and 100 - 10 * 4 <= array[x][1] < 100 - 10 * 3:
                    D4 = array[x][2]
                    D4_x = array[x][0]
                    D4_y = array[x][1]
                elif 250 + 30.0 * 1 <= array[x][0] < 250 + 30.0 * 2 and 100 - 10 * 5 <= array[x][1] < 100 - 10 * 4:
                    D5 = array[x][2]
                    D5_x = array[x][0]
                    D5_y = array[x][1]
                elif 250 + 30.0 * 0 < array[x][0] < 250 + 30.0 * 1 and 100 - 10 * 1 <= array[x][1] < 100 - 10 * 0:
                    E1 = array[x][2]
                    E1_x = array[x][0]
                    E1_y = array[x][1]
                elif 250 + 30.0 * 0 <= array[x][0] < 250 + 30.0 * 1 and 100 - 10 * 2 <= array[x][1] < 100 - 10 * 1:
                    E2 = array[x][2]
                    E2_x = array[x][0]
                    E2_y = array[x][1]
                elif 250 + 30.0 * 0 <= array[x][0] < 250 + 30.0 * 1 and 100 - 10 * 3 <= array[x][1] < 100 - 10 * 2:
                    E3 = array[x][2]
                    E3_x = array[x][0]
                    E3_y = array[x][1]
                elif 250 + 30.0 * 0 <= array[x][0] < 250 + 30.0 * 1 and 100 - 10 * 4 <= array[x][1] < 100 - 10 * 3:
                    E4 = array[x][2]
                    E4_x = array[x][0]
                    E4_y = array[x][1]
                elif 250 + 30.0 * 0 <= array[x][0] < 250 + 30.0 * 1 and 100 - 10 * 5 <= array[x][1] < 100 - 10 * 4:
                    E5 = array[x][2]
                    E5_x = array[x][0]
                    E5_y = array[x][1]
                else:
                    print('error')
                array_sorted.append([A3_x, A3_y, A3, B3_x, B3_y, B3, C3_x, C3_y, C3, D3_x, D3_y, D3, E3_x, E3_y, E3, A4_x, A4_y, A4, B4_x, B4_y, B4, C4_x, C4_y, C4, D4_x, D4_y, D4, E4_x, E4_y, E4, A5_x, A5_y, A5, B5_x, B5_y, B5, C5_x, C5_y, C5, D5_x, D5_y, D5, E5_x, E5_y, E5])
    return array_sorted
