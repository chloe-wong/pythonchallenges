import matplotlib.pyplot as plt
from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import numpy as np
import math
from scipy.special import factorial

def ConstantComplexity():
    x = [2, 4, 6, 8, 10, 12]
    y = [2, 2, 2, 2, 2, 2]
    # y = [2, 4, 6, 8, 10, 12] # Try this for Linear complexity
    plt.plot(x, y, 'b')
    xlabel('x')
    ylabel('y')
    title('Constant Complexity: O(1)')
    show()



def Quadratic():
    x = np.linspace(-5,5,100)
    y = x**2
    fig = plt.figure()
    axes = fig.add_subplot(1,1,1)
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('zero')
    xlabel('x')
    ylabel('y')
    title("Quadratic Complexity: O(n^2)")
    plt.plot(x, y, 'r')
    show()

def Logarithm():
    x = np.linspace(0,10,100)
    y = np.log(x)
    fig = plt.figure()
    axes = fig.add_subplot(2,1,1)
    axes.spines['bottom'].set_position('zero')
    xlabel('x')
    ylabel('y')
    title("Logarithmic Complexity: O(log(n))")
    plt.plot(x, y)
    show()

def Exponential():
    x = np.linspace(-10,10,100)
    y = np.exp(x)
    fig = plt.figure()
    axes = fig.add_subplot(2,1,1)
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('zero')
    xlabel('x')
    ylabel('y')
    title("Exponential Complexity: O(2^n)")
    plt.plot(x, y)
    show()

def Factorial():
    x = np.linspace(0,10,10)
    y = factorial(x)
    fig = plt.figure()
    axes = fig.add_subplot(1,1,1)
    axes.spines['left'].set_position('center')
    xlabel('x')
    ylabel('y')
    title("Factorial Complexity: O(n!)")
    plt.plot(x, y)
    show()
