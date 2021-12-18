while True:
    try:
        entrada=input('Introduzca un Número: ')
        x=int(entrada)
        break
    except ValueError:
        print('Entrada inválida!!!!')
n=1
np=0
ni=0
while x>=4:
    n=n+1
    if x % 2!=0:
        print('Par->',int(x))
        x=x/2
        np=np+1

    else:
        print('Impar-> ',int(x))
        x=3*x+1
        ni=ni+1


print('Finalizado Total=',n,' Pares=',np,' Impares= ',ni)
