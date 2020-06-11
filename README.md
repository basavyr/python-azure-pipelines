[![Build Status](https://robertpoenaru.visualstudio.com/test-pipelines/_apis/build/status/basavyr.python-azure-pipelines?branchName=master)](https://robertpoenaru.visualstudio.com/test-pipelines/_build/latest?definitionId=1&branchName=master)

# Python & CI/CD - Azure Pipelines
A simple Python that integrates CI/CD workflow with Azure Pipelines

The project contains the following implementations:

1. `average.py` - A script that generates log files with time measurements for the generation of $N$ random numbers.
   1. The random numbers are inserted into a container (e.g. list), then calculation of the average value in the container is performed, then time measurement stops.
   2. The generated logs depend on what Python interpreter is running the script (e.g. Python 2.7 or Python 3.6 and so on).
   3. Logs also change according to the platform on which the script runs.
   4. The Azure Pipeline associated with this job generates an artifact containing all the logs.

2. `data.py` - A script that performs graphical representation of some random data.
   1. The script uses `matplotlib` module for saving some plots as `.pdf` format.
   2. `numpy` is used for computational purposes.
   3. The generated data represents pairs of data points $(x,y)$, where $x\in[0,10]$ and $y=f(x;\mathcal{P})$, with $\mathcal{P}$ representing a set of parameters which enter in the function.

## Issues

[This document](issues.md) describes in detail any potential issues that ocurred in the development pipeline.

## Artifacts 

* `data.py` - this implementation generates output graphs (in `.pdf` format), and the plot name depends on the platform on which the script is executed, and also the major Python version that is chosen for execution.