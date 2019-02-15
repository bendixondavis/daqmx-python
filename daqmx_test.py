# this is an example of reading data through daqmx python api from a
# 1 slot usb cdaq with thermocouple module and plotting it using pyplot
#documentation for api is at https://nidaqmx-python.readthedocs.io

import nidaqmx
import matplotlib.pyplot as plt

plt.ion()

i=0
with nidaqmx.Task() as task: #creates a daq task
    #adds 2 thermocouple channels on input 2 and 3 to the task
    task.ai_channels.add_ai_thrmcpl_chan("cDAQ1Mod1/ai2:3")
    #loop to get 30 data points from each channel
    while i < 30:
        #reads 1 sample per channel per second from each channel
        data = task.read(number_of_samples_per_channel=1)
        #plots the data to a plot using pyplot
        plt.scatter(i,data[0],c='r')
        plt.scatter(i,data[1],c='b')
        plt.pause(0.05)
        #prints data in list format to the terminal
        print(data)
        i=i+1
        #prints number of channels to terminal
        print(task.number_of_channels)
