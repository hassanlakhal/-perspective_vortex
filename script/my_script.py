import mne
import matplotlib.pyplot as plt
# mne.sys_info()


file_path = "S001R01.edf"
mne.set_config('MNE_LOGGING_LEVEL', 'INFO', set_env=True)
raw = mne.io.read_raw_edf(file_path,preload=True)

print(raw.ch_names)
motor_channels = ["C3..", "C4..", "Cz.."]

raw_filtered = raw.copy().filter(l_freq=8, h_freq=30)
raw_motor = raw_filtered.copy().pick_channels(motor_channels)


raw.plot()
raw_motor.plot()
# print(raw_filtered.shape())
plt.show()