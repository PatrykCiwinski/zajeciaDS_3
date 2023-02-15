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
num = 0
while num < 100:
    num+=1
    if num % 3 == 0 or num % 5 == 0:
        continue
    print(num)