# -*- coding: utf-8 -*-


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as mlp
from sklearn.linear_model import LinearRegression

data= pd.read_csv("cost_revenue_clean.csv")
des_data= data.describe()
data["val"]=str
data["val"][0]="o"
print(data)

des_data

X= DataFrame(data, columns=["production_budget_usd"])
y= DataFrame(data, columns=["worldwide_gross_usd"])

mlp.figure(figsize=(10,6))
mlp.scatter(X,y)

mlp.ylim(0,3000000000)
mlp.xlim(0,450000000)
mlp.show()

regression = LinearRegression()
regression.fit(X,y)
regression.intercept_
regression.coef_

mlp.figure(figsize=(10,6))
mlp.scatter(X,y, alpha= 0.3)
mlp.plot(X, regression.predict(X), color= "red", linewidth=3)

mlp.ylim(0,3000000000)
mlp.xlim(0,450000000)
mlp.show()

data= pd.read_csv("lsd_math_score_data.csv")
print(data)

LSD= data[["LSD_ppm"]]
score=data[["Avg_Math_Test_Score"]]
time= data[["Time_Delay_in_Minutes"]]
mlp.plot( time,LSD, color= "#986D8E", linewidth= 4)
mlp.title=("Tissue concentration over time")
mlp.xlabel= "PPM"
mlp.ylabel= "minutes"
mlp.style.use("classic")

rgrn= LinearRegression()
rgrn.fit(LSD,score)
coef=rgrn.coef_[0][0]
intercept=rgrn.intercept_[0]
rgrn.score(LSD,score)
mlp.style.use("fivethirtyeight")
mlp.scatter(LSD,score, alpha= 0.7, color= 'blue',s=100)
predicted_score= rgrn.predict(LSD)
mlp.plot(LSD,predicted_score)
mlp.show()

data["Test_subject"]= "J.Lopez"
print(data)

clean_data= data[["Avg_Math_Test_Score", "LSD_ppm"]]

type(clean_data)

X= data[["LSD_ppm"]]
type(X)

del data["Time_Delay_in_Minutes"]
print(data)

import math
print(math.pi)
math.e



