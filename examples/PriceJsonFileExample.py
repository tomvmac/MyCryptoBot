import json

def validateKeyInDict(key, dict):
	if key in dict:
		print(key, " is valid")
	else:
		print(key, " is NOT valid")

# # read prices
# with open("files/prices.json", "r") as j:
# 	data = json.load(j)
# 	print(data)

# # Loop through data and print each element
# for dataElement in data:
# 	print("Symbol: ", dataElement["symbol"])
# 	print("Price: ", dataElement["price"])
# 	print("\n\n")

# # only print out specific symbols and prices
# for dataElement in data:
# 	if dataElement["symbol"] == "QNTUSDT" or dataElement["symbol"] == "GTCBTC":
# 		print("Symbol: ", dataElement["symbol"])
# 		print("Price: ", dataElement["price"])
# 		print("\n\n")


# read usdt coins and convert to dictionary
coinsDict = {}
with open("files/coins.json", "r") as j:
	data = json.load(j)

for dataElement in data:
	coinsDict[dataElement["symbol"]] = 0

print(coinsDict)

# coinKey existence check
validKey = "AAVEUSDT"
invalidKey = "TOMTOMUSDT"
validateKeyInDict(validKey, coinsDict)
validateKeyInDict(invalidKey, coinsDict)



