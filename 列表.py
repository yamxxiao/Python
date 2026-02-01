a=[1,2,3,4,5]

# for elem in a:
#     elem=elem+11
#     print(elem)
#
# for i in range(0,len(a)):
#     a[i]=a[i]+11
#     print(a[i],end=" ")
#
# a.append(1)#尾插
# for elem in a:
#     print(elem)
#
# print(a.index(5))#查找下标
# a.insert(5,89)
# print(a)
# a.pop(0)#按下标删除
# a.remove(5)
# print(a)
# # a.remove(6)#按值删除
# a.insert(4,1)
# print(a)
# b=[6,7,89,10]
# a.extend(b)#拼接数组
# print(a)
# c=a.extend(b)#这个不能被接受，打印的为None,类似为null
#对于拼接数组的extend,就类似于c++的浅拷贝

#元组,和列表类似
#创建方式
# a=()
# b=tuple()
# 也可以通过切片的方式获得元组
b=(1,2,3,4,5,6)
print(b[-1:1:-1])
#元组于列表的区别是，元组不能修改，只能读，列表都可以
# for i in b:
#     b=b+10
#     print(b)
# b.pop(1)
# print(b)
#s实际上，当涉及多元赋值时，本质上是利用元组进行工作

# def get():
#     x=10
#     y=20
#     return x,y
# x,y=get()
# print(type(get()))

#字典
#在Python中，可以同时包含多个键值对，但不能重复
#构造方式
# c={}
# d=dict()
# v=list()
# print(type(c))
# print(type(v))
#创建字典的同时需要创建键值对
# d={'rd':1,
#    'ff':2
# }
# print(d)
#可以使用in来查找字典里面是否存在key
#
# print('rd'in d)
# #也可以使用[]来找value
# print(d['rd'])
#对于列表来说使用in比较低效率，[]比较高效
#对于字典，使用[]进行写入操作