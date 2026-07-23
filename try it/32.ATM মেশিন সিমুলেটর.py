# এটিএম (ATM) মেশিন সিমুলেটর
# মূল ধারণা: ব্যালেন্স চেক, টাকা তোলা, ও জমা দেওয়ার সিস্টেম। টাকা তুললে পর্যাপ্ত ব্যালেন্স আছে কিনা তা conditionals দিয়ে চেক করা হবে। 
initial_balance = 1000  # প্রাথমিক ব্যালেন্স
def atm_machine():
    balance = initial_balance
    while True:
        print("\nএটিএম মেশিনে স্বাগতম!")
        print("1. ব্যালেন্স চেক করুন")
        print("2. টাকা তুলুন")
        print("3. টাকা জমা দিন")
        print("4. প্রস্থান করুন")
        
        choice = input("আপনার পছন্দ নির্বাচন করুন (1-4): ")
        
        if choice == '1':
            print(f"আপনার বর্তমান ব্যালেন্স: {balance} টাকা")
        
        elif choice == '2':
            amount = float(input("আপনি কত টাকা তুলতে চান? "))
            if amount <= balance:
                balance -= amount
                print(f"{amount} টাকা সফলভাবে তোলা হয়েছে। নতুন ব্যালেন্স: {balance} টাকা")
            else:
                print("দুঃখিত, পর্যাপ্ত ব্যালেন্স নেই।")
        
        elif choice == '3':
            amount = float(input("আপনি কত টাকা জমা দিতে চান? "))
            balance += amount
            print(f"{amount} টাকা সফলভাবে জমা হয়েছে। নতুন ব্যালেন্স: {balance} টাকা")
        
        elif choice == '4':
            print("ধন্যবাদ! এটিএম মেশিন ব্যবহার করার জন্য।")
            break
        
        else:
            print("অবৈধ পছন্দ, দয়া করে 1 থেকে 4 এর মধ্যে একটি সংখ্যা নির্বাচন করুন।")