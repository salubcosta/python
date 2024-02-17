matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        print("Insira o elemento da linha %s, coluna %s: " % (i, j))
        dado = int(input())
        linha.append(dado)
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print("O elemento da linha %s, coluna %s é: %s" % (i,j,matriz[i][j]))