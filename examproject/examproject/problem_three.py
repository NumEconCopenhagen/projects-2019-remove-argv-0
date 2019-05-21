
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

def plot_histogram(betas):
    fig, ax = plt.subplots(figsize = (12,8))

    ax.hist(betas[:,0], alpha = 0.3, label = r'$\beta_1$', bins = 100)
    ax.hist(betas[:,1], alpha = 0.3, label = r'$\beta_2$', bins = 100)
    ax.hist(betas[:,2], alpha = 0.3, label = r'$\beta_3$', bins = 100)
    ax.legend(fontsize = 18)
    ax.set_xlabel(r'$\beta_k$', fontsize = 18)
    ax.set_ylabel('count', fontsize = 18)
    ax.set_title("Histogram of budget shares")
    return fig 



def plot_excess_demand(pp1, pp2, dd1, dd2, dd3):
    fig = plt.figure(figsize=(2*12,2*4))
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')

    ax1.plot_surface(pp1.reshape(30,30), pp2.reshape(30,30), dd1.reshape(30,30), cmap = plt.cm.viridis, alpha = .8)
    ax2.plot_surface(pp1.reshape(30,30), pp2.reshape(30,30), dd2.reshape(30,30), cmap = plt.cm.viridis, alpha = .8)
    ax3.plot_surface(pp1.reshape(30,30), pp2.reshape(30,30), dd3.reshape(30,30), cmap = plt.cm.viridis, alpha = .8)

    ax1.set_title("$z_1$", fontsize = 18)
    ax2.set_title("$z_2$", fontsize = 18)
    ax3.set_title("$z_3$", fontsize = 18)

    ax1.set_xlabel('$p_1$', fontsize = 18)
    ax1.set_ylabel('$p_2$', fontsize = 18)
    ax2.set_xlabel('$p_1$', fontsize = 18)
    ax2.set_ylabel('$p_2$', fontsize = 18)
    ax3.set_xlabel('$p_1$', fontsize = 18)
    ax3.set_ylabel('$p_2$', fontsize = 18)

    ax1.set_ylim(10,1)
    ax2.set_ylim(10,1)
    ax3.set_ylim(10,1)

    ax1.view_init(30, 360-30)
    ax2.view_init(30, 360-30)
    ax3.view_init(30, 360-30)
    return fig
