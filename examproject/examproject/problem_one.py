
import numpy as np 
import matplotlib.pyplot as plt 

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





def plot_period_2_solution(h_vec, solutions):
    ''' Plot for question 1
    '''
    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,4))

    ax1.plot(h_vec, [s[0] for s in solutions])
    ax1.set_title('Labor supply', fontsize = 18)
    ax1.set_xlabel(r'$h_2$', fontsize = 18)
    ax1.set_ylabel(r'$l_2$', fontsize = 18)



    ax2.plot(h_vec, [s[1] for s in solutions])
    ax2.set_title('Utility', fontsize = 18)
    ax2.set_xlabel(r'$h_2$', fontsize = 18)
    ax2.set_ylabel(r'$v_2^*$', fontsize = 18)

    ax1.grid(which='major', alpha=0.8, linestyle='dotted')
    ax2.grid(which='major', alpha=0.8, linestyle='dotted')

    fig.suptitle("Period 2 solution", fontsize = 24, y = 1.05)
    plt.tight_layout()
    plt.legend()
    return fig



def plot_period_1_solution(h_vec, solutions):
    ''' Plot for question 2
    '''
    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,4))

    ax1.plot(h_vec, [s[0] for s in solutions])
    ax1.set_title('Labor supply', fontsize = 18)
    ax1.set_xlabel(r'$h_1$', fontsize = 18)
    ax1.set_ylabel(r'$l_1$', fontsize = 18)

    ax2.plot(h_vec, [s[1] for s in solutions])
    ax2.set_title('Utility', fontsize = 18)
    ax2.set_xlabel(r'$h_1$', fontsize = 18)
    ax2.set_ylabel(r'$v_1^*$', fontsize = 18)

    ax1.grid(which='major', alpha=0.8, linestyle='dotted')
    ax2.grid(which='major', alpha=0.8, linestyle='dotted')

    fig.suptitle("Period 1 solution", fontsize = 24, y = 1.05)
    plt.tight_layout()
    
    return fig


def plot_period_1_solution_with_vbands(h_vec, solutions, lowest_work_solution):
    ''' Plot for question 3
    '''
    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,4))

    ax1.plot([w*h - b for h in h_vec], [s[0] for s in solutions])
    ax1.axvspan(w*lowest_work_solution-b, 0, alpha=0.3, color='blue')
    ax1.axvline(w*lowest_work_solution-b, color = 'black')
    ax1.axvline(0, color = 'black')
    ax1.set_title('Labor supply', fontsize = 18)
    ax1.set_xlabel(r'$w\cdot h_1 - b$', fontsize = 18)
    ax1.set_ylabel(r'$l_1$', fontsize = 18)

    ax2.plot([w*h - b for h in h_vec], [s[1] for s in solutions])
    ax2.axvspan(w*lowest_work_solution-b, 0, alpha=0.3, color='blue')
    ax2.axvline(w*lowest_work_solution-b, color = 'black')
    ax2.axvline(0, color = 'black')
    ax2.set_title('Utility', fontsize = 18)
    ax2.set_xlabel(r'$w\cdot h_1 - b$', fontsize = 18)
    ax2.set_ylabel(r'$v_1^*$', fontsize = 18)

    ax1.grid(which='major', alpha=0.8, linestyle='dotted')
    ax2.grid(which='major', alpha=0.8, linestyle='dotted')

    fig.suptitle("Period 1 solution", fontsize = 24, y = 1.05)
    plt.tight_layout()
    return fig
