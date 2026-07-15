# ২৭. শব্দ গণনা: একটি বাক্যে কয়টি শব্দ আছে।
x=input("Enter a sentence: ")
words = x.split()
print(len(words))
# কয়টি স্পেস আছে বাক্যে
print(x.count(" "))