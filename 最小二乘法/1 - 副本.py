import random
import copy
a = [4.690895705, 5.829204678, 7.331880427, 4.698970004, 0.477121255]
# a.pop(0)     # 删除索引值
for i in range(0, 5):
    b = copy.deepcopy(a)
    # print(random.randint(0, 4), len(b), a)   # 从0到4的随机数
    b.pop(random.randint(0, 4))
    # print(b)


