# import matplotlib.pyplot as  plt
# year = [1950, 1970, 1980, 2000, 2010]
# pop = [2.5, 3.5, 4.5, 5.5, 7.2]

# plt.plot(year, pop)
# plt.show()

# import matplotlib
# print(matplotlib.__version__)  # 3.5.3


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)    # By defaul the plot()
# plt.show()                    # function draws a line from point to point.

# Ploting without line 
# string notation parameter '0'


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# Marker 

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([3, 8, 1, 10])
# ypoints = np.array([8, 3, 2, 1])
# plt.plot(xpoints, ypoints, 'o-.g', mec = 'r', ms = 20, mfc = 'g' )
# plt.show()


# Create labels by xlabel() and ylabel() for both axis

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y, 'o:', ms = 20, mfc = 'r', mec = 'g')

# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.title("Sports Watch Data")

# plt.show()

# Set Font Properties for titles and labels by fontdict
# loc parameter for position change(left, right, center(default))
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y, 'o:', ms = 20, mfc = 'r', mec = 'g')

# font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
# font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# plt.xlabel("Average Pulse", fontdict= font2)
# plt.ylabel("Calorie Burnage", fontdict= font2)
# plt.title("Sports Watch Data", fontdict= font1, loc= 'left')

# plt.show()

# Adding Grid lines in plot

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y, 'o:', ms = 20, mfc = 'r', mec = 'g')

# font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
# font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# plt.xlabel("Average Pulse", fontdict= font2)
# plt.ylabel("Calorie Burnage", fontdict= font2)
# plt.title("Sports Watch Data", fontdict= font1, loc= 'left')

# plt.grid()
# plt.show()


# Properties changes in Grid line

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.xlabel("Average Pulse", fontdict= font2)
plt.ylabel("Calorie Burnage", fontdict= font2)
plt.title("Sports Watch Data", fontdict= font1, loc= 'left')

plt.grid(color= 'green', linestyle= '--', linewidth= 0.5)
plt.show()



