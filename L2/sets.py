s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

# 集合中的元素是唯一的。
print(s)
# 错误示范，集合没有下标表示方法，比如下边，移除集合中第三个元素，是不对的
# s.remove(s[2])
print(s)

s.remove(2)
print(s)

print(len(s))

print(f"The set has {len(s)} elements.")