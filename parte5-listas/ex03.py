numeros = [4, 8, 15, 16, 23]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print(f'O maior número da lista é: {maior}')