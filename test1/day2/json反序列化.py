import json

f = open("data.txt",encoding="utf-8")

# data = json.loads(f.read())
data = json.load(f)
print(data["age"])