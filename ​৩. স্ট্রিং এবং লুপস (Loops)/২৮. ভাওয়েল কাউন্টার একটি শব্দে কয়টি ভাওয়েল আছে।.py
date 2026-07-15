# ২৮. ভাওয়েল কাউন্টার: একটি শব্দে কয়টি ভাওয়েল আছে। totalvowels
x=input("Enter a word: ")
totalvowels=0
for i in x:
    if i in "aeiouAEIOU":
        totalvowels+=1
print(totalvowels)