# Given a list of numbers, determine if it is overall downtrend

def isDownTrend(prices):
    trends = []

    for x in range(0, len(prices)-1):
        #  Collect Trend
        if prices[x + 1]:
            if prices[x+1] >= prices[x]:
                trends.append(0)
            else:
                trends.append(1)

    # Process Trend
    for y in range(0, len(trends)-1):
        if trends[y + 1]:
            if trends[y] + trends[y+1] > 1:
                return True

    return False

# TODO:
# 2. List shifting, add element to end of list and remove the first



#---------------------------------------------------------------
prices1 = [1.23, 1.24, 1.25, 1.26]  # Up: All Up
prices2 = [1.25, 1.24, 1.23, 1.22]  # Down: All Down
prices3 = [1.24, 1.23, 1.23, 1.22]  # Up: No Down, Some Same
prices4 = [1.23, 1.24, 1.23, 1.22]  # Down:
prices5 = [1.24, 1.23, 1.25, 1.22]  # Up: Skip Down, Not Down

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