

def med():
    print(          'ALGORITMO CALCULA MÉDIA, MEDIANA E MODA!!!\n Gustavo Oliveira!      Professora Nanci <3\n')
    med = []
    x=int(input("Entre com a quantidade de valores:"))
    i=1
    while(i<=x):
        med.append(int(input('Entre com '+str(i)+' valor: ')))
        i=i+1            
    media=(sum(med)/x)
    print('\nA média é: ',media,'\n\n')


    if len(med) % 2 == 0:                                                                      
        n = len(med)/2
        mediana=((med[int(n-1)]+med[int(n)])/2)
        print('Mediana com numero par: ',mediana,'\n\n')                                                   
    else:
        n = len(med)/2
        mediana = med[int(n)]
        print('Mediana com numero impar: ',mediana,'\n\n')


    repete = 0                                                                         
    for i in med:                                                                              
        aparece = med.count(i)                                                             
        if aparece > repete:                                                       
            repete = aparece
            
    modas = []                                                                               
    for i in med:                                                                              
        aparece = med.count(i)                                                             
        if aparece == repete and i not in modas:                                   
            modas.append(i)                                                                  
                                                                                             
    print ("moda:", modas,'\n\n')  




def proba():
    print("ALGORITMO DE PROBABILIDADE !!!!! \n Gustavo Oliveira!         Professora Nanci <3\n")
    lista = []
    amostral = []
    x=int(input("Entre com espaço amostral: "))
    z=int(input("Entre com quantidade eventos: "))
    i=1
    j=1

    while(j<=x):
        amostral.append(j)
        j+=1
        
    #while(i<=z):
     #   lista.append(int(input("Entre com evento "+ str(i) +":")))
      #  i = i+1 
    #i=1
    #cont=0
    #for k in lista:
     #   if k in amostral:
      #     cont+=1
    #r=cont/x
    r=z/x
    if r == 0:
        print("    O evento é Impossivel!!!\n\n")
    else:
        print('A probabilidade é de:%.3f '% r,'ou %.2f'%(r*100),'%\n\n')


ans=True
while ans:
    print('''             ||=================================================||
             ||            Escolha uma operação                 ||
             ||          1- Algoritmo Probabilidade.            ||
             ||          2- Algoritmo de Media, Mediana e moda. ||
             ||          0 - SAIR !!                            ||
             ||=================================================||''')
    ans=int(input())
    if ans == 1:
        proba()
    elif ans == 2:
       med()
    elif ans == 0:
        False
    else:
        print('Valor Incorreto!')
