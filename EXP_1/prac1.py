# pratik khandve B-18

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.tanh(x)                   # using tanh function 

plt.plot(x, y)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()


x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))       # 1/(1+e(-x))

plt.plot(x, y)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.exp(x-np.max(x))

plt.plot(x, y)
plt.title("SoftMax Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()



x = np.linspace(-10, 10, 100)
y = np.tanh(x)                   # using tanh function 

plt.plot(x, y)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()

