import glob
import cv2
import numpy as np
from PIL import Image
import splitfolders
import cv2
# read the image file of Normal (negative)
file = r'"C:\Users\mosaa\PycharmProjects\machine2\Dataset\Negative\*.jpg'
path_copy_Negative = 'C:\\Users\\mosaa\PycharmProjects\\machine2\data\\NegatibeBirized\\'
im_bin_negative =[]
i =0
thresh = 120
maxval = 255
for fn in glob.glob(file):
    iml = Image.open(fn)
    im_gray = np.array(Image.open(fn).convert('L'))
    i+=1
    im_bin = (im_gray > thresh) * maxval
    Image.fromarray(np.uint8(im_bin)).save(path_copy_Negative+f'bin{i}.jpg')

i=0
file = r'C:\Users\mosaa\PycharmProjects\machine2\Dataset\Positive\*.jpg'
path_copy_Positive ='C:\\Users\\mosaa\PycharmProjects\\machine2\data\\PositiveBinrized\\'
for fn in glob.glob(file):
    iml = Image.open(fn)
    im_gray = np.array(Image.open(fn).convert('L'))
    i+=1
    im_bin = (im_gray > thresh) * maxval
    Image.fromarray(np.uint8(im_bin)).save(path_copy_Positive+f'bin{i}.jpg')


input_folder = 'data/'

splitfolders.ratio(input_folder,output="images",
                   seed=3,ratio=(0.8,0.0,0.2),group_prefix=None)





