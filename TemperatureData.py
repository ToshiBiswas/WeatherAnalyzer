from Date import date
import numpy as np
class Data: # Creates a TemperatureData class when called
    def __init__(self, year, Month, maxTemperature, minTemperature, snowfall):
        self.MonthDate = date(Month,year)
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature
        self.snowfall = snowfall        