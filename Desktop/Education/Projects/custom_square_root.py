sum = 0
n = 0
x = float(input("Enter a number to find its square root: "))

if (x < 0):
    print("The square root of {} is imaginary.".format(x))
    
else:
    
    count = 0
    count2 = 0
    
    while sum < x and x >= 1:
        n += 1
        sum += ((2*n) -1)
        count2 += 1
    
    if sum > x or x < 1:
        
        if x < 1:
            r = 1
           
        else:
            sum -= ((2*n) -1)
            n -= 1
            r = x - sum 
            
        hi = r
        lo = 0
        y = (n + ((hi + lo)/2))**2
    
        while abs(x-y)>.0000001:
            
            if y > x:
                
                hi = ((hi + lo)/2)
                y = (n + ((hi + lo)/2))**2
                if abs(x-y)<=.0000001:
                    n = n + hi
                    
            elif x > y: 
                
                lo = ((hi + lo)/2)
                y = (n + ((hi + lo)/2))**2
                if abs(x-y)<=.0000001:
                    n = n + lo
                    
            count += 1
                                
    n = round(n,5)
    print("The square root of {} is {}".format(x,n))
    print("Integer took {} run throughs.".format(count2))
    print("Decimal took {} run throughs.".format(count))