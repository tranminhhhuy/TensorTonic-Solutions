def independence_test(p_a: float, p_b: float, p_a_and_b: float) -> dict:
    """
    Returns the rounded product and independence decision in a dictionary.
    """
    # check  two  result  : 
    # If they are equal (within floating-point tolerance), the events are independent.
    mul_a_b= p_a*p_b
    if  p_a_and_b== mul_a_b:
        result = True
    else: 
        result  = False
    return {"p_a_times_p_b": mul_a_b, "is_independent": result}
    
    pass