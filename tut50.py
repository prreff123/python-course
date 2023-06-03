import json
# data = '{"var1":"harry","var2":56}'
# parsed = json.loads(data)
# print(parsed['var1'])

data2 = {
    "channel_name":"CodewithHarry",
    "Cars": ['bmw','audia8','ferrari'],
    "Fridge":("roti"),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)