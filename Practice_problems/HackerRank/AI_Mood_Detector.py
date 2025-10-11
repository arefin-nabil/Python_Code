# If the message contains words like happy, joy, or smile, print Happy Mood.
# If it contains words like sad, cry, or angry, print Sad Mood.
# Otherwise, print Neutral Mood.


inp = input().split()

hp = False
sd = False

for str in inp:
    if (str == "happy") or (str == "joy") or (str == "smile"):
        hp = True
    elif (str == "sad") or (str == "cry") or (str == "angry"):
        sd = True

if(hp): print("Happy Mood")
elif(sd): print("Sad Mood")
else: print("Neutral Mood")
