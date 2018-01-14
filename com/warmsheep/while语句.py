
count = 0
number =23
while count < 3:
    guess = int(input("请输入年龄"))
    if guess == number: #如果猜测等于实际年龄
        print("恭喜你！猜对了！")
        break
        print("但是也没有奖品给你!") #如果猜测大于实际年龄
    elif guess > number:
        print("Try smaller!")
    else:
        print("Try bigger") #如果猜测小于实际年龄
    count += 1
else:
    print("对不起你的机会已经用完了")



