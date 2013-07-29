import time
import serial
ser = serial.Serial('COM8',baudrate=115200,timeout=0)
ser.isOpen()
def Initialize_Parameters():
    # Reset Screen
    resetscreen="z"     #clear screen
    ser.write(resetscreen +'\r\n')
    #Buttons
    button  =" xi 11 30 100" #Continue Button
    button1 =" xi 11 30 150" #Exit Button
    ser.write(button +'\r\n')
    ser.write(button1 +'\r\n')

#threeeedfs
    #Message
    message  ="t \"Welcome to\n Erdos Miller Instruments\n Press a button: \"11 11"
    message1 ="t \"Continue\"70 100"
    message2 ="t \"Exit\"70 150"
    color ="S 645 FFF"
    color1="S 090 FFF"
    color2="S 009 FFF"

    ser.write(color +'\r\n')
    ser.write(message +'\r\n')
    ser.write(color1 +'\r\n')
    ser.write(message1 +'\r\n')
    ser.write(color2 +'\r\n')
    ser.write(message2 +'\r\n')

    #Hotspots
    hotspot=  " xs 128 30 100 60 130"    #Continue Button
    hotspot1= " xs 129 30 150 60 180"   #Exit Button
    hotspot2= " xs 130 10 180 70 220"    #Return Button
    ser.write(hotspot+'\r\n')
    ser.write(hotspot1+'\r\n')

def ContinueInitialize_Parameters():
    message5 ="t \"Return\"90 190"    #Second Screen
    ser.write(message5+'\r\n')
    #Buttons
    button3 =" xi 2 10 180" #Return Button
    ser.write(button3+'\r\n')

    #Hotspots
    hotspot2= " xs 130 10 180 70 220"    #Return Button
    ser.write(hotspot2+'\r\n')
    
#Reading Data
Initialize_Parameters()
print("connected to: "+ ser.portstr)
while True:
    line=ser.read(4)	
    str="x128"
    str1="x129"
    str2="x130"
    print line
    if line==str:
        resetscreen="z"     #clear screen
        ser.write(resetscreen +'\r\n')
        message3 ="t \"Continue\"100 100" #Second Screen
        ser.write(message3+'\r\n')
        ContinueInitialize_Parameters()

    elif line==str1:
        resetscreen="z"     #clear screen
        ser.write(resetscreen +'\r\n')
        message4 ="t \"Exit\"100 100"     #Second Screen
        ser.write(message4+'\r\n')
        ContinueInitialize_Parameters()

    elif line==str2:
        Initialize_Parameters()
        
    else:
        print(line+ '\r\n')
ser.close()