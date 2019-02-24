#funcoes
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#programa principal
soma(2, 3)
soma(a=2, b=3)
soma(b=2, a=3)

#é possivel passar parametros tradiconalmente e passar nomeando. Se nomear, nao precsa seguir a ordem de declaração