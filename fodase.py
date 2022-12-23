a = int(input('digita um valor ai vadio'))
b = int(input('oto'))

soma = a + b
menosAi = a - b
mutiplica = a * b
divigi = a / b
maedonatan = a % b

print(soma)
print(menosAi)
print(mutiplica)
print(divigi)
print(maedonatan)
soma = str(soma)

print(type(soma))
print('soma: ' + soma)

# converção é feita indicando a classe e colocando entre parenteses a variavel, como ex:
divigi = int(divigi)
print(divigi)


# tem como fazer uma converção não definitiva
print('multi: {}'.format(mutiplica))
print('multi: {} \ndivigi: {} '.format(mutiplica, divigi))

print('\n\n\na mãe do natan é minha')

from random import randint