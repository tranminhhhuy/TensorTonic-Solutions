def conditional_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns both rounded conditional probabilities in the required order.
    """
    result = []


    pa_b= round(p_a_and_b/p_b , 4 )

    pb_a= round(p_a_and_b/p_a, 4)
    result.append(pa_b)
    result.append(pb_a)

    return result
    
    
    pass