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

st = "\nPodaj imie"
st +="\n(Wpisz q aby zakończyć)"

while True:
    name = input(st)
    if name == "q":
        break

    print(f"wpisano imię {name.title()}")