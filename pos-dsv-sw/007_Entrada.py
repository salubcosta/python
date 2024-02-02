nome = input("Informe seu nome: ")

saudacao = "Olá, "+nome

print(saudacao)

try:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
except:
    print("Favor, informe apenas números inteiros.")
else:
    print(n1+n2)