import json
test_str = "[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 4, 'Best' : 9}]"
res = json.loads(test_str.replace("'", '"')) 

x = {"name":"john", "age":23}
lx = [x for i in range(9)]

x = [3,4]
print(x.max())
