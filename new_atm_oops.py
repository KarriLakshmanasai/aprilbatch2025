
# class atm():
#     def __init__(self):
#         self.balance= 1000
#         self.user_name = "lucky@123"
#         self.set_pin = 1234
#         self.authentication = False
#         self.transaction=[]   #it is used ministatement

#     def auto_authantication (self):
#         print('please enter your user_name and pin.')
#         user_name =input("enter your user_name: ")
#         pin = int(input("pin: "))

#         if self.user_name == user_name and self.set_pin == pin :
#             self.authentication = True
#             print("your successfully loggin.")
#         else:
#             print("incorrect pin tryagain.")

#     def  deposit(self):
#         if self.authentication:
#            amount=float(input("enter amount ₹: "))
#            if amount <100:
#                 print(f"minimum ₹100 above not accetped 10 20 50 rs .")
#            elif amount >=100:
#               self.balance += amount
#               self.transaction.append(f"deposite: ₹{amount}")
#               print(f"deposite ₹{amount}. new balance: ₹{self.balance}")
#         else:
#             print("please authentication.")      

#     def withdraw(self):
#         if self.authentication:
#            amount=float(input("enter amount ₹:"))
        
#            if self.balance > amount:
#               self.balance -= amount
#               self.transaction.append(f"withdraw: ₹{amount}")
#               print(f"withdraw ₹{amount}. new balance: ₹{self.balance}")

#            else:
#                print("insuficiant fund.")
#         else:
#             print("please authentication.")

#     def check_balance(self):
#         if self.authentication:
#            print(f"your balance is ₹{self.balance}") 
#         else:
#             print("please authentication.")  

#     def mini_statment(self):
#         if self.authentication:
#             if not self.transaction:
#                 print("not transections available.")
#             else:
#                 print("\nmini statement")
#                 for transection in self.transaction[-5:] :
#                     print(transection)
#         else:
#             print("please authentication.")

#     def exit_time (self):
#         print("Thank you for using the ATM. Goodbye!")
#         self.authentication = False 

# def main():
#   ATM = atm()

#   while True:
#         print("\nATM Menu:")
#         print("1. auto_authantication")
#         print("2. deposit")
#         print("3. withdraw")
#         print("4. check_balance")
#         print("5. mini_statement")
#         print("6. exit_time")
        
#         try:
#             choice = int(input("Select an option (1-6): "))

#             if choice== 1:
#                 ATM.auto_authantication()
#             elif choice== 2:
#                 ATM.deposit()
#             elif choice== 3:
#                 ATM.withdraw()
#             elif choice== 4:
#                 ATM.check_balance()
#             elif choice== 5:
#                 ATM.mini_statment()
#             elif choice== 6:
#                 ATM.exit_time()
#                 break
#             else:
#                 print("Invalid choice. Please choose a valid option.")
#         except ValueError:
#             print("Invalid input! Please enter a number between 1 and 6.")  

# if __name__ == "__main__":
#     main()                                  










