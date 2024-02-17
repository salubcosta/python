produto = {
    'codigo':0,
    'descricao': '',
    'preco': 0.0,
    'qtde': 0.0
}

produto['codigo'] = int(input("Informe o código do produto: "))
produto['descricao'] = input("Informe a descrição do produto: ")
produto['preco'] = float(input("Informe o preco do produto: "))
produto['qtde'] = float(input("Informe a quantidade do produto: "))

for chave,valor in produto.items():
    print(chave, valor)