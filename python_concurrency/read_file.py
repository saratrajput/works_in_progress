import time
import cv2


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def take_picture():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite("image_" + str(i) + ".jpg", frame)
    cam.release()


if __name__ == '__main__':
    logfile = open("my_logfile.txt", "r")
    loglines = follow(logfile)
    i = 0
    for line in loglines:
        line = line.strip("\n")
        if line == "Take Picture":
            take_picture()
            i = i + 1
