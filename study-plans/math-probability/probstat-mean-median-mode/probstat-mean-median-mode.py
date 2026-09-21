import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    # make variable for each results : 
    total_mean =0
    total_median =[] 
    total_mode=0
    max =0
    # make  loops  to take each elements  in list 




    if len(x)==1:
        total_mean=x[0]
        total_median=x[0]
        total_mode=x[0]
        return {"mean": float(total_mean), "median": float(total_median), "mode": float(total_mode)}
        breakpoint




    
    for i in range(len(x)):
        count = 0 # for stage3 for each loop i we restart  again to count frequency of next elements 
        # stage1 : 
        total_mean+= x[i]

        

        
        # stage3 :solve mode 
        for j in range (len(x)):
            if  x[i]==x[j]:
                count+=1


        # two  condition after check frequency of x[i]
        # compare with max variable :
        if  count > max :
            max =count 
            total_mode= x[i]
        
        #  count = max 
        elif  count ==max : # because we gain total_mode = variable frequency 
            if x[i] < total_mode:
                total_mode= x[i]
        
            
            
    # if total_mode == 0 :
     # stage 2 : sovle median 
     # two 2 condition : odd and even  
    x=sorted(x)
    if len(x) %2 != 0 : # odd = x [(n+1)/2 ]
        total_median = x[ len(x) //2]
    else:
        total_median= (x[len(x)//2]+ x[len(x)//2-1 ])/2 
    
        

    # final step mean:
    total_mean=total_mean/len(x)
    

    return {"mean": float(total_mean), "median": float(total_median), "mode": float(total_mode)}
    pass