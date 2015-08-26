lista = enumerate('zero um dois três quatro cinco seis sete oito nove'.split())
numero_string=dict(lista)
string_numero={valor:chave for chave,valor in numero_string.items()}
print (numero_string)
print(string_numero)

def para_numeral(n):
    numeros=[]
    for digito in str(n):
        numeros.append(numero_string[int(digito)])

    return ", ".join(numeros)


assert "um" == para_numeral(1)
assert "um, dois" == para_numeral(12)
assert "um, um" == para_numeral(11)


def para_inteiro(string_n):
    string=""
    lista=string_n.split(", ")
    for digito in lista:
        string+=str(string_numero[digito])
    return int(string)


assert 1== para_inteiro('um')
assert 12== para_inteiro('um, dois')
