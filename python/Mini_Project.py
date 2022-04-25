# Goal is to plot a single graph of probability of a two state system, then later multiple graphs. Probality equals
# the multiplicity of the macrostate over the multiplicity of the entire system, which is in line 43 N is the total
# amount of chances of the system and n being the secondary amount.(ex. total amount of coins flipped is 100(N),
# with 20 head and 80(n) tails.) multiplicity of the entire system is calculated use 2^N, 2 being there because it's
# a two state system and N being the total amount of coins flipped. multiplicity of a macrostate is calculated using
# Omega=N!/n!*(N-n)!
from math import *
from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt

# Future N for multiple probabilities, and n should be going 0 to N
# N = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
N = 100
n = linspace(0, N)


# Function of probability using the multiplicities of the macro and total of all
def probability_function(N, n):
    p = (1 / 2 ** N) * (factorial(N)) / (factorial(n) * factorial(N - n))

    return p


# Definition for factorial:
def factorial(x):

    fact = 1
    for k in range(1, x + 1):
        fact = fact * k
    return fact


# Print statement to test if probability works
print(probability_function(100, 50))
# Crete a for loop that reads multiple values of n
for i in n:

    
# Plotting n values on the x-axis and the probability on the y-axis
# plt.plot(n, probability_function, color='black')
# plt.xlabel(r'$n-value$')
# plt.ylabel(r'$probability$')
# plt.show()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~IT BE WORKING!!!!!~~~~~~
from math import *
from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt

N = 100


def n_array(big_n):
    n_ray = []
    for i in range(0, N + 1, 2):
        if i <= N + 1:
            n_ray.append(i)
            # i = n + 2
        elif i > N + 1:
            break
    return n_ray


def factorial(n_input):
    if type(n_input) != int:
        factorial_n_array = []
        fact = 1
        for i in n_input:
            for k in range(1, i + 1):
                fact = fact * k
            factorial_n_array.append(fact)
        return factorial_n_array
    else:
        fact = 1
        for k in range(1, n_input + 1):
            fact = fact * k
        return fact


def probability_function(n_ray_ray):
    probability_array = []
    for i in n_ray_ray:
        probability = (1 / 2 ** N) * (factorial(N)) / (factorial(i) * factorial(N - i))
        probability_array.append(probability)
    return probability_array


# print(n_array(N))
# print(factorial(N))
# print(factorial(n_array(N)))
# print(probability_function(n_array(N)))

plt.plot((n_array(N)), probability_function(n_array(N)), color='black')
plt.xlabel(r'n-value')
plt.ylabel(r'probability')
plt.show()
