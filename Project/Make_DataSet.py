import numpy as np
import pandas as pd
import os
from scipy import signal
import matplotlib.pyplot as plt

'''
Saving signal along X axis

'''

# Changing working directory
# current_path = os.getcwd()
current_path = 'G:\Masters\Term 2\Machine Learning\Project'
data_path = os.path.join('PrimaryData')
# Get all files in the directory
file_names = os.listdir(data_path)
# Get .csv files
csv_files = []
for file in file_names:

    if '.csv' in file:
        csv_files.append(os.path.join(data_path,file))
# Reading files
dfs =[]
for file in csv_files:

    df = pd.read_csv(file)
    dfs.append(df)
# Combine all dataframes
test_df = pd.concat(dfs, axis=0, ignore_index=True)
# Separating Domains
x_s = []
xl_s = [] #--> Label
y_s = []
yl_s = []
x_t = []
xl_t = []
y_t = []
yl_t = []
for i in range(test_df.shape[0]):

    # Properties of signal
    date = test_df.date[i].split('/')
    ax = test_df.kks[i].split('_')
    label = '_'.join([date[0], date[1]])
    sig =  eval(test_df.data[i])
    sig = np.array(sig).reshape(-1,)
    sig = signal.detrend(sig) # Detrending the signal
    # Categorizing the signal
    if 'COMP' in test_df.kks.values[i]:
        if ax[4] == 'XREL':
            x_s.append(sig)
            xl_s.append(label)
        elif ax[4] == 'YREL':
            y_s.append(sig)
            yl_s.append(label)
    elif 'TURB' in test_df.kks.values[i]:
        if ax[4] == 'XREL':
            x_t.append(sig)
            xl_t.append(label)
        elif ax[4] == 'YREL':
            y_t.append(sig)
            yl_t.append(label)
# What is the range of data for each signal
range_xs = np.mean(np.max(np.array(x_s),axis=1)) - np.mean(np.min(np.array(x_s),axis=1))
range_ys = np.mean(np.max(np.array(y_s),axis=1)) - np.mean(np.min(np.array(y_s),axis=1))
range_xt = np.mean(np.max(np.array(x_t),axis=1)) - np.mean(np.min(np.array(x_t),axis=1))
range_yt = np.mean(np.max(np.array(y_t),axis=1)) - np.mean(np.min(np.array(y_t),axis=1))
# Properties of Fault
ranges = [range_xs, range_ys, range_xt, range_yt]
w = 50
ranges[2] = ranges[2]/2
f_amp = np.array(ranges)/50 # --> You can change this based on performance of the model
f_range = np.linspace(0,1,len(x_s[0]))
faults = []
noises = []
noised = []
for i in range(4):

    fault = f_amp[i]*np.sin(w*f_range)
    np.random.seed(69)
    noise = np.random.rand(len(f_range)) * f_amp[i] * 2
    noises.append(noise)
    faults.append(fault)
    noised.append(fault + noise)
# Normal & Fault for Source
x_sf = x_s[int(len(x_s)/2):] + noised[0] # Adding fault
x_sn = x_s[:int(len(x_s)/2)]
x_sl = np.zeros(shape=(len(x_s),)).astype('int8')
x_sl[int(len(x_s)/2):] = 1
# Normal & Fault for Target
x_tf = x_t[int(len(x_t)/2):] + noised[2] # Adding fault
x_tn = x_t[:int(len(x_t)/2)]
x_tl = np.zeros(shape=(len(x_t),)).astype('int8')
x_tl[int(len(x_t)/2):] = 1
# Source data
# Creating string array
data_s = []
for d in x_sn:
    data_s.append(str(list(d)))
for d in x_sf:
    data_s.append(str(list(d)))
source = {'date':xl_s,'data':data_s, 'target':x_sl}
df_s = pd.DataFrame(source)
# Target data
# Creating string array
data_t = []
for d in x_tn:
    data_t.append(str(list(d)))
for d in x_tf:
    data_t.append(str(list(d)))
target= {'date':xl_t,'data':data_t, 'target':x_tl}
df_t = pd.DataFrame(target)

df_s.to_csv(os.path.join(current_path,r'MainData\Source_data.csv'),index=False)
df_t.to_csv(os.path.join(current_path,r'MainData\Target_data.csv'),index_label=False)

'''
In order to read data list as a int or sth but string,
use this:

np.array(eval(df_t.data[1]))

This will turn it into a numpy array
'''
print(f_amp)
# # plt.subplot(x_s[0])
# plt.plot(x_s[0])
# plt.plot(x_s[-1])
# plt.show()