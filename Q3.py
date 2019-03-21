#Q3
import pandas as pd
europe= {'spain':'madrid', 'france':'paris', 'germany':'bonn',
         'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }


for key,value in europe.items():
    print("The Capital of "+str(key)+" is "+str(value))



my_dict = {"country":["United States","Australia","Japan","India","Russia","Morocco","Egypt"],
           "drives_right":[True,False,False,False,True,True,True],
           "cars_per_cap":[809,731,588,18,200,70,45]}

cars = pd.DataFrame(my_dict)

for label,row in cars.iterrows():
    print(label)
    print(row)    