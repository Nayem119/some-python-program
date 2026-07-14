# ২০. মিনি গেম (হায়ার/লোয়ার): কম্পিউটার একটি সংখ্যা ধরবে, ইউজারকে বলতে হবে সেটা ছোট না বড়।
import random
computer_number = random.randint(1, 100)
user_number = int(input("Enter your number: "))
if user_number > computer_number:
    print("You are higher")
elif user_number < computer_number:
    print("You are lower")
else:
    print("You are correct")
    