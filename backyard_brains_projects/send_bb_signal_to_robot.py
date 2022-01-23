import serial
import zmq
import time

port = "8001"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)


ser = serial.Serial("/dev/ttyACM0", 9600)
level1 = 100
# level2 = 180

while True:
    cc=str(ser.readline())
    inten = cc[2:][:-8]

    try:
        inten = int(float(inten))
        # print(inten)
        if inten > 0 and inten < level1:
            print("level 1")
            socket.send_string("1")
        elif inten > level1:
            print("level 2")
            socket.send_string("2")
            # time.sleep(4)
        # elif inten > level2:
        #     print("level 3")
            # print(inten)
    except:
        print("Values not ready yet!")

