import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 100  # Carrier frequency in Hz
fm = 5    # Modulating frequency in Hz
Am = 1    # Modulating signal amplitude
Ac = 2    # Carrier amplitude
beta = 5  # Frequency deviation (modulation index)
t = np.linspace(0, 1, 1000)

# Modulating and FM signal
modulating_signal = Am * np.sin(2 * np.pi * fm * t)
fm_signal = Ac * np.sin(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, fm_signal, label="FM Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Frequency Modulated Signal")
plt.show()
