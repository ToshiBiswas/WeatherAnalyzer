import numpy as np

class WeatherAnalyzer:
    def __init__(self,List):
        self.list = List

    def GetMinTemp(self):
        condition = True #this function takes a list of the full array file, and returns the minimum temp
        #by appending all the minumum temperatures into an array and using the min function. NOTE this will only work
        #if you have defined all the values into its proper classes. use a loop
        for i in range(0,len(self.list)): 
            if condition == True:
                x = np.array(self.list[i].minTemperature)
                condition = False
            else:
                x = np.append(self.list[i].minTemperature,x)
            minimum = np.amin(x)
        return f"\nthe minimum is: {minimum}\n"

    def append(self, data): #this was something left after i attempted to try and test some of these things,
        #but you can use this to append a function like a regular array
        return np.append(self.list,data)

    def GetMaxTemp(self): #this uses the same concept like the min function except the end call our the maximum temperature

        condition = True
        index = 0
        for i in range(0,len(self.list)):
            if condition == True:
                x = np.array(self.list[i].maxTemperature)
                condition = False
            else:
                x = np.append(x,self.list[i].maxTemperature)
        return f"\nThe Maximum is: {np.amax(x)}\n"
    
    def GetMaxTempAnnually(self): 
        list2d = [] # Creates list
        for i in range(1990,2020): # Defines the range and program to look across the years 1990,2020
            condition = True # sets condition to true
            for j in range(0,len(self.list)): #sets j to read the file
                if self.list[j].MonthDate.year == i:
                    if condition == True:
                        array = np.array(self.list[j])
                        condition = False
                    else:
                        array = np.append(array,self.list[j])
            condition = True
            for j in range(0,len(array)):
                if condition == True:
                    x = np.array(array[j].maxTemperature)
                    condition = False
                else:
                    x = np.append(x,array[j].maxTemperature)
            maximum = np.amax(x)
            list2d.append([i,maximum])
        return list2d
    
    def GetMinTempAnnually(self): #same concept as the max, except it uses the amin function at the end
        list2d = []
        for i in range(1990,2020):
            condition = True
            for j in range(0,len(self.list)):
                if self.list[j].MonthDate.year == i:
                    if condition == True:
                        array = np.array(self.list[j])
                        condition = False
                    else:
                        array = np.append(array,self.list[j])
            condition = True
            for j in range(0,len(array)):
                if condition == True:
                    x = np.array(array[j].minTemperature)
                    condition = False
                else:
                    x = np.append(x,array[j].minTemperature)
            minimum = np.amin(x)
            list2d.append([i,minimum])
        return list2d

    def GetSnowfallAnnually(self): #similar concept, except it takes the snowfall, and it returns the average snowfall,and it does so in a 2D list
        list2d = []
        for i in range(1990,2020):
            condition = True
            for j in range(0,len(self.list)):
                if self.list[j].MonthDate.year == i:
                    if condition == True:
                        array = np.array(self.list[j])
                        condition = False
                    else:
                        array = np.append(array,self.list[j])
            condition = True
            for j in range(0,len(array)):
                if condition == True:
                    array2 = np.array(array[j].snowfall)
                    condition = False
                else:
                    array2 = np.append(array2,array[j].snowfall)
            list2d.append([i,np.average(array2)])
        return list2d

    def GetAvgTempAnnually(self):
        list2d =[]
        for i in range(1990,2020):
            condition = True
            for j in range(0,len(self.list)):
                if self.list[j].MonthDate.year == i:
                    if condition == True:
                        array = np.array(self.list[j])
                        condition = False
                    else:
                        array = np.append(array,self.list[j])
            condition = True
            for j in range(0,len(array)):
                if condition == True:
                    x = np.array(array[j].minTemperature)
                    condition = False
                else:
                    x = np.append(x,array[j].minTemperature)
            minimum = np.amin(x)
            condition = True
            for j in range(0,len(array)):
                if condition == True:
                    array3 = np.array(array[j].maxTemperature)
                    condition = False
                else:
                    array3 = np.append(array3,array[j].maxTemperature)
            maximum = np.amax(array3)
            Avg = (minimum + maximum)/2                       #the third part tajes the maximum and the minimum and adds them then divides it by 2
            list2d.append([i,Avg])
        return list2d         