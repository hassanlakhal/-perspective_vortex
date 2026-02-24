import mne
import matplotlib.pyplot as plt
# mne.sys_info()


file_path = "S001R01.edf"
mne.set_config('MNE_LOGGING_LEVEL', 'INFO', set_env=True)
raw = mne.io.read_raw_edf(file_path,preload=True)

# print(raw.ch_names)

raw_filtered = raw.copy().filter(l_freq=8, h_freq=30)


raw.plot()
raw_filtered.plot()
# print(raw_filtered)

# data, times = raw_filtered.get_data(picks='C3..', return_times=True)
# plt.plot(times, data.T)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('EEG Channel C3')
plt.show()