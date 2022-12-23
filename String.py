tamanho = "um valor ai de alguma valor pra puxar posicao e valor"

"""

print(tamanho[1 : 6]) # mostra a posicao de x até y.
print(tamanho.strip()) # remove os espaços do começo e final
print(tamanho.lower().strip()) # converte tudo em minusculo
print(tamanho.upper().strip()) # converte tudo em maiusculo
print(tamanho.replace("valor", "penis").strip()) # altera o valor no obj
x = tamanho.split(" ") # divide os valores pelos espaços
print(x[5])
print(tamanho.split(" ")) # tornou-se split, converte para array/list
print("tamanho do tamanho: " + str(len(tamanho))) # quantos caracteres há no obj

"""

#-====================================================================================================================-#

existe = "alguma" in tamanho # pergunta existe o valor no obj
print(existe)

nexiste = "alguma" not in tamanho # pergunta não existe o valor no obj
print(nexiste)

# outra maneira de pesquisar

palavra = "Alguma"
res = palavra in tamanho
print(res) # ele vai dar como falso porque o "A" esta maiúsculo

palavra = "Alguma"
res = palavra.upper() in tamanho.upper()
print(res) # agora tudo convertido para upper, consegue encontrar

x = "penis "
y = 3
z = " finasterida"

e = x + str(y) + z
print(e)

cidade = "jundiai"
dia = 12
mes = "dezembro"
ano = 2022
kkk = "mae do natan é obesa"
data = "{}, {} de {} de {} \n\n\n \"{}\"" # placeholder é um dado reservado

print(data.format(cidade,dia,mes,ano,kkk)) # .format vai unificar tudo como uma unica classe??
ss = data.format(cidade,dia,mes,ano,kkk)
print(type(ss))


# tipor de escape: \n enter, \" aspas impressas, \' apostrofo impresso, \r espaço, \t tab, \b backspace.