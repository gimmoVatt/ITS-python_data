

''''def es_4_8():
    numbers= list (1,11)

    cubi=[] 
    for n in numbers:
        cubi.app9


  '''

''''''
'''dict={5:4,4:45,4:6}

for k in dict:
    print ("poc nient")

'''
''''n=int(input("inserisci un numero:  "))

match n:
    case n if n >0:
        print(f"numero {n}maggiore di zero")
    case n if n==0:
        print(f"numero{n} è neutro")
    case _:
        print(f"il numnero {n}è minore di zero ")







'''

'''neonato=int(input("inserisci un numero di bambini : "))

match neonato:
    case 1:
        print("congratulazioni")
    case 2:
        print("mortacci tua!!")
    case 3:
        print("ma stralimortacci tua!!")
    case _:
        print(f"ma stralimortacci tua {neonato} bambini !!")



'''

'''name=str(input("inserisci il propio nome :  "))
genere=str(input("inserisci genere f o m:  "))
print(f"name: {name}")

match genere:
    case "m":
        print("è maschio")
    case "f":
        print("è femmina")
    case _:
        print(" è assessuato")
        '''

'''voto=int(input("inserisci un voto:  "))

match voto:
    case 10:
        print("eccdellene")
    case 8|9:
       print("molkto buono")
    case 6|7:
        print("sufficente")
    case 4|5:
        print("non sufficente")
    case _:
        print("voto non valido")
        '''


oggetti=[]
counter=0
while counter<3:
    oggetti.append(str(input("inserisci un oggetto: ")).lower)
    counter+=1

match oggetti:
    case "penna","matita","quaderno":
          print("scuola")
    case "pane","latte","uova":
          print("prodotti alimentari")
    case "sedia","tavolo","armadio":
          print("mobili")
    case _:
          print("non è nessuno di questi")



