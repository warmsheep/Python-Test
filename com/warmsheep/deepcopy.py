# import copy
# x={"America":"New York","China":["四川","江苏","河南","香港"]}
# z = copy.deepcopy(x)
# z["China"].append("湖南")
# print(z)
# print(x)
#
# x={}.fromkeys(["name","age"])
# # print(x)
# import copy
# d={"Eric":"男","Ashily":"男"}
# c={"Jack Ma":"男","Elle":"女","June":[1,2]}
# d.update(c)
# e =copy.deepcopy(d)
# c["Elle"]="男"
# c["June"].append(3)
# print(d)
# print(e)

dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("字典所有值为 : ",  list(dict.values()))