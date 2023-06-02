# Homework 11.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 21, 2023

import numpy as np
import matplotlib.pyplot as plt

# 평균과 표준편차를 인수로 전달받아 x,mu,sigma에 대한 정규분포 값을 계산하여 배열/리스트 Y를 생성하여 반환하여 주는 함수 gauss
def gauss(mu, sigma, x):
    y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((x - mu)**2)/(2*sigma**2)) 
    return y

# 메인 함수 생성
def main():
    # menu값 입력받기
    menu = input("menu를 입력해주세요 = ")
    
    # 만약 menu가 1이라면 실행
    if menu == '1':
        
        # NumPy의 linespace를 사용해서 x 구하기
        mu, sigma = 0, 2
        x = np.linspace(-4*sigma, 4*sigma, num=101)

        # mu = 0 일떄 sigma = 0.5에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = 0, 0.5
        y3 = gauss(mu, sigma, x)
        plt.plot(x, y3, color="red", label="sigma=0.5")

        # mu = 0 일떄 sigma = 1에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = 0, 1
        y2 = gauss(mu, sigma, x)
        plt.plot(x, y2, color="blue", label="sigma=1")

        # mu = 0 일떄 sigma = 2에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = 0, 2
        y1 = gauss(mu, sigma, x)
        plt.plot(x, y1, color="green", label="sigma=2")
        
        # 그래프 타이틀 "Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]" 로 설정
        plt.title("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")

        plt.legend(loc="best")
        plt.grid(True)
        # 그래프 보여주기
        plt.show()

    if menu == '2':
        
        # NumPy의 linespace를 사용해서 x 구하기
        mu, sigma = 1, 2.0
        x = np.linspace(-4*sigma, 4*sigma, num=101)

        # sigma = 1.0일떄 mu = -2.0에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = -2.0, 1.0
        y3 = gauss(mu, sigma, x)
        plt.plot(x, y3, color="red", label="mu=-2.0")

        # sigma = 1.0일떄 mu = 0에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = 0, 1.0
        y2 = gauss(mu, sigma, x)
        plt.plot(x, y2, color="blue", label="mu=0.0")

        # sigma = 1.0일떄 mu = 2.0에 대하여 guass를 사용하여 정규 분포 그래프를 Matplotlib를 사용하여 그래프로 표현
        mu, sigma = 2.0, 1.0
        y1 = gauss(mu, sigma, x)
        plt.plot(x, y1, color="green", label="mu=2.0")

        # 그래프 타이틀 "Normal Distribution Graph 2 : mu = [-2.0, 0.0, 2.0], sigma = 1.0" 로 설정
        plt.title("Normal Distribution Graph 2 : mu = [-2.0, 0.0, 2.0], sigma = 1.0")

        plt.legend(loc="best")
        plt.grid(True)
        # 그래프 보여주기
        plt.show()

# 만약 __name__이 __main__ 이라면 실행
if __name__ == "__main__":
    main()