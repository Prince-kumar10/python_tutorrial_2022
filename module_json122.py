import json

data = '{"var1":"prince" , "var2":56}'

parsed = json.loads(data)

print(parsed['var1'])

# Task 1 - json.load function kya karta hai


data2 = {
    "channel_name": "movie club",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
# jscomp = json.dumps(data2)
# print(jscomp)

# Task2 what is sort_keys parameter in dumps


# json.load() accepts file object.
# ex:
with open("json_data.json", "r") as content:
     print(json.load(content))