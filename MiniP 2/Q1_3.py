import numpy as np
import matplotlib.pyplot as plt

# Defining input
t = np.arange(0,4,.1)

# Equation of lines
y1 = -2*t + 6 
y2 = np.zeros_like(t)
y3 = 2*t - 2

# Plotting the lines
plt.figure(figsize=(8,8))
plt.plot(t,y1, label = 'y + 2x -6 = 0')
plt.plot(t,y2, label = 'y = 0 ')
plt.plot(t,y3, label = 'y -2x + 2 = 0')
plt.ylim([-1,3])
plt.xlim([0,4])
plt.legend()
plt.grid()
plt.show()