import random

numI=10
numF=5.2
numC=7j

x=numI
y=numF
z=numC

print("valor: " + str(x) + " - Tipo: " + str(type(x))) # aqui ele mostra o valor e o tipo, deve ser formatado para str para concanar
print("valor: " + str(y) + " - Tipo: " + str(type(y)))
print("valor: " + str(z) + " - Tipo: " + str(type(z)))


# para realizar converção é só chamar o formato a frente da variavel

numR=[  # isso é uma lista aleatória array
    random.randrange(1, 267),
    random.randrange(1, 267),
    random.randrange(1, 267),
    random.randrange(1, 267),
    random.randrange(1, 267),
    random.randrange(1, 267)
]

xR=numR

print("loucura loucura: " + str(xR))