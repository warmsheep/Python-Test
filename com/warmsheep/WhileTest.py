#
# count = 0
# age = 22
# while count < 3:
#     inputAge = int( input("请输入你的年龄"))
#     if inputAge == age:
#         print("傻逼")
#         break
#     else:
#         print("大傻逼")
#         count += 1
count = 1
age = 22
while count:
    if int(count%3) > 0:
        inputAge = int( input("请输入你的年龄"))
        if inputAge == age:
            print("傻逼")
            break
        else:
            print("大傻逼")
    else:
        user_choice = input("是否还想再玩？")
        if user_choice == "是":
            inputAge = int(input("请输入你的年龄"))
            if inputAge == age:
                print("傻逼")
                break
            else:
                print("大傻逼")
        else:
             break
    count += 1

# count = 0
# age = 22
# while count < 3:
#     user_guess = int(input("请输入年龄"))
#     if user_guess == age:
#         break
#     else :
#         print("请重新输入！")
#
#     count += 1
#     if count == 3:
#         choice = input("你还想继续玩么？")
#         if choice == 'y':
#             count = 0







