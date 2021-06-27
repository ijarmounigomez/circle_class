# Matplotlib for the visualisation of the circle

import matplotlib.pyplot as plt
%matplotlib inline  

class circle (object):
  
  def __init__ (self, radius, color): #Constructor
    self.radius = radius;
    self.color = color;
  
  def drawCircle(self): #Draw method
    plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
    plt.axis('scaled')
    plt.show()  
  
# Example of the use! First of all, let's create a Green Circle object with a random radius and the green color:

green_circle = circle(24,'green')

# If we want to change the radius or the color for example, we could do the following:

green_circle.radius = 50
green_circle.color = 'red'

# Lastly, we will make use of our drawCircle function to print the circle:

green_circle.drawCircle()
