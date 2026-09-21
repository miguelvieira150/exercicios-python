lista = [5, 12, 8, 20, 3, 15]
contador = 0
for item in lista:
    if item > 10:
        contador = contador + 1

print(f'Quantidade de itens maiores que 10: {contador}')