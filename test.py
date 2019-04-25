import serial



with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:
    line = ser.readline()
    while line:
        print(line)
        ser.write(b'110, 135, 65, 90, 90, 90, 76')
        line = ser.readline()

