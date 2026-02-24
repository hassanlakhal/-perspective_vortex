import mne
import numpy as np

raw = mne.io.read_raw_edf("S001R01.edf", preload=True)
raw.filter(8, 30)
raw.rename_channels(lambda x: x.replace("..", ""))

sfreq = raw.info['sfreq']
window_size = int(2 * sfreq)

motor = raw.pick(["C3", "C4", "Cz"])

data = motor.get_data()


windows = []
step = window_size // 2
for start in range(0, data.shape[1] - window_size, step):
    stop = start + window_size
    chunk = data[:, start:stop]   # (3, window_size)
    windows.append(chunk)

windows = np.array(windows)

features = []

for chunk in windows:
    psd, freqs = mne.time_frequency.psd_array_welch(
        chunk,
        sfreq=sfreq,
        fmin=8,
        fmax=30,
        verbose=False
    )
    psd = np.log(psd + 1e-12)
    mu = psd[:, (freqs >= 8) & (freqs <= 12)].mean(axis=1)
    beta = psd[:, (freqs >= 13) & (freqs <= 30)].mean(axis=1)
    
    feat = np.concatenate([mu, beta])
    features.append(feat)

features = np.array(features)
features_norm = ((features - features.mean(axis=0)) / features.std(axis=0))
print(features_norm)