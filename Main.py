import numpy as np
from Date import date
from FileIO import FileIO
from TemperatureData import Data
from WeatherAnalyzer import WeatherAnalyzer
from Chart import Chart

def create_string(array):
    string = ""
    for i in range(0,len(array)):
        string = string + f"{array[i][0]}: {array[i][1]}\n"
    print(string)
    return string

def call_class(FileData):
    condition = True
    for i in range(0,len(FileData.data)):
        classdata = Data(FileData.Data[i,0],FileData.Data[i,1],FileData.Data[i,2],FileData.Data[i,3],FileData.Data[i,4])
        if condition == True:
            dataarray = np.array(classdata)
            condition = False
        else:
            dataarray = np.append(dataarray,classdata)
    dataarray = WeatherAnalyzer(dataarray)
    return dataarray

def Chart_Data_Y(array):
    y = []
    for i in range(0,len(array)):
        y.append(array[i][1])
    return y

def Chart_Data_X(array):
    x = []
    for i in range(0,len(array)):
        x.append(array[i][0])
    return x

def Create_Line_Chart(x, y, title):
    LineChart = Chart(x, y, title)
    LineChart.drawLineChart()

def Create_Bar_Chart_S(x, y,  title):
    BarChart = Chart(x, y, title)
    BarChart.drawBarChartSnow()

def Create_Bar_Chart_T(x, y,  title):
    BarChart = Chart(x, y, title)
    BarChart.drawBarChartTemperature()

def main_menu():
    print("1 - Get Minimum Temperature from 1990-2019")
    print("2 - Get Maximum Temperature from 1990-2019")
    print("3 - Get Annual Minimum temperature from 1990-2019")
    print("4 - Get Annual Maximum Temperature from 1990-2019")
    print("5 - Get Average snowfall from 1990-2019")
    print("6 - Get Annual Average temperature from 1990-2019")
    print("7 - LineChart Minimum Temperature of 1990-2019 Annually")
    print("8 - LineChart Maximum Temperature of 1990-2019 Annually")
    print("9 - BarChart Average Snowfall between 1990-2019 Annually")
    print("10 - BarChart Average Temperature between 1990-2019 Annually")
    print("11 - Exit")
    number = input("Enter a number: ")
    return number

def main_actions(FileData):
    number = "11"
    
    while True:
        number = main_menu()
        if number == "11":
            continuecommand = input("Goodbye! Press enter to Exit.")
            break
        elif number == "1":
            print(FileData.GetMinTemp())
        elif number == "2":
            print(FileData.GetMaxTemp())
        elif number == "3":
            create_string(FileData.GetMinTempAnnually())
        elif number == "4":
            create_string(FileData.GetMaxTempAnnually())
        elif number == "5":
            create_string(FileData.GetSnowfallAnnually())
        elif number == "6":
            create_string(FileData.GetAvgTempAnnually())
        elif number == "7":
            Create_Line_Chart(Chart_Data_X(FileData.GetMinTempAnnually()), Chart_Data_Y(FileData.GetMinTempAnnually()), 'Minimum Temperature between 1990-2019 Annually')
        elif number == "8":
            Create_Line_Chart(Chart_Data_X(FileData.GetMaxTempAnnually()), Chart_Data_Y(FileData.GetMaxTempAnnually()), 'Maximum Temperature between 1990-2019 Annually')
        elif number == "9":
            Create_Bar_Chart_S(Chart_Data_X(FileData.GetSnowfallAnnually()), Chart_Data_Y(FileData.GetSnowfallAnnually()), 'Average SnowFall between 1990-2019 Annually')
        elif number == "10":
            Create_Bar_Chart_T(Chart_Data_X(FileData.GetAvgTempAnnually()), Chart_Data_Y(FileData.GetAvgTempAnnually()), 'Average Temperature between 1990-2019 Annually')
        elif number == "":
            print("No Entry Detected. Please Enter a valid number")
        else:
            print("Invalid Number. Please Enter a valid number.")
        continuecommand = input("press enter to continue.")
def main():
    FileData = FileIO("CalgaryWeather.csv")
    classdata = call_class(FileData)
    main_actions(classdata)

if __name__ == "__main__":
    main()
