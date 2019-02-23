#escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milimetros.

metros = float(input('Informe valor em metros: '))
print('Centimetros: {}\nMilimetros {}'.format(metros*100, metros*1000))