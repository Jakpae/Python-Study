import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# x 값을 생성하고, 1D 배열을 2D 배열로 변경
x = np.linspace(-50.0, 50.0, 100)
x = x.reshape(-1, 1)

# x에 대한 이차식 y 값을 생성
y = x**2 - 10*x - 200

# noise를 생성하고 y에 값 추가
mu, sigma = 0.0, 100.0
noise = np.random.normal(mu, sigma, x.size)
y_noise = y + noise.reshape(-1, 1)

# PolynomialFeatures 객체 생성하여 x 데이터를 다항식 형태로 변환
poly_features = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly_features.fit_transform(x)

# 선형 회귀 모델(LinearRegression) 생성 및 학습
lr = LinearRegression()
lr.fit(x_poly, y_noise)

# 학습된 모델로 y 예측
y_pred = lr.predict(x_poly)

# 그래프 그리기
plt.scatter(x, y_noise, color='black', label='y_noise', s=3) # y_noise를 검은색 작은 점으로 표시
plt.plot(x, y_pred, color='red', linewidth=1, label='y_pred') # y_pred 값들을 빨간색 선으로 표시
plt.title('y_nose = +1.00*x**2 - 10.00*x - 200.00 + noise') # 타이틀 설정
plt.xlabel('x') # x축 레이블 설정
plt.ylabel('y') # y축 레이블 설정
plt.legend(loc="best") # 범례 설정
plt.grid(True) # 그래프 격자 표시
plt.show() # 그래프 표시










