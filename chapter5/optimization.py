import time
import random
import math

fligts={}

for line in open('schedule.txt'):
    origin, dest, depart, arrive, price = line.strip().split(',')
    print(origin)