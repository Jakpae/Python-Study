# Homework 11.3
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 22, 2023

# 그래프 구현을 위한 seaborn 모듈 import
import seaborn as sns
# NaN 제거를 위한 pandas 모듈 import
import pandas  as pd
# 그래프 출력을 위한 matplotlib 모듈 import
import matplotlib.pyplot as plt

# 펭귄 데이터 세트를 Pandas 데이터 프레임 df_penguins으로 load
df_penguins = sns.load_dataset("penguins")

# df_penguins의 데이터 자료형을 확인 및 출력
print("\nSeaborn titanic before :\n", df_penguins)

# df_penguins에 포함된 NaN 데이터들을 dorpna() 메소드로 제거한 후 
df_penguins_NaN_deleted = df_penguins.dropna(axis=0)

# 펭귄 종류별,거주섬별,몸무게에 대한 Seaborn boxplot 출력
sns.boxplot(x="species", y="body_mass_g", hue="island", data=df_penguins_NaN_deleted)
# 그래프의 title "Penguins"로 설정
plt.title("Penguins")

# 그래프 보여주는 plt.show()
plt.show()