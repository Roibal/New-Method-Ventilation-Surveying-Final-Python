import matplotlib.pyplot as plt
import csv
import datetime 

"""
The Purpose of "Data_TestUGMine_Graphing_Test.py" 
is to load data and display data collected by the two data collection 
units (raspberry pi & sense Hat) for the purpose of ventilation engineering. 

This particular python script is designed to increase the usability of this 
program by increasing the number of functions (load data, graph data)
to allow easier changing of variables.

The Data collected in this example was collected over a period of two days at
an underground mining operation 

Created by: Joaquin Roibal

Copyright (c) 2016 Joaquin Roibal
MIT License
December 1, 2016

"""

def loaddata(file_number, file_name, start_time, 
            end_time, num_list, datetime_list, temp_list, press_list, humidity_list):
    """
    The Purpose of 'loaddata' function is to load data from a file with a specified
    start time and end time. This function returns a list of lists which can be used
    for graphing purposes.
    Input: File Number, Name of File, Start Time, End Time, Num_List, Datetime_List,
        Temp_list, Press_List, Humidity_List
    Output: List of [num_files, datetime_list, temp list, pressure list, humid list]

    """
   
    with open(file_name, 'r') as csvfile:    
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row == []:
                pass
            else:
                print(row)
                #Convert from imported csv format back into datetime object
                date = row[-2].strip(" ")
                time = row[-1].strip(" ")
                time_format = str(date + ' ' + time)
                dt = datetime.datetime.strptime(time_format, "%m/%d/%Y %H:%M:%S")
                    #print(dt)
                
                #append to list of datetime, temperature objects for each file
                
                num_list.append(row[0])     #Create List of Numbers
                temp_list.append(float(row[1]))
                press_list.append(float(row[2]))
                humidity_list.append(float(row[-3]))
                datetime_list.append(dt)
                if dt<start_time or dt>end_time:
                    datetime_list.pop()     # remove measured value if out of
                    temp_list.pop()         # desired time period
                    press_list.pop()
                    humidity_list.pop()
                
    return [num_list, datetime_list, temp_list, press_list, humidity_list]
    
def graphdata(i, measured_csv_file, start_display, end_display, title_label):
    """
    The 'graphdata' function accepts a list of lists (formatted by load data function)
    and graphs the data using matplotlib.
    """
    
        
    """
    #Code Commented Out to develop new graph of specific weight/temp
        #Create SubPlots for specific weight and temperature
    plt.subplot(2, 1, 1)
    plt.plot(datetime_list, spec_weight_list)
    plt.title('Measurement of Specific Weight')
    plt.ylabel('Specific Weight, kg/m**3')

    plt.subplot(2, 1, 2)
    plt.plot(datetime_list, temp_list)
    plt.title('Measurement of Temperature')
    plt.ylabel('Temperature - Celcius')
    plt.show()
    """

    #Following Code is from Example 
    #http://matplotlib.org/examples/pylab_examples/multiple_yaxis_with_spines.html

    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    par2 = host.twinx()
    par2.spines["right"].set_position(("axes", 1.2))
    make_patch_spines_invisible(par2)
    par2.spines["right"].set_visible(True)

    if i == 0:
        p1, = host.plot(datetime_list, humidity_list, "b-", label="Humidity JR1")
        p2, = par1.plot(datetime_list, temp_list, "r-", label="Temperature JR1")
        p3, = par2.plot(datetime_list, press_list, "g-", label="Pressure JR1")
    if i == 1:
        p1, = host.plot(datetime2_list, humidity2_list, "b-", label="Humidity JR2")
        p2, = par1.plot(datetime2_list, temp2_list, "r-", label="Temperature JR2")
        p3, = par2.plot(datetime2_list, press2_list, "g-", label="Pressure JR2")

    host.set_title("Measurement and Recording of Temperature, Pressure, Humidity " +            measured_csv_file + "\n" + title_label)
    host.set_xlabel("Time")
    host.set_ylabel("Relative Humidity (%)")
    par1.set_ylabel("Temperature (C) ")
    par2.set_ylabel("Pressure (kPa)")

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]
    host.legend(lines, [l.get_label() for l in lines])
    plt.show()

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def autoplotting(num_list, datetime_list, temp_list, press_list, humidity_list):
    """
    The autoplotting function accepts a list of lists and graphs based upon this data. 
    """
    
    """
    for i in range(0, 6):
        plt.plot(datetime_list[i], temp_list[i], label='Temperature')
        plt.title('Temperature.\n Time Period: ' +str(datetime_list[i][0])+ ' - ' +str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()
        plt.plot(datetime_list[i], press_list[i], label = 'Pressure')
        plt.title('Pressure.\n Time Period: ' +str(datetime_list[i][0])+ ' - '+str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()
        plt.plot(datetime_list[i], humidity_list[i], label = 'Humidity')
        plt.title('Humidity.\n Time Period: '+str(datetime_list[i][0])+' - '+str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()
    """

    for i in range(0,8,2):
        plt.plot(datetime_list[i], temp_list[i], label = 'Temperature JR1')
        plt.plot(datetime_list[i+1], temp_list[i+1], label = 'Temperature JR2')
        plt.title('Temperature Comparison\n Time Period: ' +str(datetime_list[i][0])+ ' - ' +str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()

        plt.plot(datetime_list[i], press_list[i], label = 'Pressure JR1')
        plt.plot(datetime_list[i+1], press_list[i+1], label = 'Pressure JR2')
        plt.title('Pressure Comparison\n Time Period: ' +str(datetime_list[i][0])+ ' - ' +str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()

        plt.plot(datetime_list[i], humidity_list[i], label = 'Humidity JR1')
        plt.plot(datetime_list[i+1], humidity_list[i+1], label = 'Humidity JR2')
        plt.title('Humidity Comparison\n Time Period: ' +str(datetime_list[i][0])+ ' - ' +str(datetime_list[i][-1]))
        legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
        plt.show()

def main():

    #Load Data input format, single list: [file_number, list_file_name, start_time, end_time]
    #Graph each data collection unit on a separate graph for entire time
    first_recording = datetime.datetime.strptime("11/17/2016 06:00:00", "%m/%d/%Y %H:%M:%S")
    last_recording = datetime.datetime.strptime("11/18/2016 14:30:00", "%m/%d/%Y %H:%M:%S")
    file_list = [[0, 'JR1_Data_Collect_TestMine.csv', first_recording, last_recording]]
    file_list.append([1, 'JR2_Data_Collect_TestMine.csv', first_recording, last_recording])

    #Adjust Time Period for Data - Day 1
    first_recording1 = datetime.datetime.strptime("11/17/2016 10:00:00", "%m/%d/%Y %H:%M:%S")
    last_recording1 = datetime.datetime.strptime("11/17/2016 13:30:00", "%m/%d/%Y %H:%M:%S")
    file_list.append([2, 'JR1_Data_Collect_TestMine.csv', first_recording1, last_recording1])
    file_list.append([3, 'JR2_Data_Collect_TestMine.csv', first_recording1, last_recording1])

    #Adjust Time Period for Data - Day 2
    first_recording2 = datetime.datetime.strptime("11/18/2016 08:30:00", "%m/%d/%Y %H:%M:%S")
    last_recording2 = datetime.datetime.strptime("11/18/2016 13:30:00", "%m/%d/%Y %H:%M:%S")
    file_list.append([4, 'JR1_Data_Collect_TestMine.csv', first_recording2, last_recording2])
    file_list.append([5, 'JR2_Data_Collect_TestMine.csv', first_recording2, last_recording2])

    #Create Additional Graphs for particular time periods
    #Graph will be used to display pressure change when exiting the mine.
    first_recording3 = datetime.datetime.strptime("11/18/2016 12:30:00", "%m/%d/%Y %H:%M:%S")
    last_recording3 = datetime.datetime.strptime("11/18/2016 13:30:00", "%m/%d/%Y %H:%M:%S")
    file_list.append([6, 'JR1_Data_Collect_TestMine.csv', first_recording3, last_recording3])
    file_list.append([7, 'JR2_Data_Collect_TestMine.csv', first_recording3, last_recording3])

    
    temp_list = [[],[],[],[],[],[],[],[]]
    press_list = [[],[],[],[],[],[],[],[]]
    datetime_list = [[],[],[],[],[],[],[],[]]
    num_list = [[],[],[],[],[],[],[],[]]
    humidity_list = [[],[],[],[],[],[],[],[]]
    start_list = []
    end_list = []    

    #Create List of Start and End Times    
    for time in file_list:
        start_list.append(time[-2])
        end_list.append(time[-1])
    print(start_list, end_list)
    i = 0
    for file1 in file_list:
        #Create Empty Lists which will be used for plotting purposes
        temp_list[i] = []
        press_list[i] = []
        datetime_list[i] = []
        num_list[i] = []
        humidity_list[i] = []

        values_store = loaddata(file1[0], file1[1], file1[2], file1[3], num_list[i], datetime_list[i], temp_list[i], press_list[i], humidity_list[i])
        print(values_store)
        num_list[i] = values_store[0]
        datetime_list[i] = values_store[1]
        temp_list[i] = values_store[2]
        press_list[i] = values_store[3]
        humidity_list[i] = values_store[4]
        #An Example which plots all values
        i+=1

            #Print (plot) for all values, all time segments using for loop
    autoplotting(num_list, datetime_list, temp_list, press_list, humidity_list)

if __name__=="__main__":
    main()
