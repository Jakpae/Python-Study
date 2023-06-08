# Homework 13.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : June 7, 2023

# 필요한 라이브러리와 모듈을 Import
import os
import PIL
import cv2
import glob
import numpy as np
from tkinter import *
from PIL import Image, ImageDraw, ImageGrab

# 학습된 Keras 모델을 불러오는 Keras.models
from keras.models import load_model
# CNN_model_Digits 모델 Load
model = load_model("CNN_model_Digits")
model.summary()
print("Model is loaded successfully ...")

# Tkinter GUI 애플리케이션 설정
root = Tk()
root.resizable(0, 0)
root.title("Handwritten Digits Recognition GUI App")

# 변수를 초기화
lastx, lasty = None, None
image_number = 0

# 숫자를 그릴 수 있는 캔버스 생성
cv = Canvas(root, width=640, height=480, bg='white')
cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)

# 마우스 드래그 이벤트에 따라 캔버스에 선을 그리는 함수 Draw_lines
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=8, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

# 캔버스를 지우는 함수 Clear_Widget
def clear_widget():
    global cv
    cv.delete("all")

# 마우스 클릭 이벤트를 활성화하는 함수 Activate_event
def activate_event(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

# 숫자를 인식하고 확률을 표시하는 함수 Recognize_digit
def recognize_digit():
    global image_number
    predictions = []
    percentage = []
    
    # 캡처된 이미지의 파일명을 설정
    filename = f'image_{image_number}.png'
    widget = cv

    # 캔버스 위젯의 좌표를 가져오기
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    # 캔버스 숫자를 캡쳐하고 이미지를 저장
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
    # 색상 이미지를 로드
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 이진화를 적용
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # 경계선 찾기
    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # 숫자를 인식하고 화면에 표시하는 For반복문
    for cnt in contours:
        # 외각선을 그리기 위해 직사각형 좌표를 구함
        x, y, w, h = cv2.boundingRect(cnt)
        # 직사각형을 이미지 위에 그림
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
        # 이미지 경계를 만들기 위한 상한,하한,좌상,우상 값을 계산
        top = int(0.05 * th.shape[0])
        bottom = top
        left = int(0.05 * th.shape[1])
        right = left
        # 이미지 경계를 추가
        th_up = cv2.copyMakeBorder(th, top, bottom, left, right, cv2.BORDER_REPLICATE)
        # 위에서 구한 직사각형를 통해 ROI를 추출
        roi = th[y - top:y + h + bottom, x - left:x + w + right]
        # # 추출딘 영역의 크기를 조절하고 필요한 형태로 전환
        img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        img = img.reshape(1, 28, 28, 1)
        img = img / 255.0
        # 학습된 모델을 사용하여 에측값을 생성
        pred = model.predict([img])[0]
        final_pred = np.argmax(pred)
        # 최종 예측 결과를 표시
        data = str(final_pred) + ' ' + str(int(max(pred) * 100)) + '%'
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1
        cv2.putText(image, data, (x, y - 5), font, fontScale, color, thickness)

    # 결과를 화면에 표시
    cv2.imshow("image", image)
    cv2.waitKey(0)

# 마우스 클릭 이벤트를 연결
cv.bind('<Button-1>', activate_event)

# 버튼을 생성하고 배치
btn_save = Button(text="Recognize Digits", command = recognize_digit)
btn_save.grid(row=2, column=0, padx=1, pady=1)
btn_clear = Button(text="Clear widget", command = clear_widget)
btn_clear.grid(row=2, column=1, padx=1, pady=1)

# 애플리케이션을 실행
root.mainloop()