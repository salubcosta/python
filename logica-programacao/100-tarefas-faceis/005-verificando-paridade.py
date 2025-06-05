# 5. Verificando Paridade
# Crie um programa que verifique se o número 73 é par ou ímpar.

number = 73

result = "Ímpar"
if number % 2 == 0:
    result = "Par"

print("O número é %s" % result)