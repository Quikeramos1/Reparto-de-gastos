def pedir_datos():
    nombre_1 = input("Introduce el nombre de la persona 1: ")
    nombre_2 = input("Introduce el nombre de la persona 2: ")
    sueldo_1 = input(f"Introduce sueldo de {nombre_1}: ")
    sueldo_2 = input(f"Introduce sueldo de {nombre_2}: ")
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
       
            
def calcular_aportacion(sueldo_1, sueldo_2):
    sueldo_1=float(sueldo_1)
    sueldo_2=float(sueldo_2)
    total = sueldo_1 + sueldo_2
    tasa_1 = (sueldo_1 / total)*100
    tasa_2 = (sueldo_2 / total)*100
    return tasa_1,tasa_2

def cantidad_pagar(gastos,nombre_1,nombre_2,tasa_1, tasa_2):
    
    for clave, valor in gastos.items():
        tasa_valor_1 = (int(valor)* int(tasa_1))/100
        tasa_valor_2 = (int(valor)* int(tasa_2))/100
        print(f"{nombre_1}, tiene que pagar de {clave}: {tasa_valor_1}")
        print(f"{nombre_2}, tiene que pagar de {clave}: {tasa_valor_2}")
