def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """

    #  they want  compute probability  of two space have intersection , compute their union , both complements
    P_AUB=  float(p_a+ p_b-p_a_and_b) # combine 
    pA_C= float(1 -p_a)
    pB_C=float(1 - p_b)
    pA_B_c= float(p_a-p_a_and_b)
    result=[]
    result.append(P_AUB)
    result.append(pA_C)
    result.append(pB_C)
    result.append(pA_B_c)
    return result
    
    pass