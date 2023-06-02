import pandas as pd

DaeGu_Temp = pd.read_csv("DaeguTemp_2013_2022_CSV.csv")
print("DaeGu_Temp = \n", DaeGu_Temp)
#Avg_DaeGu_Temp = DaeGu_Temp['Avg']
#print("Avg_DaeGu_Temp =")
#print(Avg_DaeGu_Temp)

print("DaeGu_Temp.describe() =")
print(DaeGu_Temp.describe())
DaeGu_Temp_highest = DaeGu_Temp['High'].max()
print("temp_DG_highest = ", DaeGu_Temp_highest)
DaeGu_Temp_lowest = DaeGu_Temp['Low'].min()
print("DaeGu_Temp_lowest = ", DaeGu_Temp_lowest)

DaeGu_Temp_highest_day = DaeGu_Temp[DaeGu_Temp.High >= DaeGu_Temp_highest]
print("DaeGu_Temp_highest_day = "); print(DaeGu_Temp_highest_day)

DaeGu_Temp_lowest_day = DaeGu_Temp[DaeGu_Temp.Low <= DaeGu_Temp_lowest]
print("DaeGu_Temp_lowest_day = "); print(DaeGu_Temp_lowest_day)