moto = ["fan", "factor", "titan", "ninja", "noeli"]
moto.append("kavazaki") # adiciona valor ao array
moto.append("magda")
moto.append("fuvest")

print(str(len(moto)) + " moto na lista ai po:\n" + str(moto))

moto.remove("magda")
print(str(len(moto)) + " moto na lista ai po:\n" + str(moto))

moto.pop() # remove a ultima
print(str(len(moto)) + " moto na lista ai po:\n" + str(moto))

del moto[0] # deleta a partir da posição
print(str(len(moto)) + " moto na lista ai po:\n" + str(moto))

moto2 = ["MOTO SEXO", "MOTO PENIS", "HAMBURGUER"]
moto3 = moto + moto2 # une as listas

print(str(len(moto3)) + " moto na lista ai po:\n" + str(moto3))


moto.clear() # limpa a porra toda
print(str(len(moto3)) + " moto na lista ai po:\n" + str(moto3))