
import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,28,15])
mylabels = ["Apples", "Banana", "Cherry", "Kiwi"]
mycolors = ["black", "yellow", "red", "green"]
myexplode = [0.2, 0, 0, 0]
plt.pie(x,
labels= mylabels,
startangle= 0,
shadow= False,
colors= mycolors,
explode= myexplode)

plt.legend(title = "Four Fruits: ")
plt.show()

