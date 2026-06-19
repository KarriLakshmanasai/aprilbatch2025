# sum = 0
# number = [24,34,54,22,45]
# for i in number:
#     sum+=i
#     if sum >=100 :
#         print(f"sum exceded 100 {sum}")
#         break
# print(i)


# for i in range(1,600):
#     if i%2==0:
#         continue
#     print(i)
        

# words = ["hello","world","python","skip","new","break","joint"]
# for i in words:
#     print(i)
#     if i=="skip":
#         print(f"u wont skip {i}")
#         continue
#     elif i=="break":
#         print(f"u wont break {i}")
#         break
# print(i)


# my_list = [10,20,30,40,50,60,70,80]
# print(my_list[2:5:2])
    

# dict_1 = {1:"sai",
#         2:"hari",
#         3:"mahi",
#         4:1234,}
# dict_1[5]="raju"
# print(dict_1)
 
# dict_1 = {1:"sai",
#         2:"hari",         
#         3:"mahi",
#        4:1234,}   
# print(len(dict_1))
# print(dict_1.items())
# print(dict_1.values())
# print(dict_1.get(2))
# print(dict_1.pop(4))
# print(dict_1)


# user_data ={}
# user_name = input("enter username")
# pass_word = input("enter password")

# user_data[user_name]=pass_word
# print(user_data)

# print("my name is sai")


# list_1=[1,2,"sai",(2,3,4,"sai")]
# # print(type(list_1))
# set_con=set(list_1)
# print(set_con)
# list_con=list(set_con)
# print(list_con)

    
# set_1={2,3,4,(56,67),"sai","hari",2,3}
# print(set_1)

# dict_1 ={1:"sai",
#          2:"mahesh",
#          3:"hari",
#          4:[2,4,5,6,7],
#          1:(34,5,6,7),}
# # print(dict_1)
# # tuple_con = tuple(dict_1)
# # print(tuple_con)
# set_con = set(dict_1)
# print(set_con)


# a= input("enter number1: ")
# b= input("enter number2: ")
# print(int(a)+int(b))


# num_1 = int(input("enter number: "))
# num_1 += int(input("enter add number: "))
# print(num_1)

# num_1 = int(input("enter number: "))
# num_1 //= int(input("enter add number: "))
# print(num_1)

# a= 5
# b= 10
# a= a+b
# print(a)
# b= a-b
# print(b)
# a=a-b
# print(a,b)


# x=5
# y=x
# print(y)
# x = x+2
# print(x)
# y= y*2
# print(x+y)

 
# s = "python"
# s[0]="p"
# print(s)

# a =[1,2]
# b = a
# a = a+[3]
# print(b)

# a = [1,2,3,4]
# b = a[::2]
# print(b)
# b[0]=99
# print(a)

# def f():
#     i = 0
#     while i<3:
#         i += 2
#         if i == 2:
#           continue
#         return i
# print(f())


# a = "3"
# a *=2
# print(type(a))


# stock = ["banana","apple","grapes","guva"]
# print ("straberry" in stock)
# print("straberry" not in stock)


# product_cost = 10000
# discount = 10
# result = product_cost * (discount/100)
# # print(result)
# product_cost -= result
# print(f" product_cost)

# length =float(input("enter length value :"))
# breath = float(input("enter breath value :"))
# area = length * breath
# print(f"length value is {length} and breath value is {breath} after cal area value is {area}")


# age = int(input("enter the age :"))
# age += int(input("enter the increment value :"))
# print(f"increment the value is {age}")
# age -= int(input("enter the decrement value :"))
# print(f"decrement the value is {age}")

"""new_1 project of username and password

user_name = input("enter username :")
password = input("enter password :")

if user_name == "laxmansai":
    print(f"your username succesfully")
    if password == "l1u2c3k4y5":
        print(f"login succesfully \nWelcome to the Home {user_name}")
    else:
        print(f"invalid password {password} \ntry again")
else:
    print(f"invalid username {user_name} \nplease enter correct username") """


'''element = int(input("enter number :"))
print(f"{element} is a even number") if element%2==0 else print(f"{element} is not a even number")'''


'''VOWEL = input("enter the vowel :")
if VOWEL in "a,e,i,o,u":
    print(f"this is the vowel")
else:
    print(f"this is not a vowel")'''



'''VOWEL = input("enter the vowel :")
list_1 =['a','e','i','o','u']
if VOWEL in list_1 :
    print(f"this is the vowel")
else:
    print(f"this is not a vowel")'''


'''age = int(input("enter the number :"))
if age <=12:
    print(f"this {age} age is chaild")
elif age>=13 and age <=17:
    print(f"this {age} age is teenager")
elif age >=18 and age <=64:
    print(f"this {age} age is adult")
elif age >=65:
    print(f"this {age} age is old")'''


'''for i in range(1,10):
    if i >=9 :
        print(f"not satisify:{i}")
    else:
        print("good")'''

'''for i in range(2,11,2):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print("        ") '''  

'''num = int(input("enter number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")'''

'''num = int(input("enter number: "))
for i in range(num,num+1):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}") '''

'''los=[1,2,3,4,5]
for i in los:
    print(i)'''

'''lst =["ok","ok","ok","defet","ok","ok","defet","ok","ok","ok"]
res =0
for i in lst:
    if i == "defet":
        res+=1
        print(f"defet products is {res}")
        continue
    print(i)'''

'''lst = [25,30,20,40,15,25]
result=0
for i in lst:
    result+=i
    if result >=100:
        break
    print(result)'''

'''for i in range(1,600+1,2):
    print(i)'''

'''for i in range(1,600+1):
    if i%2 ==0:
        continue
    print(i)'''

'''lis_1 = list()
print(type(lis_1))'''

# my_list = [10,20,30,40,50,60,40,80]
# print(my_list.extend([28,34,56,("sai",34,56,77)]))


# los=[1,2,3,4,5]
# los.reverse()
# for i in los:
#     print(i)

# ascn and desc
# new =[63,45,67,25,7,12,23,34]
# new.sort(reverse=True)
# print(new)

# new =[63,45,12,25,7,12,23,34]
# val =0
# emty_li =[]
# for i in new:
#     if i==12: 
#        val=  new.index(i)
#        emty_li.append(val)
# print(emty_li)       



# ==============LIST____TASK=============

# my_list = [10, 20, 30, 40, 50]
# print(my_list[1:4])

# fruits = ['apple', 'banana', 'orange']
# fruits.remove('banana')
# print(fruits)

'''my_list = [10, 20, 30, 40, 50, 11,30,30,48]
num = int(input("enter number: "))
emty_list =[]
for i in my_list:
    if i == num:
        emty_list.append(i)
print(emty_list) '''

# ==========dict_tasks=====================

# What is the output of the following code?

'''my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict)) #3'''

# Which method is used to add a new key-value pair to a dictionary?
'''ans: insert()'''

# How can you access the value associated with the key 'age'?
'''my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
print(my_dict['age'])'''

# What happens if you try to access a key that doesn't exist in a dictionary using
# square brackets notation?
'''ans: It adds the key to the dictionary'''

''' ex
dit={}
dit["user"]="sai"
print(dit)'''

# Which of the following methods returns a list of all the keys in a dictionary?
'''ans: keys()'''

# Write Python code to add a new key-value pair to the following 
# dictionary:
'''my_dict = {'name': 'python', 'age': 25}
my_dict["city"]="salur"
print(my_dict)'''

# Write Python code to access and print the value associated with the key 'price' in the following 
# dictionary:
'''product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info["price"])'''

# Write Python code to remove the key-value pair with the key 'city' from the following 
# dictionary:
'''my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop("city")
print(my_dict)'''

# Write Python code to print all the keys present in the following dictionary:
'''my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())'''

# Write Python code to print all the values present in the following dictionary:
'''my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())'''


# ============"********" formation_tasks===============

'''n =int(input("enter number: "))
for i in range(n):
    row ="* "*n
    print(row)'''

'''n =int(input("enter number: "))
for i in range(1,n+1):
    row = "* "*i
    print(row)'''

'''n =int(input("enter number: "))
for i in range(n):
    row = "* "*(n-i)
    print(row)'''

# ================project_is_succes===============



# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)

'''list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 4]
emty_list =[]
for i in list1:
    for j in list2:
        if i == j:
            emty_list.append(i)
print(emty_list)'''

# original_list = [1, 2, 2, 3, 4, 4, 5]
# set_1=set(original_list)
# print(list(set_1))

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# list1.extend(list2)
# print(list1)

# enm = ['lakshmana','sai']
# res= ' '.join(enm)
# print(res)


# -----------STRINGS_TASKS---------------

# sentence = "Python is amazing"
# print(sentence[::2])

# s = "Python is fun and powerful"
# print(s.replace(' ','_'))

# s = "12345"
# print(s.isdigit())

# s = "Python is amazing"
# print(s[::-1])

# ------------THIS IS 'TITLE' NEW METHOD FOR EVERY WORD STARTING LATTER IS CAPITALIZE----------------

'''s = "python programming is fun"
print(s.title())

        (OR)
        
s = "python programming is fun"
emty_list =[]
for i in s.split(' '):
    div=i.capitalize()
    emty_list.append(div)
    jon = ' '.join(emty_list)
print(jon) '''

# ===============set_tasks========================

'''my_set = {1, 2, 3, 4, 5}
print(len(my_set))''' #5

# Which of the following methods is used to add an element to a set?
'''ans: add()'''

# Which of the following statements about sets in Python is true?
'''ans: set are mutable'''

# Write Python code to find and print the intersection of the following two sets:
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
ans: {4,5}'''

# Write Python code to find and print the union of the following two sets:
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
ans: {1, 2, 3, 4, 5, 6, 7, 8}'''

# Write Python code to find and print the elements present in set1 but not in set2 :
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))
ans: {1, 2, 3}'''

# Write Python code to find and print the symmetric difference of the following two sets:
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))
ans: {1, 2, 3, 6, 7, 8}'''

# Write Python code to check if the element 3 is present in the set my_set :
'''my_list = {1,2,3,4,5,6}
print(8 in my_list)'''

# =======================tuple_tasks=====================================

# What does the all() function return when applied to an empty tuple?
'''ans: True'''

# Which of the following statements correctly creates a tuple?
'''ans: tap=(1,2,3)'''

# What is the output of the following code snippet?
'''my_tuple = (1, 2, 3)
print(len(my_tuple))''' #3

# Which of the following statements about tuples in Python is true?
'''ans:  Tuples use parenthesis ( ) for declaration.'''

# Write a program that creates a tuple containing three 
# elements: your name, your age, and your favorite color. Then print the tuple.
'''cre = ("sai","30","black")
print(type(cre))'''

# Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple.
'''tup = ("sun","mon","tue","fri")
print(tup[2])'''

# Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.
'''tup_odd = (1,3,5)
tup_eve = (2,4,6)
print(tup_odd + tup_eve)'''

# Write a program that defines a tuple containing the dimensions of a rectangle (length and width).
# Then, unpack this tuple into two variables and calculate the area of the rectangle.
'''ract =(10,5)
length , width = ract 
print(f"length, {length}")
print(f"width, {width}")
print(f"total area, {area}")'''#Unpacking = breaking the tuple and storing each value in different variables

# Write a program that checks if a given element exists in a tuple.
'''tup = (1,2,3,4,5,6)
print(3 in tup)'''

# ================Bill_Generate mini_progect===========================

# Write a Python program to generate a bill for a supermarket purchase. The
# program should store the items and their prices in a list of tuples. It should
# then iterate over this list to print out each item along with its price. Finally,
# calculate and print the total cost of all the items.
'''items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("item         pric")
print("-----------------")
sum =0
for i,j in items:
    sum+=j
    print(f"{i}      {j}.00")
print("--------------------")
print(f"total        {sum}.00")'''

# =============================functions_tasks===========================================

#  Write a Python function named add that takes two arguments a and b and returns their sum.

'''def add(a,b):
    return a+b
obj = add(10,29)
print(obj*20)'''

'''def sample():
    user = "sai"
    id =1234
    print(user, id)
sample() '''   

# Write a Python function named square that takes a number x as input and returns its square.

'''def square (x):
    return x**int(input("enter number_2: "))
obj = square(int(input("enter square number_1: ")))
print(obj)'''

# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
'''emt_l =[]
def factorial(fact =1):
    n = int(input("enter number: "))
    for i in range(1,n):
        fact*=i
        emt_l.append(fact)
    return print(tuple(emt_l))
factorial()'''

# Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.

'''list_1 = [13,23,54,12,45,67]
emt = []
def maximum():
    for i in list_1:
        emt.append(i)
    return print(max(emt))     
maximum()'''

# Write a Python function named reverse that takes a string s as input and returns its reverse.
'''s= input("enter the string: ")
emp =[]
def reverse ():
    for i in s[::-1]:
       emp.append(i)
    return print(''.join(emp))
reverse()'''

# Write a Python function named sum_of_squares that takes a list of numbers as
# input and returns the sum of the squares of those numbers.

'''list_1 = [12,34,56,12,34]
val=0
emp =[]
for i in list_1:
    val+=(i**2)
    emp.append(val)
print(emp) ''' 


        #    (or)


'''list_1 = [12,34,56,12,34]
def sum_of_square():
    val=0           #local variable
    for i in list_1:
       val+=(i**2)  
    print(val)         
sum_of_square()
'''


# from random import *
# print(randint(10,20))


# -----------------------adv_fun----------------------

# Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of 
# each number in the input list. Use the map() function with a lambda function to implement this.

numbers =  [25,24,58,36,59,56,57,24,28,43]
'''emp =[]
for i in numbers:
    result = i**2
    emp.append(result)
print(emp) '''
# -------------(or)-------------------------
'''result = map(lambda a:a**2 , numbers)
print(list(result))'''

# Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only 
# the positive numbers from  the input list. Use the filter() function with a lambda function to implement this.

'''def filter_positive(a):
    return a%2==0
result = filter(filter_positive, numbers)
print(list(set(result)))'''


# result = filter(lambda a:a%2==0, numbers)
# print(list(result))

# maximum = numbers[0]
# for i in numbers:
#     if i>maximum:
#         maximum=i
# print(maximum)       
# 

# from functools import reduce
# result = reduce(lambda a,b:a if a>b else b, numbers)
# print(result)


# def evn (a,b):
#     yield a+b
#     yield a*b
#     yield a-b
# print(list(evn(10,5)) )   

# def traffic(a):
#     if a =='red':
#       yield a
#     elif a == 'yellow':
#        yield a
#     elif a == 'green':
#        yield a
# obj = traffic(input())
# print(obj.__next__())


'''from functools import reduce
def count_str (str):
    res=0
    for i in str:
        if i in "a,e,i,o,u":
            res+=1
    print(res)
count_str(input("enter string: "))''' 


'''from functools import reduce
def coint (str):
    vowels ="aeiouAEIOU"
    count = reduce(lambda tot,char: tot+(1 if char in vowels else 0), str,0)
    return print(count)
coint(input("enter the string: "))'''

# ============================================oops_tasks=============================================

'''class mobile():
    RAM = "128gb"
    ROM = "8gb"
    def camera(self,brand):
        print(f"butifull camera in...{brand} mobile brand")
        print(f"very fast and picture clarity space in...{self.ROM} ROM")
    def browsing(self,application):
        print(f"best browsing internet...{application} application")
        print(f"stroge accuepay in... {self.RAM} RAM")
    def music(self):
        print("listing music")
        
vivo = mobile()
vivo.camera("vivo")
vivo.browsing("google")
vivo.music()

oppo = mobile()
oppo.camera("oppo")
oppo.browsing("opra_mini")
oppo.music()'''


'''class name():
    def __init__(self,mobile_no,m_name):
        self._mobile_no = mobile_no
        self.m_name = m_name
    def mobile_1(self):
        if len(self._mobile_no) == 13 and self._mobile_no[0] =="+":
            print("enter the number: ",self._mobile_no)
        else:
            print("mobile number is must 11 digits and + symbol ")
    def name_2(self):
        print("enter the mobile brand name: ",self.m_name)

obj = name(input("enter mobile_number: "),input("enter m_name: "))
obj.mobile_1()
obj.name_2() '''  


'''fill_name = open("fill_text.txt",mode="r")
new_one = fill_name.readline()
print(new_one)
fill_name.close()'''


'''x =[1,2,3,4,5]
for i in x:
    if i==3:
       x.remove(i)  
print(x) '''  

'''cities = ["Berlin","Rome","Madrid"]
print(max(cities))'''

'''NUMS = [1,2,3,4,5,6]
for i in NUMS:
    if i%2==0:
        NUMS.remove(i)
print(NUMS) '''  

'''nums = [3,5,7,9]
nums.insert(2,4)
print(nums)'''

'''basket1 ={"apple","banana","cherry"}
basket2 ={"banana","cherry","date"}
print(basket1 - basket2)    -----------like mines in sql'''

'''x =[10,20,30]
x.append((40,50))
print(len(x))'''

'''num = [1,2,3,4]
num.remove(3)
num.append(5)
print(num)'''


# a = 1000
# b = 10 * 100
# c = int("1000")
# d = 500 +500
# print(a is b)
# print(id(a) ,id(b), id (d))


'''b =int("123")
print(b+2)'''


'''food = "pizza"
food.replace("z","s")
print(food)''' 
# ====pizza

# or

'''food = "pizza"
re = food.replace("z","s")
print(re)  '''
# ====pissa

'''car =["bmw","porch","audi"]
trand =[]
for i in car:
    if i =="porch" or"bmw":
        trand.append(i)
print(trand)'''
# =====["bmw","porch","audi"]

# a=[1,2]
# b=[1,2]
# print(id(a) , id(b), a==b)

# x =[1,2,3]
# print(x * 2)
# ans: [1,2,3,1,2,3]

'''reply = ""
if reply:
    print("happy")
else:
    print("sad")'''
# ans: sad

'''item ={"milk","bread","milk"}
print(len(item))'''


# cards = ("shoes","bag","watch")
# a,b,c = cards
# print(b)


# countries = ["america","canada","indai","australia","china","chile","california"]
# print(*countries, sep="\n")

'''countries = ["america","canada","indai","australia","china","chile","california"]
for i in countries:
    if i.startswith("c"):
        countries.remove(i)
print(countries) '''   

'''value =[1,2,3,4,5,6,7]
for i in value[:5]:
    if i%2==0:
        value.remove(i)
print(value) '''    


# for i in range(3):
#     print(i)
#     i=10


# x =(1,2,[3,4])
# x[2].append(5)
# print(x)


'''larg=[3,1,4,1,5,9,2,6]
uniqe= list(set(larg))
print(uniqe)
higest = max(uniqe)
print(higest)
uniqe.remove(higest)
print(uniqe)
second = max(uniqe)
print(second)'''



           




