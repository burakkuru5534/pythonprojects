import matplotlib.pyplot as plt
import numpy as np
 
def kareAl(x):
    return x * x
 
x=np.linspace(-2, 2, 10)
 
plt.plot(x, kareAl(x))
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')
plt.ylim([0, 3])
plt.show()
