#!/usr/bin/python3

import argparse
import random
import math
import copy

DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 768
DEFAULT_SEED = 1
DEFAULT_OUTPUT = 'all'
DEFAULT_DELTA = 1

class Point(object):
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def transform(self, alfaRad, k, cX, cY):
        self.x = int((self.x * math.cos(alfaRad) -
                    self.y * math.sin(alfaRad)) * k + cX )
        self.y = int((self.x * math.sin(alfaRad) +
                    self.y * math.cos(alfaRad)) * k + cY )

    def clone(self):
        return Point(self.x, self.y)

    def __eq__(self, P):
        return self.x == P.x and self.y == P.y

    def distanse(self, P):
        dx = self.x - P.x if self.x > P.x else P.x - self.x
        dy = self.y - P.y if self.y > P.y else P.y - self.y
        return int(math.sqrt(dx**2 + dy**2))


    @staticmethod
    def random(width, height):
        return Point(
            random.randint(-width, width),
            random.randint(-height, height))

def init(args):
    random.seed(args.seed *
                args.base *
                args.width *
                args.height *
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

#TODO: Simulate noise on master pattern
def randomize_master(args, master):
    return master

def transform_master(args, transform_key, master):
    alfaRad, k, cX, cY = transform_key
    transform_master = copy.deepcopy(master)
    for point in transform_master:
        point.transform(alfaRad, k, cX, cY)
    return transform_master

#TODO: Add parameter for noise size multiplier
def gen_recognized(args, transform_key, master):
    alfaRad, k, cX, cY = transform_key
    recognized = copy.deepcopy(master)
    while len(recognized)<args.ext:
        point = Point.random(args.width * 5, args.height * 5)
        point.transform(alfaRad, k, cX, cY)
        min_distanse = args.delta*10
        for p in recognized:
            distanse = p.distanse(point)
            if distanse<min_distanse:
                min_distanse = distanse
        if min_distanse > args.delta:
            recognized.insert(random.randint(0,len(recognized)-1), point)
    return recognized

def gen_transform_key(args):
    alfaRad = random.random()*2*math.pi
    k = (random.random()+0.5)
    cX = (random.random()-0.5) * args.width
    cY = (random.random()-0.5) * args.height
    return (alfaRad, k, cX, cY)

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
                        help='random seed for recognized (%d)' % DEFAULT_SEED)
    parser.add_argument('--delta', type=int,
                        nargs='?',
                        default=DEFAULT_DELTA,
                        help='master pattern randomize delta (%d)' % DEFAULT_DELTA)
    parser.add_argument('--output', nargs='?',
                        default=DEFAULT_OUTPUT,
                        choices=['all',
                                 'master',
                                 'recognized',
                                 'recognized-pattern',
                                 'none'],
                        help='output type (%s)' % DEFAULT_OUTPUT)
#parse arguments
    args = parser.parse_args()

#init
    init(args)

#generate master
    master = gen_master(args)

#randomize master
    master_randomized = randomize_master(args, master)

#generate transformation keys
    transform_key = gen_transform_key(args)

#transform master
    master_transformed = transform_master(args, transform_key, master_randomized)

#generate recognized
    recognized = gen_recognized(args, transform_key, master_transformed)

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
