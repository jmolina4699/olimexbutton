import serial
ser2 = serial.Serial('COM8',baudrate=115200)
ser = serial.Serial('COM10',baudrate=9600)
ser.isOpen()
ser2.isOpen()

resetscreen="z"     #clear screen
ser2.write(resetscreen +'\r\n')
line2="-1"
while True:
    line=ser.readline()
    line=line[0]
    int1="1"
    int0="0"
    if line==int1:
       # resetscreen="z"     #clear screen
        #ser2.write(resetscreen +'\r\n')
        message3 ="t \"Button ON \"100 100" #Second Screen
        ser2.write(message3+'\r\n')

    elif line==int0:
        #resetscreen="z"     #clear screen
        #ser2.write(resetscreen +'\r\n')
        message4 ="t \"Button OFF\"100 100" #Second Screen
        ser2.write(message4+'\r\n')
    else:
        pass
ser.close()