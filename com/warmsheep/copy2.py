# copy用法
names = ['a','b','c','d','e','f']
n = names.copy()
print(id(names),id(n))
n1 = names
print(id(names),id(n1))

s2 = 'a\tb'
print(s2)


  # 引用 maketrans 函数。

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

