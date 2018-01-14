
import copy
x={"America":"New York","China":["四川","江苏","河南","香港"]}
z = copy.deepcopy(x)
z["China"].append("湖南")
print(z)
print(x)