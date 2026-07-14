# সর্বোচ্চ সংখ্যা নির্ণয়: তিনটি সংখ্যার মধ্যে বড় সংখ্যা খুঁজে বের করা।
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)