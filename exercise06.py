# 题目：
# 斐波那契数列。
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

count = int(input("count : "))
 
print (fib(count))