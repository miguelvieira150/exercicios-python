positivos = 0
numero = float(input('Digite um numero: '))

while numero != 0:
    if numero > 0:
        positivos = positivos + 1
    numero = float(input('Digite outro numero: '))

print(f'Quantidade de numeros positivos digitados: {positivos}')