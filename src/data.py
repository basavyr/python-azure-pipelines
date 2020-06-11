import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import sys
import platform as os
import time
from datetime import datetime
# the set of params = {w1,w2,t0}

build_label = 'Generated with Python ' + str(sys.version_info.major)+'.'+str(
    sys.version_info.minor) + '\n'+'On '+str(os.system())+' @ '+str(datetime.utcnow())

build_file_name = 'Python-'+str(sys.version_info.major)+'.'+str(
    sys.version_info.minor)


def init_params(param1, param2, param3):
    w1 = param1
    w2 = param2
    t0 = param3
    P = [w1, w2, t0]
    return P


def MathFunction(arg, params):
    term1 = params[0]*np.power(float(arg), -2)
    term2 = float(np.sin(params[1]*arg)/arg)
    term3 = params[2]*np.power(arg, 2)
    F = term1+term2+term3
    return F


def CreatePlot(plotname, x_data, y_data, params):
    derived_params1 = [params[0]-2, params[1]+1, params[2]-0.01]
    derived_params2 = [params[0]-1, params[1]+2, params[2]+0.01]
    y_data2 = generateYData(x_data, derived_params1)
    y_data3 = generateYData(x_data, derived_params2)
    # rc('text', usetex=True)
    # rc('font', **{'family': 'serif', 'serif': ['Times']})
    plt.rcParams["font.family"] = "Times New Roman"
    # plt.title(r'$F(x;\mathcal{P}) = w_1x^{-2}+w_2\frac{\sin(x)}{x}+t_0x^2$')
    plt.text(2, 2, build_label, fontsize=6, style='italic',
             bbox={'facecolor': 'red', 'alpha': 0.1, 'pad': 10})
    plt.xlabel('x')
    plt.ylabel('F(x;P)')
    extension = '.pdf'
    source = '../graphs/'
    plotfile = source+plotname+extension
    legendstring = 'P: ('+str(params[0])+' , ' + \
        str(params[1]) + ' , '+str(params[2])+')'
    legendstring2 = 'P: ('+str(derived_params1[0])+' , ' + str(
        derived_params1[1]) + ' , '+str(derived_params1[2])+')'
    legendstring3 = 'P: ('+str(derived_params2[0])+' , ' + str(
        derived_params2[1]) + ' , '+str(derived_params2[2])+')'
    plt.plot(x_data, y_data, '-ob', label=legendstring)
    plt.plot(x_data, y_data2, '-or', label=legendstring2)
    plt.plot(x_data, y_data3, '-og', label=legendstring3)
    plt.legend(loc='best')
    plt.savefig(plotfile, bbox_inches='tight')
    plt.close()


def generateYData(x, params):
    y_data = []
    for x_id in x:
        y_data.append(MathFunction(x_id, params))
    return y_data


def generateData(x, y):
    error = 'The two lists can\'t form a VALID  dataset'
    invalid = 'The dataset contains invalid elements'
    dataset = []
    if(len(x) != len(y)):
        return error
    else:
        for id in range(len(x)):
            if(np.isnan(x[id]) == False and np.isnan(y[id]) == False):
                pair = [x[id], y[id]]
                dataset.append(pair)
    if(len(dataset) == len(x)):
        return dataset
    else:
        return invalid


params = init_params(3.0, 3.0, 0.02)

x = []
for id in np.arange(1, 10, 0.1):
    x_id = round(id, 2)
    x.append(x_id)

y = []
for x_id in x:
    current_f_val = round(MathFunction(x_id, params), 2)
    y.append(current_f_val)

for plot_id in range(20):
    plotname = 'plot-'+str(plot_id+1)+'-'+build_file_name
    x_data = np.linspace(1, 10, 50, endpoint=True)
    y_data = generateYData(x_data+plot_id,   params)
    CreatePlot(plotname, x_data, y_data, params)
    print('Generated plot '+str(plot_id+1))
