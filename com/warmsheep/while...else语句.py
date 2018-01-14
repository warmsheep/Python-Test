# count = 0
# while count <= 5:
#     count +=1
#     print("loop",count)
# else:
#     print("循环正常执行了")
# print("-----out of while loop-----")

count = 0
while count <= 5:
    count +=1
    print("loop",count)
    if count == 5 :
        break
else:
    print("循环正常执行了")
print("-----out of while loop-----")