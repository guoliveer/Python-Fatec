#Conjuntos
print("Software para teoria de conjutos")
conjL = str(input("Entre com o conjunto universo: ")).split()
conjA = str(input("Entre com os elementos do conjunto A separados por 'Espaço': ")).split()
conjB = str(input("Entre com os elementos do conjunto B separados por 'Espaço': ")).split()
conjT = list()
conjU = list()
if len(conjL) == 0:
    print("Não ha complementares dos conjuntos A e B")
else:
    for k in conjL:
        if k not in conjA:
            conjT.append(k)
uniao = conjA + conjB
uniao = list(set(uniao))
uniao.sort()
print("A uniao dos conjuntos é: %s" %(uniao))
inter = list()
x = 0
sub = list()
for k in conjA:
    if k in conjB:
        inter.append(k)
        x = len(inter)
    else:
        sub.append(k)
if x == 0:
        print("A intersecção é um conjunto Vazio!")            
else:
        print("A intersecção dos conjuntos é: %s"%inter)
print(inter)
print('A Subtração de A-B: %s' %sub)
subb = list()
for k in conjB:
    if k not in conjA:
        subb.append(k)
print('A Subtração de B-A: %s' %subb)
print("O complementar do conjunto A é: %s" %conjT)
if len(conjL) == 0:
    print("Não ha complementares dos conjuntos A e B")
else:
    for k in conjL:
        if k not in conjB:
            conjU.append(k)
print("O complementar do conjunto B é: %s" %conjU)
print("Desenvolvido por Gustavo e Jonathan afim de ajudar nas aulas de matemática discreta")
