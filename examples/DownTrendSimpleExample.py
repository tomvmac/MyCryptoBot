# Given a list of numbers, determine if it is overall downtrend

def isDownTrend(prices):
    trends = []
    PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS = 3

    for x in range(0, len(prices)-1):
        #  Collect Trend
        if prices[x + 1]:
            if prices[x+1] >= prices[x]:
                trends.append(0)
            else:
                trends.append(1)
    #
    # print (trends)
    # Process Trend
    currentConsecutiveDips = 0
    for y in range(0, len(trends)):

        if trends[y] == 1:
            currentConsecutiveDips += 1
        else:
            if y > 0:
                currentConsecutiveDips -= 1

    if currentConsecutiveDips >= PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS:
        return True

    return False


#---------------------------------------------------------------
prices1 = [1.23, 1.24, 1.25, 1.26]  # Up: All Up
prices2 = [1.25, 1.24, 1.23, 1.22]  # Down: All Down
prices3 = [1.24, 1.23, 1.23, 1.22]  # Up: No Down, Some Same
prices4 = [1.23, 1.24, 1.23, 1.22]  # Down:
prices5 = [1.24, 1.23, 1.25, 1.22]  # Up: Skip Down, Not Down
prices6 = [1.20, 1.23, 1.23, 1.23, 1.24, 1.25, 1.20] # Up
prices7 = [1.25, 1.23, 1.22, 1.23, 1.21, 1.20, 1.20] # Up
prices8 = [1.20, 1.23, 1.21, 1.20, 1.19, 1.25, 1.20] # Down


print(prices1)
print(isDownTrend(prices1))
print("\n-----------------------")


print(prices2)
print(isDownTrend(prices2))
print("\n-----------------------")

print(prices3)
print(isDownTrend(prices3))
print("\n-----------------------")


print(prices4)
print(isDownTrend(prices4))
print("\n-----------------------")

print(prices5)
print(isDownTrend(prices5))
print("\n-----------------------")

print(prices6)
print(isDownTrend(prices6))
print("\n-----------------------")

print(prices7)
print(isDownTrend(prices7))
print("\n-----------------------")

print(prices8)
print(isDownTrend(prices8))
print("\n-----------------------")