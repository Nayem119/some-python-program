# ২৫. ফ্যাক্টোরিয়াল ক্যালকুলেটর: লুপ ব্যবহার করে ফ্যাক্টোরিয়াল বের করা।
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)