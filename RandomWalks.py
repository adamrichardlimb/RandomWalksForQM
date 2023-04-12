#-- Begin importing modules.

import time
import numpy as n
from pylab import *
from random import *
import math as m
from random import randrange
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.constants import hbar, pi, m_e


#-- Finish importing modules.



#-- Begin defining function to loop.


def drunkard(max_step_number, boundary, dimensions):
    # Function which defines the drunkard walk.
    
    """A function that takes randomly selects a direction to walk in, returning
    the number of steps and the position at which the walk was stopped."""
        
    
    pos = n.zeros((dimensions), dtype=int)
    # Begin at the origin, in three dimensions.
    
    for i in range(0, dimensions):
        pos[i - 1] = randrange(1, boundary, 1)
    
    step_no = 0
    # Always start with zero steps.
    
    for i in range(0, max_step_number):
        if len(pos[pos == 0]) != 1:
            # Get array of position values equal to zero, if length of array is equal to one, call of the walk.
    
            if n.sum(n.square(pos)) < (boundary ** 2.0):
                
                step_no = step_no + 1
                #Increment step_no first, so when loop breaks halfway, output is correct.
                
                step_direction = randrange(0, dimensions, 1)
                # Chooses a direction to walk in.
        
                step_distance = randrange(-1, 2, 2)
                # Chooses wheter to increment the direction by +/- 1.
        
                pos[step_direction] += step_distance
                # Increment direction chosen by said amount.
        
            else:
                # Once done with walk, output step number.
                break

        else:
            break            
            
    return step_no
        
        
#-- Finish defining function to loop.


#-- Begin defining function to call the walk.

def begin_walks(max_step_number, boundary, dimensions, amount_of_walks, mass):
    
    """A function that calls the drunkard walk function as many times as 
    required and then generates a graph and finds the energy of the system."""
    
    constant = ( (hbar ** 2.0) /  (mass * (boundary ** 2.0) ) )
    walk_number = 0
    # Create constant, start with zero walks.
    
    step_array = zeros((amount_of_walks), dtype = int)
    # This array will store the 
    # number of steps before
    # arrest for each walk.
    
    
    while walk_number != amount_of_walks: 
    # Loops function call and stores step_no
    # in our position_array.
    
        step_array[walk_number] = drunkard(max_step_number, boundary, dimensions)
        # Sets the value of the array
        # entry corresponding to each
        # walk to its respective
        # step number value.
        
        walk_number = walk_number + 1
        # Increment walk number by one.
        
    log_population = zeros(( amax(step_array) ), dtype = float)
    # Create array with length of largest amount of steps taken.
    # This array will count the population at a 

    number_of_steps = zeros(( amax(step_array) ), dtype = float)
    # Create array counting up the amount of steps taken to reach boundary.
    
    for i in range(0,amax(step_array)):
        
        log_population[i] = - m.log( len( step_array[ step_array > i ] ) )
    
        number_of_steps[i] = i + 1
                    
    #plt.plot(number_of_steps, log_population)
    lambda_rate, _, _, _, _ = linregress(number_of_steps, log_population)

    # Plot the graph. 
    
    #plt.show()
    energy_component = dimensions * ((lambda_rate) * (boundary ** 2))
    compare_2 = ( (pi ** 2) / 8 ) * dimensions
    return constant, energy_component, compare_2
    
#-- Finish defining function to begin the walks.



#-- Begin defining function to generate theoretical values.

def theoretical(dimensions, mass, boundary):
    
    Theoretical_Energy = ( dimensions * (hbar ** 2.0) /  (mass * (boundary ** 2.0) ) ) * ( (pi ** 2.0) / 8 )
    
    return Theoretical_Energy

#-- End defining function to generate theoretical values.



#-- Begin function call to build multi-boundary and dimensional graphs.

def graph_range(max_step_number, boundary, dimensions, amount_of_walks, mass):
    
    constant, compare_1, compare_2 = begin_walks(max_step_number, boundary, dimensions, amount_of_walks, mass)
    E_J = constant * compare_1
    #comparison = compare_1 + compare_2
    #error_amount = comparison / (compare_2)
    #error_J = error_amount * E_J
    E_eV = E_J / (1.6e-19)
    #error_eV = error_amount * E_eV
    
    #Energy_Theory = theoretical(dimensions, mass, boundary)
    
    return E_J

#-- End function call to build multi-boundary and dimensional graphs.


#-- Begin types of variable to change and plot.

stop_boundary = 50
boundaries = zeros(stop_boundary - 2)
Computational_Energy = zeros(stop_boundary - 2)
#Computational_Energy_Error = zeros(stop_boundary - 2)
Theoretical_Energy = zeros(stop_boundary - 2)
#x_error = zeros(stop_boundary - 2)
Computation_Time = zeros(stop_boundary - 2)

for i in range(2, stop_boundary, 1):
    #time_start = time.clock()
    boundaries[i - 2] = i
    Computational_Energy[i - 2] = graph_range(5000, i, 2, 5000, m_e)
    #Computation_Time[i - 2] = (time.clock() - time_start)
    
print(Computational_Energy)
Computational_Line_Boundary = plt.plot(boundaries, Computational_Energy, label = 'Computational Energy', color = 'red')
plt.xlabel('Boundary / Metres')
plt.ylabel('Energy / Joules')
plt.legend()
plt.show()


"""
plt.plot(boundaries, Computation_Time)
plt.xlabel('Boundary / Metres')
plt.ylabel('Computation Time / seconds')
plt.legend()
plt.show()
"""

"""
stop_dimension = 21
dimensions = zeros(stop_dimension - 1)
Computational_Energy = zeros(stop_dimension - 1)
Computational_Energy_Error = zeros(stop_dimension - 1)
Theoretical_Energy = zeros(stop_dimension - 1)
x_error = zeros(stop_dimension - 1)

for i in range(1, stop_dimension, 1):
    dimensions[i - 1] = i
    Computational_Energy[i - 1], Computational_Energy_Error[i - 1], Theoretical_Energy[i - 1] = graph_range(20000000, 8, i, 5000, m_e)
        

plt.plot(dimensions, Computational_Energy, label = 'Computational Energy', color = 'red')
plt.plot(dimensions, Theoretical_Energy, label   = 'Theoretical Energy', color = 'green')
#plt.errorbar(dimensions, Computational_Energy, Computational_Energy_Error, color = 'red')
plt.xlabel('Dimensions')
plt.ylabel('Energy / Joules')
plt.legend()
plt.show()
"""

#-- End types of variable to chnage and plot.

#-- Finish .py file.
