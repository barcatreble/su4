#1
# num = input("Въведи числа: ")
# lst = list(map(int, num.split()))
# max = 0
# for i in lst:
#     if i > max:
#         max = i
        
# print(f"Най- голямото число в списъка е: {max}")

#2
# user_input = input("Напишете текст: ")
# dumi = user_input.split()
# for duma in dumi:
#     if len(duma) > 5:
#         print(duma)
        
#3
# user_input1 = input("Напишете елементите на първия списък: ")
# lst1 = user_input1.split()
# user_input2 = input("Напишете елементите на втория списък: ")
# lst2 = user_input2.split()
 
# for i in lst1:
#     for j in lst2:
#         if i==j:
#             print("Съвпадащите елементи са: ", i)

#4
# num = input("Въведи числа: ")
# lst = list(map(int, num.split()))
# chetni = []
# nechetni = []
# for i in lst:
#     if i % 2 == 0:
#         chetni.append(i)
#     else:
#         nechetni.append(i)
        
# print("Четните числа са:", chetni)
# print("Нечетните числа са:", nechetni)

#5
# num = input("Въведи числа: ")
# numbers = list(map(int, num.split()))
# avg = 0
# for i in numbers:
#     avg += i
    
# avg = avg/len(numbers)
# avg_list = []
# for i in numbers:
#     if i > avg:
#         avg_list.append(i)
        
# print("Числата по-големи от средната стойност на списъка са:", avg_list)

#6
# num = input("Въведи списък от числа:")
# numbers = list(map(int, num.split()))
# avg = 0
# for i in numbers:
#     avg += i
# avg = avg/len(numbers)    
# chislo = int(input("Въведи число:"))
# for i in numbers:
#     if i < avg and i > chislo:
#         print(i)

#7
# num = input("Въведи списък от числа:")
# numbers = list(map(int, num.split()))
# def nai_golqmo(numbers):
#     max = 0
#     for i in numbers:
#         if i > max:
#             max = i
#     return max
    
# print("Най-голямото число е:",nai_golqmo(numbers))

#8
# num = input("Въведи списък от числа:")
# numbers = list(map(int, num.split()))
# def suma_nad10(numbers):
#     sum = 0
#     for i in numbers:
#         if i > 10:
#             sum +=i
#     return sum
    
# print("Сумата на числата по-големи от 10 е:",suma_nad10(numbers))

#9
# num = input("Въведи списък от числа:")
# numbers = list(map(int, num.split()))
# def chetni(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count+=1
#     return count

# print("Броят на четните числа е:", chetni(numbers))

#10.1
# duma1 = input("Въведи дума:")
# bukvi1 = list(duma1)
# duma2 = input("Въведи друга дума:")
# bukvi2 = list(duma2)
# count = 0
# for i in duma1:
#     for j in duma2:
#         if i == j:
#             count+=1
# if count == len(duma1):
#     print("Анаграми")
# else:
#     print("Не са анаграми")
    
#10.2
# duma1 = input("Въведи дума:").lower()
# duma2 = input("Въведи дума:").lower()
# if sorted(duma1) == sorted(duma2):
#     print("Анаграми")
# else:

#     print("Не са анаграми")

#class
#1
class Account:
    def __init__(self, pin, account_number, balance):
        self.pin = pin
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount, pin):
        if pin != self.pin:
            print("Грешен ПИН код")
            return       
        if amount > self.balance:
            print("Балансът не може да стане отрицателен.")
            return     
        self.balance-=amount
                           
    def get_account_info(self):
        print("Номер на сметката:", self.account_number)
        print("Баланс:", self.balance)
        
account_number = input("Номер на сметката:")

while True:
    try:
        balance = int(input("Начален баланс:"))
        break
    except ValueError:
        print("Балансът трябва да е с цифри.")

while True:
    try:
        pin = int(input("ПИН код:"))
        break
    except:
        print("ПИН кодът трябва да е с цифри.")

bank_acc1 = Account(pin, account_number, balance)

while True:
    print("="*18)
    print("МЕНЮ")
    print("="*18)
    print("1. Депозит\n2. Теглене\n3. Инфо за сметката")
    print("="*18)

    nomer = int(input("Въведете номер на операция:"))
    match nomer:
        case 1:
            amount = int(input("Депозит:"))
            bank_acc1.deposit(amount)
        case 2:
            amount = int(input("Сума за теглене:"))
            entered_pin = int(input("ПИН код:"))
            bank_acc1.withdraw(amount, entered_pin)
        case 3:
            bank_acc1.get_account_info()
