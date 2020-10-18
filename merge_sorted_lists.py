#merge two sorted lists
#time O(A+B) A - num of elements in my_list, B - num of elements in alices_list
#space O(A+B)

def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list

    out = [None] * (len(my_list)+len(alices_list))
    n = len(my_list) - 1
    m = len(alices_list) - 1
    w = 0
    i,j = 0,0
    while w< len(out):
        one = my_list[i] if i<= n else float("inf")
        two = alices_list[j] if j <= m else float("inf")
        
        if one < two:
            out[w] = one
            i += 1
        else:
            out[w] = two
            j += 1
        w += 1
    

    return out
