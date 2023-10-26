menu = int(input('seleccione del menu: 1, 2 o 3: '))
if menu == 1:
    n1 = int(input('ingrese primer numero: '))
    n2 = int(input('ingrese segundo numero: '))
    # el segundo mayor al primero (n2 > n1)
    while n1 > n2:
        n2 = int(input('ingrese segundo numero: '))
    print(n2, 'es mayor que ', n1)
elif menu == 2:
    n1 = int(input('ingrese primer numero: '))
    n2 = int(input('ingrese segundo numero: '))
    # comparar el n2 hasta que sea menor n1
    while n2 > n1:
        n2 = int(input('ingrese segundo numero: '))
    print('fin')
elif menu == 3:
    print('terminar programa')
else:
    print('no existe opcion')

