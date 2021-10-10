import numpy as np
class FileIO:
    def __init__(self,file): #iniates the differet variables when called such that when a file name is input class will instantly read the different data
        self.File = file
        self.data = np.array(self.read_weather())
    
    def read_weather(self): 
        self.Data = np.loadtxt(self.File , delimiter = ',', skiprows =1, usecols=(0,1,2,3,4), dtype=np.float)
        return self.Data 
