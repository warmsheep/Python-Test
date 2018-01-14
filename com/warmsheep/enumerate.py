

# list1 = ["你", "好", "Python", "Class"]
# for index, item in enumerate(list1):
#     print (index, item)

# list1 = ["你", "好", "Python", "Class"]
# for i in list1:
#     print(list1.index(i),i)

# list1 = ["你", "好", "Python", "Class"]
# for index, item in enumerate(list1,1):
#     print (index, item)

# print(3*(40+2))
# # print(3*(40+2,))
# print(tuple([1,2,3]))
# #输出
#
# print(tuple('Hello'))
# #输出
count = 0
age = 22

while count < 3:
    user_guess = int( input("your guess:") )
    if user_guess == age :
        print("恭喜你，答对了！")
        break
    elif user_guess > age:
        print("try smaller")
    else :
        print("try bigger")
    count +=1
    while count == 3:
        choice = input('你还想要继续玩么？如果是请输入Y或者y')
        if choice == "y" or "Y":
            count = 0
