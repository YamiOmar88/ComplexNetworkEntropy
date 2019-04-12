# Lorenz Curve
# Author: Yamila M. Omar
# Date: 10/4/2019

class LorenzCurve:
    def __init__(self, property):
        '''Determines the x and y values of the Lorenz Curve 
        of a given property. Input values:
        - property: dictionary.'''
        self._calculate_x(property)
        self._calculate_y(property)
        
    def _calculate_x(self, property):
        '''Calculate the x ticks for the Lorenz Curve of property.'''
        number_x_ticks = len(property.keys()) + 1
        self.x = [i/(number_x_ticks-1) for i in range(number_x_ticks)]
        
    def _calculate_y(self, property):
        '''Calculate the y ticks for the Lorenz Curve of property.'''
        property_values = list(property.values())
        property_values.sort()
    
        cumulative = 0
        total = sum(property_values)
        self.y = [0]
        for value in property_values:
            cumulative = cumulative + value 
            self.y.append( cumulative / total )
            
    @property
    def gini(self):
        '''Calculate the Gini coefficient of the Lorenz curve.'''
        areaB = 0
        for index in range(len(self.x) - 1):
            areaB += (self.x[index+1] - self.x[index]) * 0.5*(self.y[index]+self.y[index+1])
        gini = 1 - 2 * areaB
        return gini
    

# Auxiliary function to plot multiple Lorenz Curves
# =================================================
def plot(curves, curve_names, y_label, file_name):
    ''' LorenzCurvePlot plots and saves the Lorenz curve(s). Variables:
    - curves: list of tuples (x,y,c) containing all curves (x,y) and the color c,
    - curve_names: names of those curves in the same order as the list,
    - y_label: string. percentage of cumulative sum of what?
    - file_name: name of file where to save the plot.'''
    import matplotlib.pyplot as plt
    
    # Plot line at 45 degrees
    x = curves[0][0]
    plt.plot(x,x,'--k', lw=2)
    plt.xlim(0,1)
    plt.ylim(0,1)
    
    # Plot al other curves
    for (x,y,c) in curves:
        plt.plot(x, y, marker='o', color=c, markersize=2, linewidth=2)
    plt.xlabel('fraction of nodes')
    yL = 'fraction of cumulative sum of ' + y_label + ' values'
    plt.ylabel(yL)
    plt.legend([''] + curve_names, loc=2)
    file_name = file_name + '.pdf'
    plt.savefig(file_name)