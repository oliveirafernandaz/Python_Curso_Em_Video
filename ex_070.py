cont_mil = menor = cont = 0
nome_produtos = []
cont_preco = []
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    zipped = list(zip(nome_produtos, cont_preco))
    for n, p in zipped:
        minimo_valor = min(cont_preco)
        if p == minimo_valor:
            barato = n
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if preco > 0:
        cont_preco.append(preco)
    if preco > 1000:
        cont_mil += 1
    if continuar == 'n':
        break

print(f'O valor total da compra foi de R${sum(cont_preco)}.')
print(f'Temos {cont_mil} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato foi {barato} e custou R${min(cont_preco)}.')

