nums=[2,4,5,6]  

target = 11

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        
        if nums[i]+nums[j]==target:
            print(i,j)
            break
        if nums[i]+nums[j]!=target:
            print("no tar")