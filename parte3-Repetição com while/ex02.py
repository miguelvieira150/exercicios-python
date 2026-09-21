soma = 0
numero = float(input('Digite um numero: '))

while numero >= 0:
    soma = soma + numero
    numero = float(input('Digite outro numero: '))

print(f'A soma total é: {soma}')