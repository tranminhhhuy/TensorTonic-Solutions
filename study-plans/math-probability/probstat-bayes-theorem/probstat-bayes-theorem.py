def bayes_theorem(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
    """
    Returns the posterior probability rounded to four decimals.
    """


    #stage 1 
    p_B = p_b_given_a*p_a+ p_b_given_not_a*(1-p_a)
    pa_b= (p_b_given_a*p_a)/p_B
    pa_b=float(pa_b)

    pa_b=round(pa_b,4 )
    return pa_b

    pass