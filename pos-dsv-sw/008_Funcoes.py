def imprimeMsg(msg):
    print(msg)


imprimeMsg("Hello, world!")

def soma(numero1, numero2):
    return numero1+numero2

print(soma(7,3))

def multiplicaNumeros(*varArgs):
    total = 0
    for arg in varArgs:
        if total == 0:
            total = arg
        else:
            total *= arg
    return total
    
print(multiplicaNumeros(3,2,3,2)) # 36 = 3*2*3*2