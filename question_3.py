# Question 3 -- changePossibilities(amount,amount):
# Your quirky boss collects rare, old coins.
# They found out you're a programmer and asked you to solve something they've been wondering for a long time.
# Write a function that, given an amount of money and an array of coin denominations,
# computes the number of ways to make the amount of money with coins of the available denominations.
#
# Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢),
# your program would output 4—the number of ways to make 4¢ with those denominations:
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢

def changePossibilities(value, coins):
    combinations = [0] * (value + 1)
    amount = range(len(coins) + 1)
    combinations[0] = 1
    print(combinations)
    print(amount)

    # for coin in coins:
    #     for value in amount:
    #         if value >= coin:
    #             combinations[value] += combinations[value - coin]
    #         else:
    #             continue
    # print(combinations[-1])





#Driver Code
changePossibilities(4, [1,2,3])
#changePossibilities(10, [1,2,4])
