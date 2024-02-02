preco = 8.755548

print("Valor: %.2f" % preco)


# Cria arquivo e escreve com conteúdo do print. Se quiser adicionar precisa alterar o w por a de append
arquivo = open("arquivo", "w")
print("PRIMEIRA LINHA", file=arquivo)
arquivo.close()