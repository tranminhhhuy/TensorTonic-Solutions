def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    result=x0
    i=0
    while i < steps :
        i+=1
        result= result - lr*( 2*a*result  + b )
    return result
    pass