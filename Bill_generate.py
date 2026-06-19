# =====================bill_generation_project_main=========================================
from datetime import datetime
name = input("enter your name: ")
phno = int(input("enter the phone number: "))
lists='''
Rice       Rs 10/kg
Suger      Rs 30/kg
Oil        Rs 80/liter
Salt       Rs 10/kg
Panner     Rs 40/kg
eggs       Rs 8/pes
Boost      Rs 250/bottele
'''

price =0
tax =0
dis =0
quntity =0
pricelist =[]
ilist =[]
qlist =[]
plist =[]
total_price =0
finalprice =0

items = {'rice':100, 'Suger':30, 'Oil':80, 'Salt':10, 'Panner':40, 'egg':8, 'Boost':250}
while True:
    option = input("press 1 for lists or press 2 exit the program :")
    if option == '2':
        print("thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp = input("to buy press 1 or press 2 exit: ")
            if inp == '2':
                print("thank you for shopping")
                break
            elif inp == '1':
                item = input("enter the item: ")
                while True:
                    quntity_input = input("enter the quntity: ")
                    if quntity_input.isdigit():
                        quntity = int(quntity_input)
                        break
                    else:
                        print("please enter valid qunitity.")
                        
                if item in items:
                    price = quntity * items[item]
                    pricelist.append((item, quntity, items[item], price))
                    total_price += price
                    ilist.append(item)
                    qlist.append(quntity_input)
                    plist.append(float(price))
                else: 
                    print("select item is not available. sorry for the inconvenience.")

        if total_price >0:
            tax = (total_price * 12) / 100
            discount = int(input("enter discount: "))
            dis = total_price * discount / 100
            finalprice = (total_price+tax) - dis
            print("thank you for shopping")
            print("-------------------------------------------------------------------")
            print("                          Lucky_Mart                               ")
            print("                             salur                                 ")
            print("-------------------------------------------------------------------")
            print(f"Name : {name}                                       phno: {phno}")
            print("-------------------------------------------------------------------")
            print("Sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(0,len(pricelist)):
                print(i, 13 * " ", ilist[i], 10 * " ",  qlist[i], 13 * " ",  plist[i])
            print("----------------------------------------------------------------------")
            print(f"                                     total_amount: Rs {float(total_price)}")
            print(f"                                              Tax: Rs {tax}")
            print(f"                                        discount: -Rs {float(dis)}")
            print("----------------------------------------------------------------------")
            print(f"                                      final_price: Rs {finalprice}")
            print("------------------------------------------------------------------------")
            print("                         Thank you & Visit again                        ")
            print(f"{datetime.now()}------------------------------------------------------------")

            