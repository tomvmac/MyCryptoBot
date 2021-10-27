import PriceTrends

# PrecentGainLoss
prevPrice1 = 4.00
currPrice1 = 5.00
# print(PriceTrends.percentGainLoss(prevPrice1, currPrice1),"%")
#
prevPrice2 = 4.00
currPrice2 = 3.00
# print(PriceTrends.percentGainLoss(prevPrice2, currPrice2),"%")


# add to PriceTrends
priceTrends = []
# priceTrends = [{"idx": 0, "price": 1.22}, {"idx": 2, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 3, "price": 1.28}]

PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.34})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.99})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.98})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 2.98})

# print(priceTrends)

# PriceTrends.isDownTrend
priceTrends1 = [{"idx": 0, "price": 100.00}, {"idx": 1, "price": 104.00}, {"idx": 2, "price": 105.25}, {"idx": 3, "price": 106.26}]  # Up / False
priceTrends2 = [{"idx": 0, "price": 105.25}, {"idx": 1, "price": 104.24}, {"idx": 2, "price": 103.23}, {"idx": 3, "price": 102.22}]  # Down / True
priceTrends3 = [{"idx": 0, "price": 102.00}, {"idx": 1, "price": 123.00}, {"idx": 2, "price": 123.00}, {"idx": 3, "price": 123.00}, {"idx": 4, "price": 124.00}, {"idx": 5, "price": 125.00}, {"idx": 6, "price": 120.00}]  # Up - And Same / False
priceTrends4 = [{"idx": 0, "price": 125.25}, {"idx": 1, "price": 123.23}, {"idx": 2, "price": 122.22}, {"idx": 3, "price": 123.23}, {"idx": 4, "price": 121.21}, {"idx": 5, "price": 120.20}, {"idx": 6, "price": 120.20}]  # Up / False
priceTrends5 = [{"idx": 0, "price": 120.20}, {"idx": 1, "price": 123.23}, {"idx": 2, "price": 121.21}, {"idx": 3, "price": 120.20}, {"idx": 4, "price": 119.19}, {"idx": 5, "price": 125.25}, {"idx": 6, "price": 120.20}]  # Down / True
priceTrends6 = [{"idx": 0, "price": 120.20}, {"idx": 1, "price": 123.23}, {"idx": 2, "price": 123.22}, {"idx": 3, "price": 123.21}, {"idx": 4, "price": 123.50}, {"idx": 5, "price": 125.25}, {"idx": 6, "price": 120.20}]  # Up - Small Changes / False
priceTrends7 = [{"idx": 0, "price": 120.20}, {"idx": 1, "price": 123.90}, {"idx": 2, "price": 123.20}, {"idx": 3, "price": 122.40}, {"idx": 4, "price": 121.50}, {"idx": 5, "price": 125.25}, {"idx": 6, "price": 120.20}]  # Down - Big Enough Changes / True



print(PriceTrends.isDownTrend(priceTrends1))
print(PriceTrends.isDownTrend(priceTrends2))
print(PriceTrends.isDownTrend(priceTrends3))
print(PriceTrends.isDownTrend(priceTrends4))
print(PriceTrends.isDownTrend(priceTrends5))
print(PriceTrends.isDownTrend(priceTrends6))
print(PriceTrends.isDownTrend(priceTrends7))
