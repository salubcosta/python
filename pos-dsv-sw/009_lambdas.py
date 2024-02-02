f = lambda x,y=3 : x*y

print(f(2,4)) # 8

print(f(7)) # 21


l = lambda x, y, z : x*y*z
print(l(z=3,y=10,x=0)) # 0


def somaTres(a,b,c):
    '''
    Esta função realiza a soma de três valores
    '''
    return a+b+c

print(somaTres.__doc__) # Retorna o comentários da função