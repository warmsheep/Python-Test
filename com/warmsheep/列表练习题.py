# # 1.创建一个空列表，命名为names，往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl元素
# names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
# # 2.往names列表里black_girl前面插入一个alex
# names.insert(names.index('black_girl'),'alex')
#
# # 3.把shanshan的名字改为中文姗姗
# names[names.index('shanshan')] = '姗姗'
#
# # 4.往names列表里rain的后面插入一个子列表，[oldboy,oldgirl]
# names.insert(names.index('rain'),['oldboy','oldgirl'])
#
# # 5.返回peiqi的索引值
# names.index('peiqi')
#
# # 6.创建新列表[1,2,3,4,2,5,6,2]，合并入names
# n = [1,2,3,4,2,5,6,2]
# names.extend(n)
#
# # 7.取出names列表中索引4-7的元素
# names[4:8]
#
# # 8.取出names列表中索引2-10的元素，步长为2
# names[0:11:2]
#
# # 9.取出names列表中的最后三个元素
# names[-3:]
#
# # 10.循环names列表，打印每个元素的索引值，和元素
# for i in names:
#     print(names.index(i),i)
# for i in enumerate(names):
#     print(i)
# # 如果不想要括号
# for index,i in enumerate(names):
#     print(index,i)
#
# # 11.循环names列表，打印每个元素的索引值，和元素,当索引值为偶数时，把对应元素改为1
# for i in names:
#     if (names.index(i))%2 == 0:
#         print(index, i)
# #         names[names.index(i)] == -1
# # print(names)

# for index,i in enumerate(names):
#     if index%2 == 0:#偶数
#         names[index] = -1
#         print(index,i)
#
# print(names)


# # # 12.names里有3个2 ，请返回第二个2的索引值，不要人肉数，要动态找（提示：找到第一个2的基础上，再找第二个2）
# n = [1,2,3,4,2,5,6,2]
# # n.index(2)+1+n[n.index(2)+1:].index(2)
# # print(n.index(2)+1+n[n.index(2)+1:].index(2))
# first_index = n.index(2)
# new_list = n[first_index+1:]
# second_index = new_list.index(2)
# second_value = first_index + second_index +1
# print(second_value) #最好一步一步写比较好理解

# 13.现有商品如下：
    # products = [['iphone 8 ',6888],['MacPro',14800],['Coffee',31],['Book',80],['NikeShoes',799]
# products = [['iphone 8 ',6888],['MacPro',14800],['Coffee',31],['Book',80],['NikeShoes',799]]
# for i in products:
#     a = products.index(i)
#     b = products[products.index(i)][0]
#     c =  products[products.index(i)][1]
# info = """
# ------------商品列表------------
# %d.            %s            %d
#
# """ %(a,b,c)
# print(info)

# 老师的解答
# print("-------商品列表---------")
# for index,p in enumerate(products):
#     # print(index,p[0],p[1])
#     print("%s, %s      %s "%(index,p[0], p[1]  )) #格式化打印



# products = [['iphone 8 ',6888],['MacPro',14800],['Coffee',31],['Book',80],['NikeShoes',799]]
# count=0
# while count<=4:
#     a = count
#     b = products[count][0]
#     c = products[count][1]
#
# info = """
# ------------商品列表------------
# %d.            %s            %d
#
# """ %(a,b,c)
#
# print(info)


# 14.写一个循环，不断的问客户需要什么，用户选择一个商品编号，就把对应的商品添加到购物车，最终用户输入q退出时，打印购物车里的商品列表


# count = 1
# while count:
#     choice_goods = input("请输入您想要购买的商品编码：")
#     goods_pool.append(choice_goods)
#     goods_pool=[]
#     if choice_goods == "q":
#         for i in goods_pool:
#             print(i)
#             break

products = [['iphone 8 ',6888],['MacPro',14800],['Coffee',31],['Book',80],['NikeShoes',799]]
shopping_cart =[]
exit_flag = False
while not exit_flag:
    print("- - - - - - 商品列表 - - - - - - ")
    for index, p in enumerate(products): #index、p只是临时变量
        print("%s, %s      %s "%(index,p[0], p[1]  ))
    choice = input("输入想买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice >=0 and choice < len(products):
            print("Added products %s into shopping_cart."%(products[choice]))
            shopping_cart.append(products[choice])
        else:
            print("商品不存在！")
    elif choice == "q":
        if len(shopping_cart)>0:
            print("- - - - -您已购买以下商品- - - - - ")
            for index,p in enumerate(shopping_cart):
                print("%s, %s   %s " % (index, p[0], p[1]))
        exit_flag = True# break,尝试用一下标志位
    else:
        exit_flag = True