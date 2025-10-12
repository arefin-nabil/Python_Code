n = input()
t = input()
t=tuple(t)
print(hash(t))

# Python 2
# n = int(raw_input()) 
# t = tuple(map(int, raw_input().split())) 
# print hash(t)