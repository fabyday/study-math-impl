

# not
def simple_random(n : int, seed : int): 
    """
        size
    Args:
        n (int): size
        seed (int) : seed
    return : 
        random interger list , random float list
    """
    l0 = seed 
    l = [l0]
    x = []
    # I assumed it 32 bit.(but python is not data size sensitive... so It is super naive impl.)
    min_val = 1
    max_val =  2147483647 #2**32 - 1
    if  l0 < min_val  :
        raise ValueError("seed can't be negative")
    
    if max_val < l0 : 
        raise ValueError("seed can't be greater than 2^32-1 (8bit)")
    
    for i in range(n):
        li = (7**5 * l[-1]) % max_val
        l.append(li)
        xi = li/(max_val)
        x.append(xi)
        
        
    return l[1:], x


def unix_like_random_generator(n, seed):
    """_summary_

    Args:
        n (_type_): _description_
        seed (_type_): _description_
    """
    
    
    
    l = []
    r = []
    



if __name__ == "__main__":
        
    rand_i1, rand_f1 = simple_random(20, seed=2394)
    rand_i2, rand_f2 = simple_random(20, seed=132)
    print(rand_i1)
    print(rand_i2)
    print(rand_f1)
    print(rand_f2)
    
    
    
    
    
    
    
    

        
        
        
        