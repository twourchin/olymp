#!/usr/bin/python3

import argparse
import random

DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 768
DEFAULT_SEED = 1
DEFAULT_OUTPUT = 'all'

class Point(object):
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def transform(self, alfaRad, k, cX, cY):
        self.x = int( (self.x * math.cos(alfaRad) - self.y * math.sin(alfaRad)) * k + cX )
        self.y = int( (self.x * math.sin(alfaRad) + self.y * math.cos(alfaRad)) * k + cY )

    def clone(self):
        return Point(self.x, self.y)

    def __eq__(self, P):
        return self.x == P.x and self.y == P.y

    @staticmethod
    def random(width, height):
        return Point(
            random.randint(1,width),
            random.randint(1, height))

def init(args):
    random.seed(args.seed*
                args.base*
                args.width*
                args.height*
                args.ext)

def output(list):
    for element in list:
        print("%d %d" % (element.x, element.y))

def gen_master(args):
    master = []
    for i in range(args.base):
        p = Point.random(args.width, args.height)
        try:
            while master.index(p)>-1:
                p = Point.random(args.width, args.height)
        except ValueError:
            master.append(p)
    return master

def transform_master(args, master):

    pass

def gen_recognized(args, master):

    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int,
                        nargs='?',
                        default=DEFAULT_WIDTH,
                        help='master pattern field width (%d)' % DEFAULT_WIDTH)
    parser.add_argument('--height', type=int,
                        nargs='?',
                        default=DEFAULT_HEIGHT,
                        help='master pattern field height (%d)' % DEFAULT_HEIGHT)
    parser.add_argument('--base', type=int,
                        nargs='?',
                        required=True,
                        help='master pattern points count')
    parser.add_argument('--ext', type=int,
                        nargs='?',
                        required=True,
                        help='recognized points count')
    parser.add_argument('--seed', type=int,
                        nargs='?',
                        default=DEFAULT_SEED,
                        help='randomize seed for pattern generation')
    parser.add_argument('--output', nargs='?',
                        default=DEFAULT_OUTPUT,
                        choices=['all', 'master', 'recognized', 'recognized-pattern', 'none'],
                        help='output type (%s)' % DEFAULT_OUTPUT)
#parse arguments
    args = parser.parse_args()

#init
    init(args)

#generate master
    master = gen_master(args)

#transform master
    master_transformed = transform_master(args, master)

#generate recognized
    recognized = gen_recognized(args, master_transformed)

#output
    if args.output == 'all':
        print(len(master))
        output(master)
        print(len(recognized))
        output(recognized)
    elif args.output == 'master':
        output(master)
    elif args.output == 'recognized':
        output(recognized)
    elif args.output == 'recognized-pattern':
        output(master_transformed)
    elif args.output == 'none':
        pass

if __name__ == "__main__":
    main()
