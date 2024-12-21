import math
def abc(a,size):
    power= int(math.pow(2,size))
    o= 0
    i= 0
    for o in range(0,abc):
        for i in range(0,abc):
            if o & (1<<i) > 0:
                print(a[i])
        print("")   
size=int(input("enter size :/"))
a=[] 
for x in range(0,size):
    n=int(input("enter a num"))    
    a.append(n)
abc(a,len(a))