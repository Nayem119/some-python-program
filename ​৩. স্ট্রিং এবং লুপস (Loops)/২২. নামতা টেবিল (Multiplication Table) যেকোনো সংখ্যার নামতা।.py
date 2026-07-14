# ২২. নামতা টেবিল (Multiplication Table): যেকোনো সংখ্যার নামতা।
number = int(input("Enter a number: "))
for i in range(1, 11):  
    print(f'{number} x {i} = {number * i }') #table line
    print("----------------------------") #separator line