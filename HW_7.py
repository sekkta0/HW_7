slovo = input('Введіть слово')
new = slovo[::-1]
if new == slovo:
    print('Не паліндромом')
else:
    print('Паліндромом')  