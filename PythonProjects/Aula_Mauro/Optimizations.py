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
FS = (7, 7)
DPI = 50
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

def fitness_function(a):
    predicted = np.sin(x_data) + np.sin(a * x_data)
    diff = predicted - y_data
    mae = np.mean(np.abs(diff))
    return mae

D = 1
ME = 500
PS = 80
lb = 2.
ub = 8.
npoints = 50

x_data = np.linspace(lb, ub, npoints)
y_data = objective_function(x_data) + (2*np.random.rand(npoints)-1)/1.5

problem_dict1 = {
    "bounds": FloatVar(lb=(lb,) * D, ub=(ub,) * D, name="delta"),
    "obj_func": fitness_function,
    "minmax": "min",
    "log_to": None, #"file",
#    "log_file": "result.log",
}

model1 = PSO.AIW_PSO(epoch=ME, pop_size=PS, c1=2.05, c2=2.05, alpha=0.8)
model2 = PSO.OriginalPSO(epoch=ME, pop_size=PS, c1=2.05, c2=2.05, w_min=0.7, w_max=0.8)
model3 = MFO.OriginalMFO(epoch=ME, pop_size=PS)
model4 = EFO.DevEFO(epoch=ME, pop_size=PS, r_rate = 0.3, ps_rate = 0.95, p_field = 0.3, n_field = 0.5)
model5 = ASO.OriginalASO(epoch=ME, pop_size=PS, alpha = 50, beta = 0.2)
model6 = MA.OriginalMA(epoch=ME, pop_size=PS, pc = 0.85, pm = 0.15, p_local = 0.5, max_local_gens = 10, bits_per_param = 4)
model7 = ACOR.OriginalACOR(epoch=ME, pop_size=PS, sample_count = 25, intent_factor = 0.5, zeta = 1.0)
model8 = BBO.DevBBO(epoch=ME, pop_size=PS, p_m=0.01, n_elites=2)
model9 = GSKA.DevGSKA(epoch=ME, pop_size=PS, pb = 0.1, kr = 0.9)
model10= SA.GaussianSA(epoch=ME, pop_size=2, temp_init = 100, cooling_rate = 0.99, scale = 0.1)

g_best1 = model1.solve(problem_dict1)
model = model1
g_best = g_best1
nm = 1
g_best2 = model2.solve(problem_dict1)
if (g_best2.target.fitness < g_best.target.fitness):
    model = model2
    g_best = g_best2
    nm = 2
g_best3 = model3.solve(problem_dict1)
if (g_best3.target.fitness < g_best.target.fitness):
    model = model3
    g_best = g_best3
    nm = 3
g_best4 = model4.solve(problem_dict1)
if (g_best4.target.fitness < g_best.target.fitness):
    model = model4
    g_best = g_best4
    nm = 4
g_best5 = model5.solve(problem_dict1)
if (g_best5.target.fitness < g_best.target.fitness):
    model = model5
    g_best = g_best5
    nm = 5
g_best6 = model6.solve(problem_dict1)
if (g_best6.target.fitness < g_best.target.fitness):
    model = model6
    g_best = g_best6
    nm = 6
g_best7 = model7.solve(problem_dict1)
if (g_best7.target.fitness < g_best.target.fitness):
    model = model7
    g_best = g_best7
    nm = 7
g_best8 = model8.solve(problem_dict1)
if (g_best8.target.fitness < g_best.target.fitness):
    model = model8
    g_best = g_best8
    nm = 8
g_best9 = model9.solve(problem_dict1)
if (g_best9.target.fitness < g_best.target.fitness):
    model = model9
    g_best = g_best9
    nm = 9
g_best10 = model10.solve(problem_dict1)
if (g_best10.target.fitness < g_best.target.fitness):
    model = model10
    g_best = g_best10
    nm = 10
g_best11 = direct(fitness_function, bounds=[(lb, ub)])
if (g_best11.fun < g_best.target.fitness):
    print("### => ATTENTION!")
    nm = 11
g_best12 = shgo(fitness_function, bounds=[(lb, ub)])
if (g_best12.fun < g_best.target.fitness):
    print("### => ATTENTION!")
    nm = 12

print(f"Model: {model1.name}, Solution: {g_best1.solution}, Fitness: {g_best1.target.fitness}")
print(f"Model: {model2.name}, Solution: {g_best2.solution}, Fitness: {g_best2.target.fitness}")
print(f"Model: {model3.name}, Solution: {g_best3.solution}, Fitness: {g_best3.target.fitness}")
print(f"Model: {model4.name}, Solution: {g_best4.solution}, Fitness: {g_best4.target.fitness}")
print(f"Model: {model5.name}, Solution: {g_best5.solution}, Fitness: {g_best5.target.fitness}")
print(f"Model: {model6.name}, Solution: {g_best6.solution}, Fitness: {g_best6.target.fitness}")
print(f"Model: {model7.name}, Solution: {g_best7.solution}, Fitness: {g_best7.target.fitness}")
print(f"Model: {model8.name}, Solution: {g_best8.solution}, Fitness: {g_best8.target.fitness}")
print(f"Model: {model9.name}, Solution: {g_best9.solution}, Fitness: {g_best9.target.fitness}")
print(f"Model: {model10.name}, Solution: {g_best10.solution}, Fitness: {g_best10.target.fitness}")
print(f"Model: {"DIRECT"}, Solution: {g_best11.x}, Fitness: {g_best11.fun}")
print(f"Model: {"SHGO"}, Solution: {g_best12.x}, Fitness: {g_best12.fun}")

print("Best model: ")
print(f"#{nm}, Model: {model.name}, Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

res = gp_minimize(fitness_function,   # the function to minimize
                  [(lb, ub)],         # the bounds on each dimension of x
                  initial_point_generator="random",
                  acq_func="gp_hedge",      # the acquisition function
                  n_calls=100,         # the number of evaluations of f
                  n_random_starts=80,  # the number of random initialization points
#                  noise=0.1**2,       # the noise level (optional)
                  n_jobs=4,
                  random_state=42)   # the random seed

"x^*=%.14f, f(x^*)=%.14f" % (res.x[0], res.fun)

g_best.solution[0]

plt.figure(figsize=FS, dpi=DPI)
# Set default sans-serif font
plt.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['mathtext.fontset'] = "cm"
plt.tick_params(axis='both', direction='in', length=5)

sns.set_theme(font="Times New Roman", font_scale=3)

plot_convergence(res)

def fitted_function(x):
    a1, = g_best.solution
    f = np.sin(x) + np.sin(a1*x)
    return f

plt.figure(figsize=FS, dpi=DPI)
# Set default sans-serif font
plt.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['mathtext.fontset'] = "cm"
plt.tick_params(axis='both', direction='in', length=5)

sns.set_theme(font="Times New Roman", font_scale=3)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")

x_fun = np.linspace(lb, ub, npoints*100)
fun = objective_function(x_fun)
y_data_fit = fitted_function(x_fun)

plt.scatter(x_data, y_data, label='Data', color=RED, s=100)
plt.plot(x_fun, y_data_fit, label='Fit', color=GREEN, linewidth=3)
plt.plot(x_fun, fun, label="$\\sin(x) + \\sin\\!\\left(\\frac{10x}{3}\\right)$", color=BLUE, linewidth=3)
plt.legend(loc='best')
plt.show()

##################################################################
D = 2
lb = 0.
ub =  5.
npoints = 11

with open('../../../../../Desktop/Data01/file.txt', 'w') as f:
    for i in range(npoints):
        xx = i*(ub-lb)/(npoints-1)+lb
        for j in range(npoints):
            yy = j*(ub-lb)/(npoints-1)+lb
            print(xx,',',yy, file=f)


filein = 'Test_opt_3D'
dataset = filein + '.csv'

df = pd.read_csv(dataset, encoding='cp1252')
df.info()
df.describe()

x_data1 = df.drop(['y_data', 'z_data'], axis=1).T.to_numpy()[0]
y_data1 = df.drop(['x_data', 'z_data'], axis=1).T.to_numpy()[0]
z_data1 = df.drop(['x_data', 'y_data'], axis=1).T.to_numpy()[0]

x_data = x_data1
y_data = y_data1
z_data = z_data1

def objective_function(x, y):
    f = 2*x**3 + 5*y**2
    return f

def fitness_function(params):
    a, b = params
    predicted = a * x_data**3 + b * y_data**2
    diff = predicted - z_data
    mae = np.mean(np.abs(diff))
    return mae

ME = 500
PS = 100

lb = -10.
ub =  10.
problem_dict2 = {
    "bounds": FloatVar(lb=(lb,) * D, ub=(ub,) * D, name="delta"),
    "obj_func": fitness_function,
    "minmax": "min",
    "log_to": None, #"file",
#    "log_file": "result.log",
}

model1 = PSO.AIW_PSO(epoch=ME, pop_size=PS, c1=2.05, c2=2.05, alpha=0.8)
model2 = PSO.OriginalPSO(epoch=ME, pop_size=PS, c1=2.05, c2=2.05, w_min=0.7, w_max=0.8)
model3 = MFO.OriginalMFO(epoch=ME, pop_size=PS)
model4 = EFO.DevEFO(epoch=ME, pop_size=PS, r_rate = 0.3, ps_rate = 0.95, p_field = 0.3, n_field = 0.5)
model5 = ASO.OriginalASO(epoch=ME, pop_size=PS, alpha = 50, beta = 0.2)
model6 = MA.OriginalMA(epoch=ME, pop_size=PS, pc = 0.85, pm = 0.15, p_local = 0.5, max_local_gens = 10, bits_per_param = 4)
model7 = ACOR.OriginalACOR(epoch=ME, pop_size=PS, sample_count = 25, intent_factor = 0.5, zeta = 1.0)
model8 = BBO.DevBBO(epoch=ME, pop_size=PS, p_m=0.01, n_elites=2)
model9 = GSKA.DevGSKA(epoch=ME, pop_size=PS, pb = 0.1, kr = 0.9)
model10= SA.GaussianSA(epoch=ME, pop_size=2, temp_init = 100, cooling_rate = 0.99, scale = 0.1)

g_best1 = model1.solve(problem_dict2)
model = model1
g_best = g_best1
nm = 1
g_best2 = model2.solve(problem_dict2)
if (g_best2.target.fitness < g_best.target.fitness):
    model = model2
    g_best = g_best2
    nm = 2
g_best3 = model3.solve(problem_dict2)
if (g_best3.target.fitness < g_best.target.fitness):
    model = model3
    g_best = g_best3
    nm = 3
g_best4 = model4.solve(problem_dict2)
if (g_best4.target.fitness < g_best.target.fitness):
    model = model4
    g_best = g_best4
    nm = 4
g_best5 = model5.solve(problem_dict2)
if (g_best5.target.fitness < g_best.target.fitness):
    model = model5
    g_best = g_best5
    nm = 5
g_best6 = model6.solve(problem_dict2)
if (g_best6.target.fitness < g_best.target.fitness):
    model = model6
    g_best = g_best6
    nm = 6
g_best7 = model7.solve(problem_dict2)
if (g_best7.target.fitness < g_best.target.fitness):
    model = model7
    g_best = g_best7
    nm = 7
g_best8 = model8.solve(problem_dict2)
if (g_best8.target.fitness < g_best.target.fitness):
    model = model8
    g_best = g_best8
    nm = 8
g_best9 = model9.solve(problem_dict2)
if (g_best9.target.fitness < g_best.target.fitness):
    model = model9
    g_best = g_best9
    nm = 9
g_best10 = model10.solve(problem_dict2)
if (g_best10.target.fitness < g_best.target.fitness):
    model = model10
    g_best = g_best10
    nm = 10
# g_best11 = direct(fitness_function, bounds=[(lb, ub)])*D
# if (g_best11.fun < g_best.target.fitness):
#     print("### => ATTENTION!")
#     nm = 11
# g_best12 = shgo(fitness_function, bounds=[(lb, ub)])*D
# if (g_best12.fun < g_best.target.fitness):
#     print("### => ATTENTION!")
#     nm = 12

print(f"Model: {model1.name}, Solution: {g_best1.solution}, Fitness: {g_best1.target.fitness}")
print(f"Model: {model2.name}, Solution: {g_best2.solution}, Fitness: {g_best2.target.fitness}")
print(f"Model: {model3.name}, Solution: {g_best3.solution}, Fitness: {g_best3.target.fitness}")
print(f"Model: {model4.name}, Solution: {g_best4.solution}, Fitness: {g_best4.target.fitness}")
print(f"Model: {model5.name}, Solution: {g_best5.solution}, Fitness: {g_best5.target.fitness}")
print(f"Model: {model6.name}, Solution: {g_best6.solution}, Fitness: {g_best6.target.fitness}")
print(f"Model: {model7.name}, Solution: {g_best7.solution}, Fitness: {g_best7.target.fitness}")
print(f"Model: {model8.name}, Solution: {g_best8.solution}, Fitness: {g_best8.target.fitness}")
print(f"Model: {model9.name}, Solution: {g_best9.solution}, Fitness: {g_best9.target.fitness}")
print(f"Model: {model10.name}, Solution: {g_best10.solution}, Fitness: {g_best10.target.fitness}")
# print(f"Model: {"DIRECT"}, Solution: {g_best11.x}, Fitness: {g_best11.fun}")
# print(f"Model: {"SHGO"}, Solution: {g_best12.x}, Fitness: {g_best12.fun}")

print("Best model: ")
print(f"#{nm}, Model: {model.name}, Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

def fitted_function(x, y):
    a1, a2 = g_best.solution
    f = a1 * x**3 + a2 * y**2
    return f

xx = x_data[18]
yy = y_data[18]
zz = z_data[18]
print(f"x_data: {xx}")
print(f"y_data: {yy}")
print(f"z_data: {zz}")
print(f"z_function: {objective_function(xx,yy)}")
print(f"z_fitted: {fitted_function(xx,yy)}")

plt.figure(figsize=FS, dpi=DPI)
# Set default sans-serif font
plt.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['mathtext.fontset'] = "cm"
plt.tick_params(axis='both', direction='in', length=5)

sns.set_theme(font="Times New Roman", font_scale=2)

lb = 0
ub = 5

x_fun = np.linspace(lb, ub, npoints*10)
y_fun = np.linspace(lb, ub, npoints*10)
X_fun, Y_fun = np.meshgrid(x_fun, y_fun)
fun = objective_function(X_fun, Y_fun)
z_data_fit = fitted_function(X_fun, Y_fun)

ax = plt.axes(projection='3d')
ax.scatter3D(x_data, y_data, z_data, label="Data", color=RED)
ax.plot_surface(X_fun, Y_fun, fun, rstride=1, cstride=1, label="$2x_1^3 + 5x_2^2$", cmap='viridis', antialiased=False)
ax.plot_surface(X_fun, Y_fun, z_data_fit, rstride=1, cstride=1, label="Fit", cmap='coolwarm', antialiased=False)
ax.legend(loc='best')
