# 题目：
# 练习函数调用。

def hello_world(n):
    print ('hello world : %d' % n)
 
def three_hellos():
    for i in range(3):
        hello_world(i)

if __name__ == '__main__':
    three_hellos()