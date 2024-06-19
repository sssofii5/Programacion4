##Tablas de multiplicar
a=1
while a!=0:
    a=int(input("Dame el valor y te devuelvo la tabla de multiplicar"))

    for i in range(1,11):
        print(f"(i)x(a)=")
        print(i*a)
print('Programa finalizado1')