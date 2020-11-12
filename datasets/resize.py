import os
import glob
import cv2

PATH = "./masular/train_A/"

paths = glob.glob(os.path.join(PATH, "*.png"))

for path in paths:
    img = cv2.imread(path);
    res = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path, res)
    print(path)