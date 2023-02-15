# letter= input("Podaj literę: ")
# i = 0
#
# while letter !="":
#     print(letter)
#     i+=1
#     if i == 5:
#         letter=input("Podaj kolejną: ")
#         i =0
# print("bye bye")
#
# st = "\nPodaj imie"
# st +="\n(Wpisz q aby zakończyć)"
#
# while True:
#     name = input(st)
#     if name == "q":
#         break
#
#     print(f"wpisano imię {name.title()}")
#
from math import sqrt

# num = 0
# while num < 100:
#     num+=1
#     if num % 3 == 0 or num % 5 == 0:
#         continue
#     print(num)
from time import time
#
# counter = 0
# for n in range(2,100):
#     is_prime = True
#     s = int(sqrt(n))
#
#     for i in range(2,s +1):
#         if n%i ==0:
#             is_prime = False
#             break
#     if is_prime:
#         counter+=1
#         print(f"{n}: jest pierwsza")
#
# print(f"liczb pierwszych jest {counter}")
#
# i=0
# x=40
#
# while (expression:=5*x*i+1)<1000:
#     print(f"{i}: {expression}")
#     i+=1


sum = 0
for i in range(1,101):
    sum+=i
print(sum)