lista_a = []

lista_b = [10,20,30]

lista_c = [3.14, lista_a, lista_b]

print(lista_c)

lista_c.append(99)

print(lista_c)

print(lista_c.pop())

print(lista_c)

# TESTANDO.
lista = []

for i in range(5):
    dado = input("Digite o elemento da posição %d: " % i)
    lista.append(dado)

print("Lista preenchida:")

for i in range(5):
    print("O elemento da posição %s é: %s" % (i, lista[i]))