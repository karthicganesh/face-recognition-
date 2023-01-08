import os
import warnings
warnings.simplefilter('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.color import rgb2gray 
karthic = os.listdir("D:/python/karthic pic")
limit = 10
karthic = [None]*limit
j=0
for i in gopi:
    if (j<limit):
        karthic[j] = imread("D:/python/karthic pic/"+i)
        j += 1
    else:
        break
    imshow(karthic[20])
        