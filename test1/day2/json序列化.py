
import json

def sayhi():
    print("hey")

data = {
    'name':"alex",
    "age":22,
    "sex": "M",
}
#
f = open("data.txt","w",encoding="utf-8")
#f.write(   json.dumps(data) )

json.dump(data,f)

json.dump([1,2,3],f)

# f = open("data.txt","r",encoding="utf-8")
# data = eval(f.read()  )

# print(data)
# print(data["age"])
# f.close()