

#
# data = ( x*2 for x in range(5))
#
# print(data)
#
# # for i in data:
# #     print(i)
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())
# print(next(data))
# print(next(data))
# print(next(data))
def fib(num):
    '''
    :param num: 求多少个数列 10
    :return: # 0 1 1 2 3 5 8 13 21 34
    '''
    count = 0
    a,b = 0 ,1 #a=0, b= 1
    while count < num:
        tmp = a
        a = b
        b = a + tmp
        #print(a)
        count +=1
        yield a #返回a, 同时挂起当前这个函数， a返回给了通过__next__()调用当前函数的人
        #return a
    print("done...")
#
# f = fib(1000000) #生成了一个生成器对象，就是代表推到公式准备好了的意思
# print(f.__next__()) #a
# print(f.__next__()) #a
# print(f.__next__()) #a
# print(f.__next__()) #a

# f.__next__() #a
# f.__next__()

def simple(name):
    for i in name:
        yield  i


s = simple("alex")
print(s.__next__())
print(s.__next__())
print(s.__next__())

