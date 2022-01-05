# Problem 3
import pandas as pd
print()

weatherData = pd.read_csv("weather_data.txt")

print("max actual_precipitation: %s" % weatherData.actual_precipitation.max())
condition = (weatherData.actual_precipitation == weatherData.actual_precipitation.max())
print(weatherData.loc[condition, "actual_precipitation"])
print("date of highest actual_precipitation: %s" % weatherData.loc[292, "date"])

print()

bounds = weatherData.loc[0:30, "actual_max_temp"]
print(weatherData.loc[0:30, "actual_max_temp"])
print("min temp: %d" % bounds.min())
print("max temp: %d" % bounds.max())
average = ( bounds.min() + bounds.max() ) / 2
print("average temp: %d" % average)

print()

print("actual max temp: %s" % weatherData.actual_max_temp.max())
print("record max temp: %s" % weatherData.record_max_temp.max())
condition = (weatherData.actual_max_temp == weatherData.actual_max_temp.max())
print(weatherData.loc[condition, "actual_max_temp"])
print("There are 0 days where 'actual_max_temp == record_max_temp'")

print()

print(weatherData.loc[92:122, "actual_precipitation"])
summedPrecip = sum( weatherData.loc[92:122, "actual_precipitation"] )
# print(weatherData.loc[92:122, "date"])
print("Total rain in October 2014: %s" % summedPrecip)

print()

bounds = (weatherData.actual_min_temp < 60) & (weatherData.actual_max_temp > 90)
print(weatherData.loc[bounds, "date"])