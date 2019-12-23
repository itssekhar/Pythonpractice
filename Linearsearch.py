""" Linear Search """

def linear(data,target):
    for i in range(0,len(data)):
        if data[i]==target:
            return True
    return False
if __name__ == "__main__":
    data = [2,3,4,5,6]
    print(linear(data,6))
    


def linear(data,target):
    for i in range(0,len(data)):
        if data[i]==target:
            return True
    return False
if __name__ == "__main__":
    data = [2,3,4,5,9]
    print(linear(data,6))
    