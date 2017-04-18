import csv
import pandas as pd
import cv2
import os
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Dropout
from keras.layers.convolutional import Convolution2D, Cropping2D
from keras.optimizers import Adam
import h5py
import numpy as np

lines = []
with open('/Users/omarfaroque/Desktop/data/driving_log.csv') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		#print (line)
		lines.append(line)
print (len(lines))

images = []
measurements = []
for line in lines:
	sourch_path = line[0]
	filename = sourch_path.split('/')[-1]
	current_path = '/Users/omarfaroque/Desktop/data/IMG/'+filename
	image = cv2.imread(current_path)
	images.append(image)
	measurement = float(line[3])
	measurements.append(measurement)

X_train = np.array(images)
y_train = np.array(measurements)

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160,320,3)))
print(model.output_shape)

model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
model.add(Dropout(0.2))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Dropout(0.2))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Dropout(0.2))


model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')


model.fit(X_train, y_train, validation_split=0.2,shuffle=True,nb_epoch=5)



model.save('model.h5')
