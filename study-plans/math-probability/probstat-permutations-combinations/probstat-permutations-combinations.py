def perms_and_combs(n: int, r: int) -> list:
    """
    Returns permutations, combinations, and n factorial as integers.
    """
    

    # make loop for down n -1  
    total_n=1
    totaln_r=1 
    total_r=1 
    c = n -r 
    for i in range(n):
        total_n*=i+1
        # calculate n_r ! 
        if i < c :
            totaln_r*=i+1 
        #  calculate r ! 
        if  i < r : 
            total_r*= i +1 

    #  permutation 
    per=int (total_n/ totaln_r)
    # combination 
    com= int(total_n/ (totaln_r*total_r))
    # total_n
    toal_n= int(total_n)
    

    
    result = []
    result.append(per)
    result.append(com)
    result.append(total_n)  
    return result
    pass