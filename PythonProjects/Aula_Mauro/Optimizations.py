#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from skopt import gp_minimize
from skopt.plots import (
    plot_gaussian_process,
    plot_convergence,
)

from scipy.optimize import (
    curve_fit, 
    shgo, 
    direct,
    Bounds,
)

from mealpy import (
    FloatVar,
    Problem,
    PSO,
    MFO,
    EFO,
    ASO,
    MA,
    ACOR,
    BBO,
    GSKA,
    SA,
)

# Define colors as in Gnuplot
RED = '#DD181F'
GREEN = '#5E9C36'
BLUE = '#0060AD'
ORCHID = '#BA55D3'
PERU = '#CD853F'
GRAY = '#696969'
BLACK = '#000000'
DARKTURQUOISE = '#00CED1'
ORANGE = '#F89441'
MAGENTA = '#FF00FF'
YELLOW = '#F7F09A'

# Define figure parameters
FS = (8, 7)
DPI = 70
SMALL_SIZE = 10
MEDIUM_SIZE = 16
BIGGER_SIZE = 26

cmap = sns.diverging_palette(
    h_neg=18,
    h_pos=248,
    s=140,
    as_cmap=True,
)
sns.set_context("poster")
sns.set_theme(font="Times New Roman", font_scale=2)
sns.color_palette("husl", 9)

def nint(x):
    nx = int(x + (x % (1 if x >= 0 else -1)))
    return nx

def objective_function(x):
    f = np.sin(x) + np.sin(10.*x/3.)
    return f

def fitness_function(parameters):
    Ws = parameters
    predicted = Ws[0]
    for i in range(len(Ws)):
        if i == 0:
            continue
        predicted += (Ws[i] * x_data[f'x{i}'])

    diff = predicted - y_data
    mae = np.mean(np.abs(diff))
    return mae

D = 9
ME = 100
PS = 80
lb = 0.
ub = 1
npoints = 133

csv_data = pd.read_csv('ex2.csv', sep=',')

print('Data Loaded:')
print(csv_data)

x_data = csv_data[['x1','x2','x3','x4','x5','x6','x7','x8']]
y_data = csv_data['y']

problem_dict1 = {
    "bounds": FloatVar(lb=(lb,) * D, ub=(ub,) * D, name="delta"),
    "obj_func": fitness_function,
    "minmax": "min",
    "log_to": "console",
}

model1 = PSO.AIW_PSO(epoch=ME, pop_size=PS, c1=2.05, c2=2.05, alpha=0.8)

print('Initializing problem solving')
g_best1 = model1.solve(problem_dict1)
model = model1
g_best = g_best1
nm = 1

print(f"Model: {model1.name}, Solution: {g_best1.solution}, Fitness: {g_best1.target.fitness}")

print("Best model: ")
print(f"#{nm}, Model: {model.name}, Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

dimensions = []
for i in range(D):
    dimensions.append((lb, ub))

res = gp_minimize(fitness_function,   # the function to minimize
                  dimensions,         # the bounds on each dimension of x
                  initial_point_generator="random",
                  acq_func="gp_hedge",      # the acquisition function
                  n_calls=100,         # the number of evaluations of f
                  n_random_starts=80,  # the number of random initialization points
#                  noise=0.1**2,       # the noise level (optional)
                  n_jobs=4,
                  random_state=42)   # the random seed

"x^*=%.14f, f(x^*)=%.14f" % (res.x[0], res.fun)

g_best.solution[0]

sns.set_theme(font="Times New Roman", font_scale=3)

plot_convergence(res)

def fitted_function():
    Ws = g_best.solution
    f = Ws[0]
    for i in range(len(Ws)):
        if i == 0:
            continue
        f += x_data[f'x{i}'] * Ws[i]
    return f

sns.set_theme(font="Times New Roman", font_scale=3)

y_data_fit = fitted_function()

print('\nValue')
print(y_data_fit)

plt.figure(figsize=FS, dpi=DPI)
# Set default sans-serif font
plt.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['mathtext.fontset'] = "cm"
plt.tick_params(axis='both', direction='in', length=5)

plot_convergence(res)

plt.figure(figsize=FS, dpi=DPI)
# Set default sans-serif font
plt.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['mathtext.fontset'] = "cm"
plt.tick_params(axis='both', direction='in', length=5)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")

plt.scatter(y_data_fit, y_data, label='Data', color=RED, s=100)
plt.legend(loc='best')
plt.show()