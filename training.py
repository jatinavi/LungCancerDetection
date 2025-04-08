import cv2
import numpy as np
import pandas as pd
from glob import glob
from sklearn.model_selection import train_test_split

IMG_SIZE = 256
SPLIT = 0.2
EPOCHS = 10
BATCH_SIZE = 64

path = "path_to_dataset_folder"  # <- update this with the actual path
classes = ['class1', 'class2']   # <- replace with actual class names like ['benign', 'malignant']

X = []
Y = []

for i, cat in enumerate(classes):
    images = glob(f'{path}/{cat}/*.jpeg')
    
    for image in images:
        img = cv2.imread(image)
        if img is not None:
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            X.append(img)
            Y.append(i)

X = np.asarray(X)
one_hot_encoded_Y = pd.get_dummies(Y).values

X_train, X_val, Y_train, Y_val = train_test_split(X, one_hot_encoded_Y,
                                                  test_size=SPLIT,
                                                  random_state=2022)

print(X_train.shape, X_val.shape)
