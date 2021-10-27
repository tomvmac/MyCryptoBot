import Constants

def percentGainLoss(prevPrice, currPrice):
    percentageGainLoss = ((currPrice - prevPrice) / prevPrice) * 100
    return percentageGainLoss

def isDownTrend(priceTrends):
    trends = []

    # Sort priceTrends
    priceTrends.sort(key=lambda x: x.get('idx'))

    for x in range(0, len(priceTrends)-1):
        #  Collect Trend
        currPrice = 0
        prevPrice = 0
        percentageGainLoss = 0
        if priceTrends[x + 1]["price"]:
            currPrice = priceTrends[x+1]["price"]
            prevPrice = priceTrends[x]["price"]
            percentageGainLoss = percentGainLoss(prevPrice, currPrice)
            if percentageGainLoss <= Constants.PRICE_TRENDS_DOWNTREND_PERCENTAGE_THRESHOLD:
                trends.append(1)
            else:
                trends.append(0)

    # print(trends)

    # Process Trend 0 is no dip, 1 is a dip
    currentConsecutiveDips = 0
    for y in range(0, len(trends)):

        if trends[y] == 1:
            currentConsecutiveDips += 1
        else:
            if y > 0:
                currentConsecutiveDips -= 1

    if currentConsecutiveDips >= Constants.PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS:
        return True

    return False

def addPriceTrend(priceTrends, priceTrend):

    # Sort priceTrends
    priceTrends.sort(key=lambda x: x.get('idx'))

    if len(priceTrends) == Constants.PRICE_TRENDS_SIZE:
        # Remove first element from priceTrends
        priceTrends.pop(0)
        # Reindex priceTrends
        for i in range(0 , len(priceTrends)):
            priceTrends[i]["idx"] = i

    # Append new priceTrend
    if len(priceTrends) > 0:
        # Get last idx
        lastIdx = priceTrends[len(priceTrends) - 1]["idx"]
        # Update new record with lastIdx + 1
        priceTrend["idx"] = lastIdx + 1
    else:
        priceTrend["idx"] = 0

    priceTrends.append(priceTrend)

    return priceTrends
