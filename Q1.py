#Q1

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('gapminder.csv')
dataset

year=dataset['year']
pop=dataset['population']
plt.xlabel('year')
plt.ylabel('population')
plt.plot(year,pop)
plt.show()

gdp_cap=dataset['gdp_cap']
life_exp=dataset['life_exp']
plt.xlabel('gdp_cap')
plt.ylabel('life_exp')
plt.scatter(gdp_cap,life_exp)
plt.show()


plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()

plt.hist(life_exp, bins=5)
plt.show()
plt.clf()
plt.hist(life_exp, bins=20)
plt.show()
plt.clf()


# Observation : Bins 20 contains better observations.

