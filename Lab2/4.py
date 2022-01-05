# Problem 4
import pandas as pd
import matplotlib.pyplot as plt
print()

weatherData = pd.read_csv("weather_data.txt")

weatherData.plot(kind='line', y=['actual_min_temp', 'actual_max_temp'])
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.show()

print(weatherData.loc[:, "actual_precipitation"])
weatherData["actual_precipitation"].plot(kind='hist')
plt.xlabel("Actual Precipitation")
plt.ylabel("Frequency")

plt.show()