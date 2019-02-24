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

#----------------
#recebe quantidade aleatorias de parametros e transforma em tupla
def contador(*num):
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2)


#-------------
def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma2(5, 2)
soma2(2, 9, 4)
