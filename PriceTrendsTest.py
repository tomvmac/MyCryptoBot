import PriceTrends


# add to PriceTrends
priceTrends = []
# priceTrends = [{"idx": 0, "price": 1.22}, {"idx": 2, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 3, "price": 1.28}]

PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.34})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.99})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 1.98})
PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": 2.98})

print(priceTrends)

# PriceTrends.isDownTrend
priceTrends1 = [{"idx": 0, "price": 1.23}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.25}, {"idx": 3, "price": 1.26}]  # Up / False
priceTrends2 = [{"idx": 0, "price": 1.25}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Down / True
priceTrends3 = [{"idx": 0, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Up / False
priceTrends4 = [{"idx": 0, "price": 1.23}, {"idx": 1, "price": 1.24}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.22}]  # Down / True
priceTrends5 = [{"idx": 0, "price": 1.24}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.25}, {"idx": 3, "price": 1.22}]  # Up / False
priceTrends6 = [{"idx": 0, "price": 1.20}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.23}, {"idx": 4, "price": 1.24}, {"idx": 5, "price": 1.25}, {"idx": 6, "price": 1.20}]  # Up / False
priceTrends7 = [{"idx": 0, "price": 1.20}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.23}, {"idx": 3, "price": 1.20}, {"idx": 4, "price": 1.21}, {"idx": 5, "price": 1.25}, {"idx": 6, "price": 1.20}]  # Up / False
priceTrends8 = [{"idx": 0, "price": 1.20}, {"idx": 1, "price": 1.23}, {"idx": 2, "price": 1.21}, {"idx": 3, "price": 1.20}, {"idx": 4, "price": 1.19}, {"idx": 5, "price": 1.25}, {"idx": 6, "price": 1.20}]  # Down / True


# print(PriceTrends.isDownTrend(priceTrends1))
# print(PriceTrends.isDownTrend(priceTrends2))
# print(PriceTrends.isDownTrend(priceTrends3))
# print(PriceTrends.isDownTrend(priceTrends4))
# print(PriceTrends.isDownTrend(priceTrends5))
# print(PriceTrends.isDownTrend(priceTrends6))
# print(PriceTrends.isDownTrend(priceTrends7))
# print(PriceTrends.isDownTrend(priceTrends8))

