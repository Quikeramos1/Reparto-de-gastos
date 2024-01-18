def pedir_datos():
    nombre_1 = ""
    while nombre_1 == "":
        nombre_1 = input("Introduce el nombre de la persona 1: ")
        try:
            no_vacio(nombre_1)
        except ValueError as e:
            print(f"Error: {e}")

    nombre_2 = ""
    while nombre_2 == "":
        nombre_2 = input("Introduce el nombre de la persona 2: ")
        try:
            no_vacio(nombre_2)
        except ValueError as e:
            print(f"Error: {e}")

    sueldo_1 = ""
    while sueldo_1 == "":
        sueldo_1 = input(f"Introduce sueldo de {nombre_1}: ")
        
        try:
            no_vacio(sueldo_1)
        except ValueError as e:
            print(f"Error: {e}")

    sueldo_2 = ""
    while sueldo_2 == "":
        sueldo_2 = input(f"Introduce sueldo de {nombre_2}: ")
        
        try:
            no_vacio(sueldo_2)
        except ValueError as e:
            print(f"Error: {e}")
    float(sueldo_1)
    float(sueldo_2)
    tasa_1, tasa_2 = calcular_aportacion(sueldo_1, sueldo_2)
    gastos = {}
    introducir = input("¿Quires introducir los gastos? (S/N): ").lower()

    if introducir == "s":
        n_gasto = "ok"
        while n_gasto != "":
            n_gasto = input("Introduce el concepto del gasto o deja en blanco para finalizar: ")
            if n_gasto == "":
                cantidad_pagar(gastos,nombre_1,nombre_2,tasa_1, tasa_2)
                break    
            importe_gasto = input("Introduce el importe del gasto: ")
            gastos[n_gasto]= float(importe_gasto)
            print(gastos)
        
    elif introducir != "s":
        print("Saliendo del programa")
        exit()   

def no_vacio(dato):
    if dato == "":
        print("El campo no puede estar vacío")
        raise ValueError("Campo vacío: " + dato)
           
            
def calcular_aportacion(sueldo_1, sueldo_2):
    sueldo_1=float(sueldo_1)
    sueldo_2=float(sueldo_2)
    total = sueldo_1 + sueldo_2
    tasa_1 = (sueldo_1 / total)*100
    tasa_2 = (sueldo_2 / total)*100
    return tasa_1,tasa_2

def cantidad_pagar(gastos,nombre_1,nombre_2,tasa_1, tasa_2):
    total1=[]
    total2=[]

    for clave, valor in gastos.items():
        tasa_valor_1 = (int(valor)* int(tasa_1))/100
        tasa_valor_2 = (int(valor)* int(tasa_2))/100
        total1.append(float(tasa_valor_1))
        total2.append(float(tasa_valor_2))
        print(f"{nombre_1}, tiene que pagar de {clave}: {tasa_valor_1}")
        print(f"{nombre_2}, tiene que pagar de {clave}: {tasa_valor_2}")

    print(f"\nEl total acumulado de {nombre_1} es de {sum(total1)}")
    print(f"El total acumulado de {nombre_2} es de {sum(total2)}\n")
        