""" Binary search for sorted data"""

def binary(data,target):
    if len(data)==0:
        return False
    else:
        midpoint = len(data)//2
        if data[midpoint]==target:
            return True
        else:
            if target<data[midpoint]:
                return binary(data[:midpoint],target)
            else:
                return binary(data[midpoint+1:],target)
if __name__ == "__main__":
    ls = [2,3,5,6,8,9,10,30]
    print(binary(ls,34))
            
                