import json

# Write dictionary date to a json file
# data = {"MOO":"Moodia", "Google":"Search", "Python":"Language"}
# with open("files/myfile.json", "w") as j:
# 	json.dump(data, j)

# write more complicated data
# data = {"Sites": [{"MUO": "Media", "Google": "Search", "Python": "Language"}]}
# with open("files/myfile.json", "w") as j:
#     json.dump(data, j)


# convert a list into dict and then json
# dataList = ["MUO", "Media", "Lycos", "Search", "Java", "Language"]
# dataDict = {dataList[i]:dataList[i+1] for i in range(0, len(dataList), 2)} #convert data into a dictionary
# with open("files/myfile.json", "w") as j:
# 	json.dump(dataDict, j)


# merge two lists together
# data = ["MUO", "Google", "Python"]
# data2 = ["Media", "Search", "Language"]
# outputData = {data[i]:data2[i] for i in range(len(data))} #merge the two lists into a dictionary
# with open("files/myfile.json", "w") as j:
# 	json.dump(outputData, j)

# access and query data from json file
# with open("files/myfile.json", "r") as j:
# 	mydata = json.load(j)
# 	# print entire json
# 	print(mydata)
# 	# print a specific element
# 	print(mydata["Google"])

# read file, change contents and then write file
with open("files/myfile.json", "r") as j:
	mydata = json.load(j)
	mydata["Python"] = "Snake"
	mydata["BTC"] = "BitCoin"

with open("files/myfile.json", "w") as k:
	json.dump(mydata, k)
