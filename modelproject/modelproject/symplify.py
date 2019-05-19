
import sympy as sp 

def substitute_solution(what, where, equation):
    ''' Substitute the solution of `equation`
        w.r.t `what` into `where`.

    Args: 
        what: sp symbol
        where: sp expression
        equation: sp equation
    Returns:
        sp equation
    '''
    return where.subs(what, sp.solve(equation, what)[0])