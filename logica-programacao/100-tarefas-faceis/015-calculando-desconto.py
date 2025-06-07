# 15. Calculando Desconto
# Crie um programa que calcule o preço final de um produto de R$493 com 19% de desconto.
valor_produto = float(input("Informe o preço de um produto: "))
desconto = float(input("Informe a porcentagem de desconto: "))

valor_final = valor_produto - valor_produto * (desconto/100)

print(f"O valor final do produto com desconto é de: R$ {valor_final}")