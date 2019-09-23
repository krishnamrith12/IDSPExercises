

def evenOdd(x):
    if not x:
        print("empty")
        return    
    if x[0] %2==0:
        print(x[0], "is even")
	evenOdd(x[1:])
    return "Finished"  

print(evenOdd([0,1,2,3,4]))
