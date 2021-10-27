def isDownTrend(priceTrends):
    trends = []
    PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS = 3

    # Sort priceTrends
    priceTrends.sort(key=lambda x: x.get('idx'))

    for x in range(0, len(priceTrends)-1):
        #  Collect Trend
        if priceTrends[x + 1]["price"]:
            if priceTrends[x+1]["price"] >= priceTrends[x]["price"]:
                trends.append(0)
            else:
                trends.append(1)

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

def addPriceTrend(priceTrends, priceTrend):
    MAX_PRICE_TRENDS = 5

    # Sort priceTrends
    priceTrends.sort(key=lambda x: x.get('idx'))

    if len(priceTrends) == MAX_PRICE_TRENDS:
        # Remove first element from priceTrends
        priceTrends.pop(0)
        # Reindex priceTrends
        for i in range(0 , len(priceTrends)):
            priceTrends[i]["idx"] = i

    # Append new priceTrend
    # Get last idx
    lastIdx = priceTrends[len(priceTrends) - 1]["idx"]
    # Update new record with lastIdx + 1
    priceTrend["idx"] = lastIdx + 1
    priceTrends.append(priceTrend)

    return priceTrends



# ------------------------------------------------------------------------------------------------------------------------------------

# add to PriceTrends
priceTrends = [{"idx": 0, "price": 1.22}, {"idx": 2, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 3, "price": 1.28}]

addPriceTrend(priceTrends, {"idx": 0, "price": 1.34})
addPriceTrend(priceTrends, {"idx": 0, "price": 1.99})
addPriceTrend(priceTrends, {"idx": 0, "price": 1.98})
addPriceTrend(priceTrends, {"idx": 0, "price": 2.98})

print(priceTrends)

# isDownTrend
priceTrends1 = [{"idx": 0, "price": 1.23}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.25}, {"idx": 3, "price": 1.26}]  # Up / False
priceTrends2 = [{"idx": 0, "price": 1.25}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Down / True
priceTrends3 = [{"idx": 0, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Up / False
priceTrends4 = [{"idx": 0, "price": 1.23}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Down / True
priceTrends5 = [{"idx": 0, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.25}, {"idx": 3, "price": 1.22}]  # Up / False
priceTrends6 = [{"idx": 0, "price": 1.20}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.23}, {"idx": 4, "price": 1.24}, {"idx": 5, "price": 1.25}, {"idx": 6, "price": 1.20}]  # Up / False
priceTrends7 = [{"idx": 0, "price": 1.25}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.22}, {"idx": 3, "price": 1.23}, {"idx": 4, "price": 1.21}, {"idx": 5, "price": 1.20}, {"idx": 6, "price": 1.20}]  # Up / False
priceTrends8 = [{"idx": 0, "price": 1.20}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.21}, {"idx": 3, "price": 1.20}, {"idx": 4, "price": 1.19}, {"idx": 5, "price": 1.25}, {"idx": 6, "price": 1.20}]  # Down / True



print(isDownTrend(priceTrends1))
print(isDownTrend(priceTrends2))
print(isDownTrend(priceTrends3))
print(isDownTrend(priceTrends4))
print(isDownTrend(priceTrends5))
print(isDownTrend(priceTrends6))
print(isDownTrend(priceTrends7))
print(isDownTrend(priceTrends8))

