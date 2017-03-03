def secondSmallest(lst):
    if len(lst) <= 1:
        return None

    else:

        init = 0
        first = 0
        second = 0
        
        for value in lst:
            if init == 0:
                    first = value
                    
            if init == 1:
                    second = value
                    
            if value < first:
                    second = first
                    first = value
                    
            if value > first:
                    if value < first:
                        second = value
                        
                    if value < second:
                        second = value
                        
                    if second == first:
                        second = value

            init += 1
            
        print('Second Smallest Value:',second)
        print('Smallest Value:',first)


lst = [99,44,55,67,34,77,44,55,44,88,999,87]
secondSmallest(lst)


