import matplotlib.pyplot as plt
import numpy as np 
import argparse
import copy 
import os.path

import sys
import decimal

sys.path.append("./modules")
import load_cube

###############################################################################

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

###############################################################################

"""
compute the spherical integral 
"""

parser = argparse.ArgumentParser()
parser.add_argument("-fa","--filea", help="cube format file to be used as "\
        "file A (perform A - B)", \
        required=True, type=str)
parser.add_argument("-fb","--fileb", help="cube format file to be used as "\
        "file B (perfoem A - B)", \
        required=True, type=str)
parser.add_argument("-c","--center", help="X,Y,Z coordinate of the center "\
        " will use 0,0,0 as a default value", \
        required=True, type=str)
parser.add_argument("-dr","--deltar", help="dR step value ", \
        required=True, type=str)

if len(sys.argv) == 1:
    parser.print_help()
    exit(1)

args = parser.parse_args()

if not (os.path.isfile(args.filea)):
    print "File ", args.filea, " does not exist "
    exit(1)

print('Reading... ' + args.filea)
acube = load_cube.cube()
acube.readfile(args.filea)

if not (os.path.isfile(args.fileb)):
    print "File ", args.fileb, " does not exist "
    exit(1)

print('Reading... ' + args.fileb)
bcube = load_cube.cube()
bcube.readfile(args.fileb)

totcube = acube - bcube

