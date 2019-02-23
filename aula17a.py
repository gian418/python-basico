num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

a = [2, 3, 4, 7]
#b = a #dessa maneira so referencia e nao copia.. se mexer em b, mexe em a
b = a[:] #dessa maneira copia a em b utilizando fatiamento. Se mexer em b não altera a a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')