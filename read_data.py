import pickle
import pandas as pd
import numpy as np
import scipy.io
import csv
from data_loading import real_data_loading, sine_data_generation

df = pd.DataFrame(columns=['cntHb', 'channel', 'taskLabel'])

# For each participant
for dataset in range(1, 11):
    print("Participant: ", dataset)
    participant = np.loadtxt(f'data/{dataset:02}_processed.csv', delimiter=",")
    # print(participant.shape)
    time = np.loadtxt(f'data/{dataset:02}_time.csv', delimiter=",")
    time = time / 1000
    mat = scipy.io.loadmat(f'data/{dataset:02}_labels.mat')['Y']
    labels = []
    label_two_count = 0

    # Fix the labels matrix so it can be easily indexed
    for lab in mat:
        labels.append(lab[0])

    # For each channel in participants (grouped so they're a continuous sequence)
    for channel in range(0, 40):
        labelIndex = 0
        start = 0
        end = 100
        currRow = []
        label_two_count = 0

        # For each window (which each come with a specific label)
        for i in range(len(time)):
            if label_two_count < 10:
                end = int(round(time[i]))
                segment = participant[start:end][:, channel]
                # print(start, end, channel, segment.shape)

                # If the there's a full data collection window (excludes the 0-2 second windows before the participant's first task)
                if segment.shape[0] > 3:
                    # print("i: ", i, "Channel: ", channel, " Label: ", labels[labelIndex])
                    for i in range(0, 28): # Limit all sequences to 28 readings to they can be consistent 
                        # Now that we've collected all the right information, we can add this as a row to the DataFrame
                        currRow = [segment[i], channel + 1, labels[labelIndex]] # Channel is 0-indexed
                        df.loc[len(df)] = currRow
                    if labels[labelIndex] == 2:
                        label_two_count += 1
                    labelIndex = labelIndex + 1 # Only index the label if we've actually moved to the next trial, since the start ones don't count
                start = end + 1
            else:
                if labels[labelIndex] != 2:
                    end = int(round(time[i]))
                    segment = participant[start:end][:, channel]
                    # print(start, end, channel, segment.shape)

                    # If the there's a full data collection window (excludes the 0-2 second windows before the participant's first task)
                    if segment.shape[0] > 3:
                        # print("i: ", i, "Channel: ", channel, " Label: ", labels[labelIndex])
                        for i in range(0, 28): # Limit all sequences to 28 readings to they can be consistent 
                            # Now that we've collected all the right information, we can add this as a row to the DataFrame
                            currRow = [segment[i], channel + 1, labels[labelIndex]] # Channel is 0-indexed
                            df.loc[len(df)] = currRow
                        labelIndex = labelIndex + 1 # Only index the label if we've actually moved to the next trial, since the start ones don't count
                    start = end + 1
                else:
                    labelIndex += 1
        segment = participant[start:start + 29][:, channel]

        # Does the last row always
        for i in range(0, 28):
            currRow  = [segment[i], channel + 1, labels[labelIndex]]
            df.loc[len(df)] = currRow
# Ensure the data looks right
print(df.head(5))
print(df.shape) # Dimensions should be [total recordings x participants (rows), 3 (cols)]
df.to_csv('cntHb_doppel_reduced.csv', sep=",") # Save for use in DoppelGANger

# segmented = []
# for p in range(1, 11):
#     participant = np.loadtxt(f'data/{p:02}_processed.csv', delimiter=",")
#     # print(participant.shape)
#     time = np.loadtxt(f'data/{p:02}_time.csv', delimiter=",")
#     time = time / 1000
#     mat = scipy.io.loadmat(f'data/{p:02}_labels.mat')['Y']
#     start = 0
#     end = 100
#     for counter, time in enumerate(time):
#         end = int(time)
#         # print("Window: ", start, end)
#         # print("P: ", participant[start:end])
#         # print("P Shape: ", participant[start:end][:, 0].shape)
#         if mat[counter][0] == 1: # Gets label 1 only
#             segmented.append(participant[start:end][:, 0]) # Gets channel 1 only
#         start = end + 1
# print("Segmented: ", segmented)
# print(len(segmented))
# print(len(segmented[1]))

# df = pd.DataFrame(segmented).transpose()
# print(df)
# df.to_csv('c1l1_full.csv')

# c1_data = np.load('c1_data.npy')
# c1_labels = np.load('c1_labels.npy')

# print(c1_data[c1_labels == 1])
# print(c1_data[c1_labels == 1].shape)

# c1_data = c1_data[:, 0, :]
# print(c1_data[c1_labels == 3])
# data_to_save = np.transpose(c1_data[c1_labels == 3])

# headers = ''
# # Label them 1 - 30 (inclusive)
# for participant in range(1, 31):
#     # Label them 1 - 26 (inclusive)
#     for trial in range(1, 26):
#         label = 'p' + str(participant) + '_t' + str(trial)
#         headers = headers + label + ','
# np.savetxt("c1_l3.csv", np.transpose(c1_data[c1_labels == 1]), header=headers, delimiter=",")