def max_list_iter(int_list):

    if type(int_list) != list:
        raise ValueError("Not a list")
    
    if not int_list:
        return None
    
    high = int_list[0]

    for i in int_list:
        if i > high:
            high = i
    return high
pass

def reverse_rec(int_list):
     if type(int_list) != list:
        raise ValueError("Not a list")
    
     if len(int_list) == 0:
        return []
     else: 
         return [int_list[-1]] + reverse_rec(int_list[:-1])
     
pass


def bin_search(target, low, high, int_list):

    if type(int_list) != list:
        raise ValueError("Not a list")
    
    if len(int_list) == 0:
        return None

    if low <= high:
        mid = (high + low) // 2
        
        if int_list[mid] == target:
            return mid  
        elif int_list[mid] < target:
            return bin_search(target, mid + 1, high, int_list)
        else:
            return bin_search(target, low, mid - 1, int_list)
    else:
        return None  
pass

