def sort_list(l):
    l1 = []  
    while len(l1) != len(l):
        min_val = min(l)  
        l1.append(min_val) 
        l.remove(min_val)  
    print(l1)
sort_list([10, 9, 8])