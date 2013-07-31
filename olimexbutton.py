import serial
ser2 = serial.Serial('COM8',baudrate=115200)
ser = serial.Serial('COM10',baudrate=9600)
ser.isOpen()
ser2.isOpen()
def changescreen(line1):
    int1="1"
    int0="0"
    if line1==int1:
        # resetscreen="z"     #clear screen
        #ser2.write(resetscreen +'\r\n')
        message3 ="t \"Button OFF\"100 100" #Second Screen
        ser2.write(message3+'\r\n')
    elif line1==int0:
        #resetscreen="z"     #clear screen
        #ser2.write(resetscreen +'\r\n')
        message4 ="t \"Button ON\"120 120" #Second Screen
        ser2.write(message4+'\r\n')
    else:
        pass

resetscreen="z"     #clear screen
ser2.write(resetscreen +'\r\n')
line2="-1"
while True:
    line=ser.readline()
    line=line[0]
    print line
    if(line==line2):
        print("Same")
    else:
        ser2.write(resetscreen +'\r\n')
        print("different")
        changescreen(line)
        line2=line
    print line2
ser.close()