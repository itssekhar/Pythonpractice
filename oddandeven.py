num=int(input("enter a numer:"))
res=num%2

if(res>0):
    print("odd number")
else:
    print("even number")

 """ Using function"""    

 def Number(n):
    res=n%2
    if res>0:
        return "odd" 
    else:
        return "even"
    
Number(2)
       
