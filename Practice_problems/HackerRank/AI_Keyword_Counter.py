inp = input().split()

cnt = 0


for x in inp:
    if "ai" == x:
        # print("ai")
        cnt += 1
    elif "data" == x:
        # print("data")
        cnt += 1
    elif "model" == x:
        cnt += 1
    elif "learn" == x:
        cnt += 1
    elif "train" == x:
        cnt += 1
    elif "neural" == x:
        cnt += 1
    

# for i in inp:
    


# print(cnt)

if cnt >= 2:
    print("AI Detected")
else:
    print("Not AI Related")
