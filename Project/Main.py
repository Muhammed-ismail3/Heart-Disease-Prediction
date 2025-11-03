import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("heart.csv")

# print(data.head())

# print("\n\n\n\n\n")

# print(data.info())




# print(data[["Age","RestBP","Chol","MaxHR","Oldpeak"]].describe())
# print(data.columns)

# print(len(data))

#print(data[data.isnull().any(axis=1)])
#print(data.isnull().any())

# print(data.duplicated().sum())

# print(data[data["Age"] == 62])

# print(data["Sex"].value_counts())

# print(data.groupby("Sex")["Age"].mean())

# print(data["ChestPain"].unique())

# print(data[data["Chol"] > 360])
# print(pd.crosstab(data["RestBP"] > 170,data["Target"]))

# print(pd.crosstab(data["Target"], data["Sex"]).loc[1].sum())

# print(data.groupby(["Age"]).mean(numeric_only=True))

##########################################
# data["RestBP"].hist(edgecolor='black')

# plt.boxplot(data["Chol"])

data = data.dropna()
data.isnull().sum()

# data[["Sex","Target"]].hist()

# data.plot( x='Sex', y='Target', kind='hist')

# data["RestBP"].hist()

data2 = data.drop(152, axis= 0)

# print(data[data["Chol"] > 360])

# print("\n-----------------------\n")
# print(data2[data2["Chol"] > 360])
# print("\n-----------------------\n")

# print(data2[data2["RestBP"]> 170])
# print(data2.isnull().sum())
# data2[["MaxHR","Oldpeak"]].hist(edgecolor = 'black')

# print(len(data2[(data2["Oldpeak"] > 2)]))

print(len(data2[data2["Oldpeak"]>= 4]))

# plt.boxplot(data2["Oldpeak"])

data2.to_csv("Data_Cleaned.csv")


plt.show()
