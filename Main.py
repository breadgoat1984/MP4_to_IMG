
# Importing all necessary libraries
import time
import os
import cv2
import numpy as np

vid_file_path = r"C:\Users\User\Videos\4K Video Downloader\Task A - APC December 2022 - Accounting for the Big Ranch acquisition.mp4"
# Read the video from specified path
cam = cv2.VideoCapture(vid_file_path)
OLD_FRAME = './data/test.jpg'


def mse(img1, img2):
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse, diff


try:

    # creating a folder named data
    if not os.path.exists('./data'):
        os.makedirs('./data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while True:
    # Set the frame index what frame it should start looking from
    cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'

        # writing the extracted images
        cv2.imwrite(name, frame)
        print('Creating...' + name)
        # time.sleep(5)
        img1 = cv2.imread(OLD_FRAME)
        img2 = cv2.imread(name)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        error, diff = mse(img1, img2)
        # change the number below higher or lower depending on the results
        #  it can be a float.
        # this number sets the "sensitivity/difference tolerance"
        if error > 5:
            OLD_FRAME = name
        else:
            os.remove(name)
        # increasing counter so that it will
        # show how many frames are created
        # and also set search from 30 frames ahead.
        currentframe += 30

    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
