print('\033[35m{:=^40}\033[m'.format(' CONVERSOR DE MEDIDAS'))

m = float(input('Qual o valor (em metros)? '))
print(f'\033[31m{m / 1000 :.3f}km\033[m')
print(f'\033[31m{m / 100 :.2f}hm\033[m')
print(f'\033[31m{m / 10 :.1f}dam\033[m')
print(f'\033[31m{m :.0f}m\033[m')
print(f'\033[31m{m * 10 :.0f}dm\033[m')
print(f'\033[31m{m * 100 :.0f}cm\033[m')
print(f'\033[31m{m * 1000 :.0f}mm\033[m')
