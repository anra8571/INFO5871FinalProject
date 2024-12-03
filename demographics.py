import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('synthetic_cntHb_reduced_375000.csv')
# print(df.head(10))

print(df.shape[0])

# Count how many of each channel and each label
channels = np.zeros(40)
labels = np.zeros(3)
for i in range(0, df.shape[0], 28):
    channels[int(df.loc[i, 'channel'] - 1)] += 1
    labels[int(df.loc[i, 'taskLabel'] - 1)] += 1
print("Length of Channels: ", len(channels))
print(channels)
print("Length of Labels: ", len(labels))
print(labels)

# Plot Channels
channel_x = np.arange(1, 41, 1)
plt.bar(channel_x, channels)
plt.title("Samples per Channel for Synthetic Reduced Left-Hand")
plt.xlabel("Channels 1 - 40")
plt.ylabel("Number of Samples Per Channel")
plt.show()

# Plot Labels
labels_x = np.arange(1, 4, 1)
plt.bar(labels_x, labels)
plt.title("Samples per Label for Synthetic Reduced Left-Hand")
plt.xlabel("Labels 1 - 3")
plt.ylabel("Number of Samples Per Label")
plt.show()