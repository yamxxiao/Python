# f='my name is xiaowei'
# print(len(f))
# f=10
# print(f)
# d:int=10
# print(d)
# w:str='shi'
# print(w)
#zer
# #希望打印出来“a=10”
# a=10
# print(f'a={a}')#这个语法叫做格式化字符串\
#输入操作
# num=input('请输入一个数字')
# print(f'这个数为{num}')
#因为input输入的是一个str类型，如果进行运算，则只是字符串相加
#要解决这个问题，办法是使用 int（）进行强转，依此类推 str(),float()
a=input("请输入第一个相加的数")
b=input("请输入第二个相加的数")
a=int(a)
b=int(b)
num=(a+b)
print(f'结果为{num}')

