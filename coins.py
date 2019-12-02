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
           