import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([8, 4, 1 ,5])

plt.plot(y1, label='garis 1')
plt.plot(y2, label='garis 2')
plt.plot(y3, label='garis 3')

plt.title('Plot Dua Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()