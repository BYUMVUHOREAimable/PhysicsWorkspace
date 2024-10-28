import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 100  # Carrier frequency in Hz
fm = 10   # Modulating frequency in Hz
Ac = 5    # Carrier amplitude
Am = 2    # Modulating amplitude
t = np.linspace(0, 1, 1000)

# Signals
carrier = Ac * np.sin(2 * np.pi * fc * t)
modulating = Am * np.sin(2 * np.pi * fm * t)
am_signal = (Ac + Am * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

# Plot
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, carrier, label="Carrier Signal")
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t, modulating, label="Modulating Signal", color="orange")
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, label="AM Signal", color="purple")
plt.legend()
plt.xlabel("Time")
plt.show()
