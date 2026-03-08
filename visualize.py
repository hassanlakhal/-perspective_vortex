from src.preprocessing import load_and_filter
import matplotlib.pyplot as plt

# 1. Load data
epochs, raw = load_and_filter(1, 4)

# 2. Visualize Signal
raw.plot(n_channels=10, title="Filtered EEG (8-30Hz)")


# 3. Visualize Power Spectral Density
raw.compute_psd().plot()
plt.show()