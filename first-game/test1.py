import json

#with open('test_data.txt','w') as f:
#    json.dump(data, f)

with open('test_data.txt') as f:
    data = json.load(f)
    for entry in data.items():
        print(entry)