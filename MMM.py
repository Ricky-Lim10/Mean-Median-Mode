import statistics
import pandas as pd

df=pd.read_csv("SOCR-HeightWeight.csv")
data=df["Height(Inches)"].tolist()
data=df["Weight(Pounds)"].tolist()

mean=sum(data)/len(data)
median=statistics.median(data)
mode=statistics.mode(data)

print("The mean is:", mean)
print("The median is:",median)
print("The mode is:", mode)



