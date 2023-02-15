users = ['anna01', 'bob7', 'susan']

while (u:=input('Podaj użytkownika: ')) !='':
    if u not in users:
        print(f'{u} zrejestruj się')
    else:
        print('{u} przejdź do logowania')
print('Koniec')