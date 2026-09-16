num1 = float(input('escreva um número: '))
num2 = float(input('digite outro número: '))
if num1 > num2:
    print(f'o numero {num1} é maior que {num2}')
elif num1 < num2:
    print(f'o numero {num1} é menor que {num2}')    
else:
    print(f'os numeros {num1} e {num2} são iguais')