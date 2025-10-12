# str = input()

# str = ''.join(sorted(str))

# cnt = {}

# for ltr in str:
#     cnt[ltr] = cnt.get(ltr,0) + 1

# for k, v in cnt.items():
#     print(f"{k} : {v}")


s = input()
count = {}
for word in s:
    count[word] = count.get(word, 0) + 1
for k, v in sorted(count.items()):
    print(f"{k} : {v}")


# str = list(input())
# cnt = {}
# for ltr in sorted(str):
#     cnt[ltr] = cnt.get(ltr,0) + 1
# for k, v in cnt.items():
#     print(f"{k} : {v}")
