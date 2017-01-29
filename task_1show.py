#!/usr/bin/python3
from tkinter import *
import math
import sys

WINDOW_SIDE=512

#Data format, resized and centred for WINDOW_SIDE points
# [0] - master pattern
# [1] - recognized pattern
def show(data):
    master = Tk()

    def close(event):
        master.withdraw() # if you want to bring it back
        sys.exit() # if you want to exit the ent

    master.bind('<Escape>', close)

    w = Canvas(master, width=WINDOW_SIDE*2, height=WINDOW_SIDE)
    w.pack()

    w.create_line(WINDOW_SIDE, 0, WINDOW_SIDE, WINDOW_SIDE)

    for x,y in data[0]:
        w.create_oval(x-2,y-2,x+2,y+2)
    for x,y in data[1]:
        w.create_oval(WINDOW_SIDE+x-2,y-2,WINDOW_SIDE+x+2,y+2)

    mainloop()

def read_data():
    return [
        [ int(value)
            for value in value.strip().split(' ')
        ] for value in sys.stdin.readlines()
    ]

def resize_data(data):
    x = sorted([x for x,y in data])
    y = sorted([y for x,y in data])

    x_center = (x[-1]+x[0])/2
    y_center = (y[-1]+y[0])/2

    x_k = (WINDOW_SIDE*0.9)/(x[-1]-x[0])
    y_k = (WINDOW_SIDE*0.9)/(y[-1]-y[0])

    k = min(x_k, y_k)

    for point in data:
        point[0] = int( (point[0]-x_center) * k + WINDOW_SIDE/2)
        point[1] = int( (point[1]-y_center) * k + WINDOW_SIDE/2)

    return data

def convert_data(data):
    master_size = data[0][0]
    recognized_size = data[master_size+1][0]
    master = data[1:master_size+1]
    recognized = data[-recognized_size:]
    return [resize_data(master), resize_data(recognized)]

def main():
    data = convert_data(read_data())
    show(data)

if __name__ == "__main__":
    main()
