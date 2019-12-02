#Num of coins
def num_coins(cents):
    coins =[25,10,5,1]
    num = 0
    
    for coin in coins:
        while cents>=coin:
            print(coin)           
            cents = cents - coin
            num = num + 1
    return num

print(num_coins(26))

#Num of min coins
def num_coins(cents):
    coins = [25,10,5,1]
    num = 0
    for i in range(0,len(coins)):
        for j in range(1,len(coins)):
            if coins[i]>coins[j]:
                coins1 = coins[i]
                while cents>=coins1:
                    print(coins1)
                    cents = cents-coins1
                    num = num + 1
    return num

print(num_coins(100))