#Creacion de las variables
want_great="S" 
vaild_eptions= 0

#Inicia bucle con la condiccion verdadera
while want_greet== "S":     
    print("hola que tal! ")
    want_greet= input("¿quiere otro saludo?")
    #Verificaccion de input
    if want_greet not in "s":
        print("No le he entendido pero le sali")
        want_greet="s"
        continue
    vaild_eptions += 1
    print(f"(vaild_options)repuestas validas")
    print("que tenga un buen dia")
