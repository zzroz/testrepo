#preguntando cuantos vectores
while True:
    try:
        nuvectores=input('cuantos vectores: ')
        nuve=int(nuvectores)
        break
    except ValueError:
        print('Entrada inválida!!!!')

#creando cantidad de vectores
contador1=0
nuveclis=list()
while contador1!=nuve:
    contador1=contador1+1
    nuveclis.append(contador1)

#almacenando los vectores
Tvectores=list()

for k in nuveclis:
    print('\n',nuveclis[k-1],'vector: ')
#preguntando cuantas componentes y volviendolo entero
    while True:
        try:
            componentes=input('\ncuantas componentes: ')
            com=int(componentes)
            break
        except ValueError:
            print('Entrada inválida!!!!')

#creando una lista para recorrer cada componente
    contador=0
    cancomp=list()
    while contador!=com:
        contador=contador+1
        cancomp.append(contador)
#ingresando las componentes
    vector=list()
    for i in cancomp:
#try para repetir si la entrada no sirve
        while True:
            try:
                c1=input('ingresa '+str(i)+' componente: ')
                vc1=float(c1)
                vector.append(vc1)

                break
            except ValueError:
                print('Entrada inválida!!!!')

    Tvectores.append(vector)#guardando los vectores
    print('\neste es el',nuveclis[k-1], 'vector: ',vector)

#ver vectores? redundante por ahora pero sirve
cualvector=input('\n cual vector quiere ver?: ')
intcualvector=int(cualvector)
print(Tvectores[intcualvector-1])

#preguntando la operación para hacer
operaciones=['suma', 'punto', 'cruz']
operacion=input('¿que quiere hacer?[suma/punto/cruz]: ')
res=list()
if operacion=='suma':
    cuantosop=input('todos? [s/n]')
    if cuantosop=='s':
        for k in Tvectores:
          for i in Tvectores[k]:
               res.append(Tvectores[i])

print(Tvectores[:][1])
