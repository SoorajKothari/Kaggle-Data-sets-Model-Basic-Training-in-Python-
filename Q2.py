#Q2

import pandas as pd
import numpy as np

my_dict = {"country":["United States","Australia","Japan","India","Russia","Morocco","Egypt"],
           "dr":[True,False,False,False,True,True,True],
           "cpc":[809,731,588,18,200,70,45]}

cars = pd.DataFrame(my_dict)
print(cars)

cars.index = ["US","AUS","JAP","IN","RU","MOR","EG"]
print(cars)


for index,row in cars.iterrows():
    if row["cpc"] > 500:
            print("Country: "+str(row["country"])+" => cpc "+str(row["cpc"]))




d = {}
#with and
for index,row in cars.iterrows():
    if np.logical_and(row["cpc"]>=100,row["cpc"] <= 500):
        print(row)
        d["cpc_with_And"] = row["cpc"]



