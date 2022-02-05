# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(José-Manuel Martin Coronado, Instituto de Econometría de Lima)
"""

### Parquetes ####
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (11, 5)  #set default figure size
import numpy as np
from numpy import exp
from scipy.integrate import odeint

###Parámetros iniciales###
pop_size = 3.3e7 #33 MILLONES PERU
γ = 1 / 18
σ = 1 / 5.2
R0e=1.6

def F(x, t, R0=R0e):
    """
    Time derivative of the state vector.

        * x is the state vector (array_like)
        * t is time (scalar)
        * R0 is the effective transmission rate, defaulting to a constant

    """
    s, e, i = x

    # New exposure of susceptibles
    β = R0(t) * γ if callable(R0) else R0 * γ
    ne = β * s * i

    # Time derivatives
    ds = - ne
    de = ne - σ * e
    di = σ * e - γ * i

    return ds, de, di

###Valores Iniciales###
i_0 = 1e-7
e_0 = 4 * i_0
s_0 = 1 - i_0 - e_0
x_0 = s_0, e_0, i_0

def solve_path(R0, t_vec, x_init=x_0):
    """
    Solve for i(t) and c(t) via numerical integration,
    given the time path for R0.

    """
    G = lambda x, t: F(x, t, R0)
    s_path, e_path, i_path = odeint(G, x_init, t_vec).transpose()

    c_path = 1 - s_path - e_path     # cumulative cases
    return i_path, c_path


### Ejemplo1
t_length = 550  #JM: 1 AÑO
grid_size = 1000
t_vec = np.linspace(0, t_length, grid_size)

R0_vals = np.linspace(1.6, 3.0, 6)
labels = [f'$R0 = {r:.2f}$' for r in R0_vals]
i_paths, c_paths = [], []

for r in R0_vals:
    i_path, c_path = solve_path(r, t_vec)
    i_paths.append(i_path)
    c_paths.append(c_path)

def plot_paths(paths, labels, times=t_vec):

    fig, ax = plt.subplots()

    for path, label in zip(paths, labels):
        ax.plot(times, path, label=label)

    ax.legend(loc='upper left')

    plt.show()
    
plot_paths(i_paths, labels)
plot_paths(c_paths, labels)


### Ejemplo2

def R0_mitigating(t, r0=3, η=1, r_bar=1.6):
    R0 = r0 * exp(- η * t) + (1 - exp(- η * t)) * r_bar
    return R0

η_vals = 1/5, 1/10, 1/20, 1/50, 1/100
labels = [fr'$\eta = {η:.2f}$' for η in η_vals]

fig, ax = plt.subplots()

for η, label in zip(η_vals, labels):
    ax.plot(t_vec, R0_mitigating(t_vec, η=η), label=label)

ax.legend()
plt.show()

i_paths, c_paths = [], []

for η in η_vals:
    R0 = lambda t: R0_mitigating(t, η=η)
    i_path, c_path = solve_path(R0, t_vec)
    i_paths.append(i_path)
    c_paths.append(c_path)
    
plot_paths(i_paths, labels)
plot_paths(c_paths, labels)


### Ejemplo3
i_0 = 25_000 / pop_size
e_0 = 75_000 / pop_size
s_0 = 1 - i_0 - e_0
x_0 = s_0, e_0, i_0


R0_paths = (lambda t: 0.5 if t < 30 else 2,
            lambda t: 0.5 if t < 120 else 2)

labels = [f'scenario {i}' for i in (1, 2)]

i_paths, c_paths = [], []

for R0 in R0_paths:
    i_path, c_path = solve_path(R0, t_vec, x_init=x_0)
    i_paths.append(i_path)
    c_paths.append(c_path)

plot_paths(i_paths, labels)
ν = 0.01
paths = [path * ν * pop_size for path in c_paths]
plot_paths(paths, labels)
paths = [path * ν * γ * pop_size for path in i_paths]
plot_paths(paths, labels)

