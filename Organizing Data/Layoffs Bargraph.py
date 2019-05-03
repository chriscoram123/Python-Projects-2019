import matplotlib.pyplot as plt
import numpy as np

# 2D bar graph of rise of automation in a automotive factory in New York within
# a span of 5 years.
# Variables
N = 5
humanWorkers = (500, 450, 400, 350, 270)
human = (1, 2, 3, 4, 5)
ind = np.arange(N)
width = 0.65

# Plotting Variables
p1 = plt.bar(ind, humanWorkers, width, yerr=human)

# Name Placements
plt.title('Staff Layoffs In NY Automotive Plant, 2018')
plt.ylabel('Amount of Workers')
plt.xlabel('Months')
plt.xticks(ind, ('January','May','August','October','December'))
plt.yticks(np.arange(0, 500, 200))

plt.show()