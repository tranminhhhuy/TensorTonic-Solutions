import numpy as np
import math 
def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """

  
    u_mean= 0#  gain variable for u_mean
    for i in range(len(x)):
        # stage1 :  calculate the sample mean x_
        u_mean+= x[i]
    # complete compution of u_mean
    u_mean=u_mean/len(x)

    total_squared_deivation= 0
    for j in range(len(x)):
        sum_and_square= (x[j]-u_mean)**2
        total_squared_deivation+= sum_and_square
    # result 
    total_squared_deivation=total_squared_deivation/(len(x)-1)
    sample_standard=math.sqrt(total_squared_deivation)
    
    return { "variance": total_squared_deivation, "std_dev": sample_standard }

    pass