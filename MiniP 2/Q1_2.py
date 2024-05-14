import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2,2,0.01)

f = np.zeros_like(x)

num = range(0,6)
for j in num:
    alpha = j
    for i in range(len(f)):

        if x[i] >= 0:
            f[i] = x[i]
        elif x[i] < 0 :
            f[i] = alpha * (np.exp(x[i]) - 1)
    df = np.gradient(f)

    # Plot
    plt.subplot(len(num),2,2*(j+1)-1)
    plt.plot(x, f, linewidth=2)
    plt.title(f'alpha = {alpha}')
    plt.subplot(len(num),2,2*(j+1))
    plt.plot(x, df, linewidth=2)
    plt.subplots_adjust(hspace=1)


plt.show()