import numpy as np
import pickle
import pandas as pd

cntHb_synth = pd.read_csv('cntHb_doppel_reduced.csv')
print("Head 10: ", cntHb_synth.head(10))

# X should be [samples, variables, length]
# For fNIRS, this is [75 trials x 10 participants, 40 channels, 28 seconds]
# Y is a list of labels
ind_data = []
labels = []

# Split all the data into individual arrays for easier processing
for ind in range(0, 840000, 28):
    end = ind + 27
    ind_data.append(cntHb_synth.loc[ind:end, 'cntHb'])

for participant in range(0, 840000, 8400):
        for task in range(0, 75, 1):
            ind = participant + (task * 28)
            labels.append(cntHb_synth.loc[ind, 'taskLabel'].astype(str)) # The label can be a float (as in this case) or a string
print("Length of Labels: ", len(labels))
np.save('reduced_labels_format.npy', labels)
# print(type(labels[0]))
print("Ind Length: ", len(ind_data))
print("Ind Length: ", len(ind_data[0]))

# Process into the required dimensions for classification
total_data = []
for task in range(750):
    channel_arr = []
    for channel in range(40):
        channel_ind = (channel * 75) + task
        # print(channel_ind)
        # There's an off-by-one error here, we do one more iteration than necessary
        try:
            channel_arr.append(ind_data[channel_ind])
        except IndexError:
            pass
    total_data.append(channel_arr)
# np_version = np.asarray(total_data)
# print("NP Dims: ", np_version.shape)
print(len(total_data))
print(len(total_data[1]))
print(len(total_data[1][0]))

for i in range(len(total_data)):
    if len(total_data[i]) != 40:
        print(len(total_data[i]))
    for j in range(len(total_data[i])):
        if len(total_data[i][j]) != 28:
            print(len(total_data[i][j]))

save = np.array(total_data, dtype=float)
np.save('reduced_class_format.npy', save)

# f = open('cntHb_doppel_class_format.pckl', 'wb')
# pickle.dump(save, f)
# f.close()