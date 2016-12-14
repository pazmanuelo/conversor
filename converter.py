'''codigo para convertir temperaturas'''

def conversor():
    print("1)C->F\n2)F->C\n3)K->C\n4)C->K\n5)F->K\n6)K->F")
    operador = int(input("Indique el numero para la transformacion "))

    if operador == 1:
        temp = int(input("Temperatura en grados Celsius "))
        convertCaF = temp * 1.8 + 32
        print(str(temp)+" grados Celsius es igual a "+ str(convertCaF)+ " Farenheit")


    elif operador == 2:
        temp = int(input("Temperatura en grados Farenheit "))
        convertFaC = (temp-32)/1.8
        print(str(temp)+" grados Farenheit es igual a "+ str(convertFaC)+ " grados Celsius")


    elif operador == 3:
        temp = int(input("Temperatura en Kelvin "))
        convertKaC = temp-273.15
        print(str(temp)+" Kelvin es igual a "+ str(convertKaC)+ " grados Celsius")


    elif operador == 4:
        temp = int(input("Temperatura en grados Celsius "))
        convertCaK = temp+273.15
        print(str(temp)+" grados Celcius es igual a "+ str(convertCaK)+ " Kelvin")


    elif operador == 5:
        temp = int(input("Temperatura en grados Farenheit "))
        convertFaK = (5/9)*(temp-32)+273.15
        print(str(temp)+" grados Farenheit es igual a " + str(convertFaK) + " Kelvin")


    elif operador == 6:
        temp = int(input("Temperatura en Kelvin "))
        convertKaF = 1.8*(temp-273.15)+32
        print(str(temp)+" Kelvin es igual a " + str(convertKaF) + " grados Farenheit")

    otravez()

def otravez():
    denuevo = input("Desea convertir otra temperatura? S o N\n")
    if denuevo.upper() == "S":
        conversor()

    else:
        print("====Hasta Luego====")

def hola():
    print("Conversor de unidades de temperatura")

hola()
conversor()
