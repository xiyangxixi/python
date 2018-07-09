s = set([1, 2, 3])
s.add(4)
# 可以重复添加 但是没效果 str不可变，list可变
print(s)
s.remove(4)
print(s)
print(s)