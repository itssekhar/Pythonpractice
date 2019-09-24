""" Linear Search """

def linear(data,target):
    for i in range(0,len(data)):
        if data[i] == target:
            return True
    return False

if __name__ =="__main__":
    data=[1,2,4,6,7,8,30,10]
    print(linear(data,20))
    