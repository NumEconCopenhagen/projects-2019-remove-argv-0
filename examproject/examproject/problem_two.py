
import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt 

def func_vt(v_tm1, x_t, delta):
    'v_t = delta*v_{t-1} + x_t'
    return delta*v_tm1 + x_t

def func_st(s_tm1, c_t, omega):
    's_t = omega*s_{t-1} + c_t'
    return omega*s_tm1 + c_t


def plot_single_shock(y_vec, pi_vec):
    ''' Plot for question 3
    '''
    fig, ax = plt.subplots(figsize = (12,8))

    ax.plot(y_vec, color = 'red', label= '$y^*_t$')
    ax.plot(pi_vec, color = 'blue', label = '$\pi^*_t$')

    ax.grid(which='major', alpha=0.8, linestyle='dotted')
    ax.set_xlabel('$t$', fontsize = 18)
    ax.set_ylabel('$y^*_t$, $\pi^*_t$', fontsize = 18)
    ax.set_title("Evolution of $y^*$, $\pi^*$", fontsize = 20)
    ax.legend(fontsize = 18)
    
    return fig


def plot_random_shocks(y_vec, pi_vec):
    ''' Figure for question 4
    '''
    fig, ax = plt.subplots(figsize = (12,8))

    ax.plot(y_vec, color = 'red', label= '$y^*_t$', linewidth=0.5)
    ax.plot(pi_vec, color = 'blue', label = '$\pi^*_t$', linewidth = 0.5)

    ax.grid(which='major', alpha=0.8, linestyle='dotted')
    ax.set_xlabel('$t$', fontsize = 18)
    ax.set_ylabel('$y^*_t$, $\pi^*_t$', fontsize = 18)
    ax.set_title("Evolution of $y^*$, $\pi^*$", fontsize = 20)
    ax.legend(fontsize = 18)
    
    return fig



def plot_correlation_and_phi(phi_space, correlation):
    ''' Figure 1 for question 5
    '''
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(phi_space, correlation, color = 'blue')

    ax.grid(which='major', alpha=0.8, linestyle='dotted')
    ax.set_xlabel('$\phi$', fontsize = 18)
    ax.set_ylabel('$corr(y^*_t, \pi^*_t)$', fontsize = 18)
    ax.set_title("Correlation btwn. $y^*_t, \pi^*_t$ for varying $\phi$", fontsize = 20)
    return fig
