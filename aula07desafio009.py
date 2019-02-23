#faca um programa que leia um numero inteiro e
#mostre na tela a sua tabuada

num = int(input('Calcular a tabuada de: '))
for i in range(10):
    print('{}x{}={}'.format(num, i+1, num*(i+1)))