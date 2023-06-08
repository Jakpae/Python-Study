import os, os.path
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D
kr_utils = tf.keras.utils
from keras import backend as k
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt

MNIST_npz_path = "/Users/leeseungjun/Library/CloudStorage/GoogleDrive-jfldjd@yu.ac.kr/내 드라이브/공부/소프트웨어/과제/MyPyPackage/MNIST/mnist.npz" # put mnist.npz file at C:\MNIST\mnist.npz
#load dataset directly from keras library
print("Loading MNIST data (MNIST_npz_path = {}) . . . .".format(MNIST_npz_path))
(X_train, y_train), (X_test, y_test) = mnist.load_data(path = MNIST_npz_path)
print("Loading mnist.npz is completed now !!")


# reshape format [samples][width][height][channels]
print("Reshaping format . . . .")
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')
# Converts a class vector (integer) to binary class matrix print("Converting class vector . . . .")
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)
# normalize inputs X_train = X_train / 255 X_test = X_test / 255
print("Preparing a CNN model . . . .")
# define a CNN model (Convolutional Neural Network)
num_classes = 10
model = Sequential([
    Conv2D(32, kernel_size= (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')])

print("Compiling the model . . . .")
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


print("Fitting the model . . . .")
# fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=2)
print("The model has successfully trained")
# print summary of the model and save the model model.summary() #model.save("CNN_model_Digits")
#print("The model has successfully saved !!")
# evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("CNN error: %.2f%%"%(100 - scores[1]*100))

#============ stage 2 ======================== import cv2
from tkinter import *
from PIL import Image, ImageDraw, ImageGrab

print("\n========================================")
print("Stage 2 : Handwritten digit recognition with tkinter GUI") # create a main window first (named as root)
root = Tk()
root.resizable(0, 0)
root.title("Handwritten Digits Recognition GUI App")
# Initialize variables lastx,
lasty = None, None
image_number = 0

# Create a canvas for drawing digits
cv = Canvas(root, width=640, height=480, bg='white')
cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=8, fill='black',
                   capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y
def clear_widget():
    global cv
    cv.delete("all")
def activate_event(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y
def recognize_digit():
    global image_number
    predictions = []
    percentage = []
    #image_number = 0
    filename = f'image_{image_number}.png'
    widget = cv

    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    # grab the image, crop it
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

    # read the image in color format
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    # convert the image in grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # applying 0tsu thresholding
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # findContour() function helps in extracting the contours from the image
    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in contours:
        # get bounding box and extract ROI
        x, y, w, h = cv2.boundingRect(cnt)
        # create rectange
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
        top = int(0.05 * th.shape[0])
        bottom = top
        left = int(0.05 * th.shape[1])
        right = left
        th_up = cv2.copyMakeBorder(th, top, bottom, left, right, cv2.BORDER_REPLICATE)  # extract the image ROI
        roi = th[y - top:y + h + bottom, x - left:x + w + right]
        # resize roi image to 28x28 pixels
        img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        # reshaping the image to support our model input
        img = img.reshape(1, 28, 28, 1)
        # normalizing the image
        img = img / 255.0
        pred = model.predict([img])[0]
        final_pred = np.argmax(pred)
        data = str(final_pred) + ' ' + str(int(max(pred) * 100)) + '%'
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1
        cv2.putText(image, data, (x, y - 5), font, fontScale, color, thickness)

    cv2.imshow("image", image)
    cv2.waitKey(0)

# Tkinter
cv.bind('<Button-1>', activate_event)
# Add buttons and labels
btn_save = Button(text="Recognize Digits", command = recognize_digit)
btn_save.grid(row=2, column=0, padx=1, pady=1)
btn_clear = Button(text="Clear widget", command = clear_widget)
btn_clear.grid(row=2, column=1, padx=1, pady=1)

# mainloop()
root.mainloop()