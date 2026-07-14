# ২৬. প্যাটার্ন প্রিন্টিং (স্টার): স্টার দিয়ে ত্রিভুজ ।
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# বা বর্গ বানানো
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print("*", end=" ")
    print()