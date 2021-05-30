import matplotlib.pyplot as plt
import numpy as np
import math

n=7;
k=4;

x = np.linspace(1,n,n);
y1 = np.log2(x);
y2 = x;
y3 = np.power(x,2);
y4 = np.power(x,3);
y5 = np.power(x,k);

plt.plot(x, y1, color='k', label='O(logn)')
plt.plot(x, y2, color='g', label='O(n)')
plt.plot(x, y3, color='b', label='O(n^2)')
plt.plot(x, y4, color='y', label='O(n^3)')
plt.plot(x, y5, color='r', label='O(n^k)')
plt.legend(loc="upper right")
plt.xlim(1, 7.0)
plt.ylim(0, 20.0)
plt.xlabel('n')
plt.ylabel('Runtime')
plt.show()
