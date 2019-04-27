
import numpy as np 
import sympy as sp 

import matplotlib.pyplot as plt 

def make_euler_equation(dc1, dc2, u, c1, lmbda):
    ''' Construct the euler equation.

    Args:
        dc1: derivative of lagrangian w.r.t c1
        dc2: derivative of lagrangian w.r.t c2
        u: within period utility function
        c1: consumption in period 1 
        lmbda: lambda
    '''

    x = dc2.subs(lmbda, sp.solve(dc1, lmbda)[0])

    euler_eq = sp.Eq(sp.Derivative(u(c1)),
                     sp.solve(x, sp.Derivative(u(c1)))[0]
                    )
    return euler_eq 



