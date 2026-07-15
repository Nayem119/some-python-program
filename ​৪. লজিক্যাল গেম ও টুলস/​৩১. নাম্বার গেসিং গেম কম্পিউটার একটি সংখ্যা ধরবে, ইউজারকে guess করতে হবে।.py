# ​৩১. নাম্বার গেসিং গেম: কম্পিউটার একটি সংখ্যা ধরবে, ইউজারকে guess করতে হবে।
import random
computer_number=random.randint(1, 100)
user_number=int(input("Enter a number: "))
if user_number==computer_number:
    print("You win")
else:
    print("You lose")
