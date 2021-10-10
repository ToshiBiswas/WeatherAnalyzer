import numpy as np
import matplotlib.pyplot as pyplot

class Chart():
    def __init__(self, x, y, title): #, title, xlabel, ylabel)#
        self.x = x
        self.y = y
        self.title = title

    def drawLineChart(self):
        
        pyplot.figure()
        pyplot.title(self.title)
        pyplot.ylabel('Temperature')
        pyplot.xlabel('Years')

        pyplot.plot(self.x, self.y, marker='o')
        pyplot.show()

    def drawBarChartSnow(self):
        
        Years = self.x
        performance = self.y

        pyplot.bar(Years, performance, align='center') # The following can be used for a lighter blue #, alpha=0.5
        pyplot.xlabel('Years')
        pyplot.ylabel('SnowFall')
        pyplot.title(self.title)
    
        pyplot.show()

    def drawBarChartTemperature(self):
        
        Years = self.x
        performance = self.y

        pyplot.bar(Years, performance, align='center') #, alpha=0.5
        pyplot.xlabel('Years')
        pyplot.ylabel('Temperature')
        pyplot.title(self.title)
    
        pyplot.show()