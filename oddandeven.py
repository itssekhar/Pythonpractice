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
       
"""Using main function for to find an even and odd number """
def tofindoddoreven(n):
    if n%2 == 0 :
        print("even number")
    elif n%2!=0:
        print("odd number")

if __name__ == "__main__":
    n = int(input("Enter n number:"))
    tofindoddoreven(n)