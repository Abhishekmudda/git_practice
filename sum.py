def cal_sum(num):
    sum=0

    for i in range(num):
        sum=sum+i

    return sum

def cal_fact(num):
    fact=1

    for i in range (1,num):
        fact=fact * i

    return fact

num=int(input("enter the number"))
print(cal_sum(num))
print(cal_fact(num))