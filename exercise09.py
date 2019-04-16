# 题目：
# 暂停一秒输出。

import time
 
myD = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
for key, value in dict.items(myD):    
    time.sleep(key) # 暂停 key 秒
    print (key, value)
print ('end')