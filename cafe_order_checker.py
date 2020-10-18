#time O(S) --> O(N), number of elements in S array
#space O(2) --> O(1), only space created from candidates array

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    
    
    D, T = 0,0
    candidates = [0] * 2
    if len(take_out_orders) == 0:
        candidates[0] = None
    else:
        candidates[0] = take_out_orders[T]
    if len(dine_in_orders) != 0:
        candidates[1] = dine_in_orders[D]
    else:
        candidates[1] = None
    
    
    
    for order in served_orders:
        if order not in candidates:
            return False
        
        elif order == candidates[0]:
            T += 1
            if T >= len(take_out_orders):
                candidates[0] = None
            else:
                candidates[0] = take_out_orders[T]

        else:
            D += 1
            if D >= len(dine_in_orders):
                candidates[1] = None
            else:
                candidates[1] = dine_in_orders[D]
                
    return ( (D == len(dine_in_orders)) and (T == len(take_out_orders)) )
