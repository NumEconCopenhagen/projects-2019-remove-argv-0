
import numpy as np 


rho = 2
beta = 0.96
gamma = 0.1
w = 2
b = 1
Delta = 0.1


def consumption(h_t: float, l_t: bool):
    ''' Consumption function
    
    Args:
        h_t: human capital level
        l_t: state of employment
        
    Returns:
        float
    '''
    if l_t == True:
        return w*h_t
    return b


def utility_cons(c_t: float):
    ''' Utility of consumption
    
    Args:
        c_t: consumption
    
    Returns:
        float
    '''
    return c_t**(1-rho) / (1 - rho)


def utility_work(l_t: int):
    ''' (dis)utility of work
    
    Args:
        l_t: state of employment
        
    Returns:
        float
    '''
    return gamma*l_t



def total_utility(c_t: float, l_t: bool):
    ''' Total utility of agent.
    
    Args:
        c_t: consumption in period t
        l_t: state of employment in period t       
    '''
    return utility_cons(c_t) - utility_work(l_t)


def human_capital_accumulation(h1: float, l1: bool, rng: np.random.RandomState):
    ''' HC in period 2
    
    Args: 
        h1: HC in period 1
        l1: employment state in period 1
        rng: random number generator.
    
    Returns:
        float
    '''
    return h1 + l1 + (rng.uniform() > 0.5)*Delta
