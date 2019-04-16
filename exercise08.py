# 题目：
# 输出 9*9 乘法表。

for i in range(1,10):
    for j in range(1,10):
        if (j == 9):
            print ('%d * %d = %d' % (i,j,i*j))
        else:
            print ('%d * %d = %d' % (i,j,i*j), end ='\t')