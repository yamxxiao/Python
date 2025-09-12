num=1
sum=0

while num<=5:

    ret=1
    i=1
    while i<=num:
        ret*=i
        i+=1
    sum+=ret
    num+=1

print(f'阶乘和为：{sum}')