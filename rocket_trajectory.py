import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('trajectory.csv')

data.columns = data.columns.str.strip()

print(data.head())

time = data['Time']
altitudes = data['Altitude']
velocity = data['Velocity']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

ax1.plot(data['Time'], data['Altitude'], color='r')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Altitude (meters)')
ax1.set_title('Altitude vs. Time')
ax1.grid(True, linestyle='--')
ax1.legend()

ax2.plot(data['Altitude'], data['Velocity'], color='b')
ax2.set_xlabel('Altitude (meters)')
ax2.set_ylabel('Velocity (meters/second)')
ax2.set_title('Velocity vs. Altitude')
ax2.grid(True, linestyle='--')
ax2.legend()

plt.tight_layout()
plt.show()
