# ৮. সিম্পল ইন্টারেস্ট: সরল মুনাফা নির্ণয়ের প্রোগ্রাম।
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
interest = (principal * rate * time) / 100
print("The interest is: ", interest)