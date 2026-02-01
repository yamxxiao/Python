class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#隐藏属性是__变量名
#对标c++的private的是_符号
#实际上，隐藏属性就是等于_类名__变量名
#隐藏属性子类不会继承
class Man():
    def __play(self):#这是个隐藏方法的类
        print('van游戏')
        self.__play()#可以通过self.的方法调用隐藏属性
pe=person( 'da',12)
print(pe.name)

man=Man()
