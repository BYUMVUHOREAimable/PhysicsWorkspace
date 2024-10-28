

import numpy as np
import matplotlib.pyplot as plt

# Define the x values (e.g., 0 to 0.1 in small steps)
x = np.linspace(0, 0.1, 500)

# Define the signals
y1 = 2 * np.sin(100 * x)
y2 = 4 * np.sin(100 * x + np.pi)

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label=r'$y_1 = 2\sin(100x)$')
plt.plot(x, y2, label=r'$y_2 = 4\sin(100x + \pi)$')
plt.title("Signals $y_1$ and $y_2$")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
