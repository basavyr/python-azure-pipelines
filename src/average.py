# see this post https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script
import sys

# taken from https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from timeit import default_timer as timer
import time

import platform as os
from datetime import datetime
import random

import numpy as np
import scipy as sp
import matplotlib as plt

# py_ver = str(sys.version_info.major)+'.'+str(sys.version_info.minor)
py_build_info = 'null'
if(sys.version_info.major == 2):
    py_build_info = 'Python' + \
        str(sys.version_info.major)+'.'+str(sys.version_info.minor)
else:
    py_build_info = 'Python' + \
        str(sys.version_info.major)+'.'+str(sys.version_info.minor)

currentOS = 'null'
if(str(os.system()) == 'Darwin'):
    currentOS = 'MacOS'
else:
    currentOS = 'Linux'


def average(array):
    sumv = 0.0
    for x in array:
        sumv = sumv+x
    return float(sumv/len(array))


def generate_rand_container(size):
    container = []
    for id in range(size):
        r_int = random.randrange(0, 100, 1)
        container.append(r_int)
    return container


newline = '\n'

for log_file in range(100):
    log_file_name = str(os.system())+'-'+py_build_info + '-' + \
        str(int(time.time()))+'.log'
    path = '../logs/'+log_file_name
    new_log_file = open(path, 'w')
    for log_line in range(999):
        start = timer()
        rand_container = generate_rand_container(1000)
        avg = average(rand_container)
        end = timer()
        now_utc = datetime.now()
        generation_time = 'GEN_TIME - ' + str(now_utc)
        machine = ' OS - ' + currentOS
        platform = ' PLATFORM - '+str(os.platform())
        aarch = ' ARCH -' + str(os.architecture()[0])
        operation = ' RESULT - '+str(avg)
        duration = ' PROCESS_DURATION - ' + str(float(end-start))
        build_info = ' PY_BUID_VER - '+py_build_info
        new_log_file.write(generation_time+machine +
                           platform+aarch+operation+duration+build_info)
        new_log_file.write(newline)
    new_log_file.close()
    print('Generated file '+str(log_file+1))
