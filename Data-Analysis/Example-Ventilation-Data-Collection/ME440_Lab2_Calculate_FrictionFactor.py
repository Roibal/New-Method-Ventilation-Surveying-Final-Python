import math
import matplotlib.pyplot as plt
import Ventilation_Mining_Python_Toolbox as vent

"""
The Purpose of this python script is to calculate the friction factor for a mine
ventilation network setup. The Mine Ventilation Network is located on the 
New Mexico Tech Main Campus in MSEC 187.

Copyright (c) 2016 Joaquin Roibal
MIT License
"""

def main():
    """
    Lab 2 requires the calculation of friction factors for a ventilation network.
    This code will utilize a previously developed ventilation analysis toolbox.
    """
    #Initialize values for network include length & diameter
    Length = 70   #Length of Ducting in Feet
    Diameter = (4 / 12)        #Convert Diameter of 4 inches to Feet
    #Format for Data Storage: Measurement Location, Tot. Press, Stat. Press,
    #Vel. Press, Velocity [units in Pascals]  
    #Data Collected 11/23/2016   
    measured_values = []
    measured_values.append([1, 302.7, 265.3, 35.3, 7.73])
    measured_values.append([3, 291.7, 251.7, 37.7, 8.05])
    measured_values.append([5, 284.0, 243.7, 38.3, 7.92])
    measured_values.append([11, 230.7, 182.7, 47.3, 8.8])
    measured_values.append([12, 121.0, 121.0, 0, .18])
    measured_values.append([13, 156.0, 126.7, 28.0, 6.95])
    measured_values.append([10, 81.0, 67.0, 15.3, 4.6])
    measured_values.append([9, 71.3, 39.7, 28.7, 6.9])
    measured_values.append([2, 39.3, 1.3, 40.3, 8.5])

    for num in measured_values:
        num[1] = num[1]*0.00401463078662         #Convert from Pa to in H20
        num[2] = num[2]*0.00401463078662
        num[3] = num[3]*0.00401463078662
        num[4] = num[4]*3.28                #Convert from Meters to Feet

    #print(measured_values)
    i = 0
    for val in measured_values:
        Q = val[4]*3.14*(Diameter/2.0)**2*60.0/100000.0  #Flow in CFM
        #print(Q)
        spec_weight_air = 0.075
        if i == 0:
            Head_Loss_F = 0
            Prev_Head_Val = val[1]
        else:
            Head_Loss_F = Prev_Head_Val - val[1]
        k_factor = vent.CalculateFrictionFactor(Head_Loss_F, 30, Diameter, Q, spec_weight_air)
        #print(k_factor)
    Tot_Head_Loss_F = measured_values[0][1]-measured_values[-1][1]
    In_11_Head_Loss_F = measured_values[0][1]-measured_values[3][1]
    In_5_Head_Loss_F = measured_values[0][1]-measured_values[2][1]
    Five_13_Head_Loss_F = measured_values[2][1]-measured_values[5][1]
    Eleven_Ten_Head_Loss_F = measured_values[3][1]-measured_values[-3][1]
    print("Inlet to 11 Head Loss:", In_11_Head_Loss_F)
    print("Total Head Loss:    ", Tot_Head_Loss_F)
    print("Inlet to 5 Head Loss:", In_5_Head_Loss_F)
    print("5 to 13 Head Loss:", Five_13_Head_Loss_F)
    print("11 to 10 Head Loss:", Eleven_Ten_Head_Loss_F)
    tot_k_factor = vent.CalculateFrictionFactor(Tot_Head_Loss_F, Length, Diameter, Q, spec_weight_air)
    print("Total Calculated Friction Factor:    ", tot_k_factor)
    in_11_k_factor = vent.CalculateFrictionFactor(In_11_Head_Loss_F, 23.95, Diameter, Q, spec_weight_air)
    in_5_k_factor = vent.CalculateFrictionFactor(In_5_Head_Loss_F, 10.5, Diameter, Q, spec_weight_air)
    five_13_k_factor = vent.CalculateFrictionFactor(Five_13_Head_Loss_F, 26.26, Diameter, Q, spec_weight_air)
    eleven_ten_k_factor = vent.CalculateFrictionFactor(Eleven_Ten_Head_Loss_F, 24.28, Diameter, Q, spec_weight_air)
    print("Friction Factor from Inlet to 11:    ", in_11_k_factor)
    print("Friction Factor from Inlet to 5:    ", in_5_k_factor)
    print("Friction Factor from 5 to 13:    ", five_13_k_factor)
    print("Friction Factor from 11 to 10:    ", eleven_ten_k_factor)
        #val.append(k_factor)
    #print(measured_values)

if __name__ == "__main__":
    main()


