def calcular(operacao, a, b ):
    if operacao == 1:
        return a+b
    elif operacao == 2:
        return a-b
    elif operacao == 3:
        return a/b
    elif operacao == 4:
        return a*b
    else:
        return "Operação inválida"

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))

op = int(input("Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\nSua escolha: "))

print("Resultado: %d" % calcular(op, numero1, numero2))