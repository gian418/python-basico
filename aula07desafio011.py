#faca um programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta-la
#sabendo que cada litro de tinta pinta uma de 2m²

altura = float(input('Altura: '))
largura = float(input('Largura '))

area = altura*largura
qtdTinta = area/2;

print('Area: {} m²\nTinta necessaria: {} litros'.format(area, qtdTinta))