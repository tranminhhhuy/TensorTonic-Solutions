import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code her
    # index of each parameter 
    for i in range(len(param)):   
        # loop while to check t time 
            m[i]= (beta1*m[i])+((1-beta1)*grad[i])
            v[i]= (beta2*v[i])+(1-beta2)*(grad[i]**2)
            
            m_t=m[i]/(1-beta1**t)
            v_t=v[i]/(1-beta2**t)

            
            param[i]=param[i]-lr*( (m_t)/(math.sqrt(v_t)+ eps) )
            
    param_new=param
    m_new=m
    v_new=v
    
        
    return param_new,m_new,v_new

    
    
    pass