import numpy as np
import pandas as pd

#creating the list using the dic, list, array
labels=['hello','Welcome',"Goodmorning","po"]
dic1={"day1":430,"day2":560,"day3":670}

arr=np.array([1,2,34,5])
ser1=pd.Series(dic1)
print(ser1)

ser2=pd.Series([1,2,3,4],['usa','america','rome','calicut'])
print(ser2)

ser3=pd.Series([1,2,3,4],['usa','calicut','paris','america'])
print(ser3)

print(ser2+ser3)
print(ser2[0])
