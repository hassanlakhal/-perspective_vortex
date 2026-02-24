import mne
import matplotlib.pyplot as plt
# mne.sys_info()


file_path = "S001R01.edf"
mne.set_config('MNE_LOGGING_LEVEL', 'INFO', set_env=True)
raw = mne.io.read_raw_edf(file_path,preload=True)

print(raw.ch_names)
data, times = raw.get_data(picks='C3..', return_times=True)

plt.plot(times, data.T)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('EEG Channel C3')
plt.show()