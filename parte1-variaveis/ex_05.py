preco = float(input('digite o preço do produto: '))
quantidade = int(input('digite a quantidade comprada: '))

valor_total = preco * quantidade
print(f'valor total: R$ {valor_total:.2f}')