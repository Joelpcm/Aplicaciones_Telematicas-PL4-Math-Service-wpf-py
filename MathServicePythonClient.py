from suds.client import Client  

# URL del WSDL que describe el servicio
wsdl_url = 'http://localhost:8733/Design_Time_Addresses/MathService/Math/?wsdl'

# Crear cliente de Zeep para interactuar con el servicio
client = Client(wsdl_url)

#print (client)

while(True):
    print("Introduzca: \n - 1) para saber si un número es primo\n - 2) para sumar tuplas\n - exit) para salir")

    request = input()

    if (request == "1"):

        print("Ingrese un numero entero para saber si es primo o no")

        valor = int(input())

        result = client.service.Prime(valor)

        # Mostrar el resultado
        if result:

            print(f"El numero {valor} es primo")
        else:

            print(f"El numero {valor} no es primo")

        print()

    elif (request == "2"):

        print("Ingrese tuplas separadas por comas para sumarlas:")

        txt_datos = input()  # Tomar la entrada de la tupla

        data = txt_datos.split(',')
        #print(data)
        for i in range(len(data)):
            data[i] = float(data[i])
        #print(data)

        # Crear la estructura de la tupla que sera enviada
        tuple_obj = client.factory.create('ns0:Tuple')  # ns0 corresponde al espacio de nombres de Tuple en el WSDL

        array_of_double = client.factory.create('ns2:ArrayOfdouble') # ns2 corresponde al espacio de nombres de ArrayOfdouble en el WSDL  (Si metes float normal no funciona)
        array_of_double.double = data  

        # Asignar valores a la tupla
        tuple_obj.Name = ''  
        tuple_obj.Data = array_of_double

        try:
            resultado = client.service.SumTuple(tuple_obj)  
        
        except Exception as ex:
            print(f"Error: {ex}")
            
        # Mostrar el resultado
        print(f"Suma: {resultado['Data'][0]}, Nombre: {resultado['Name']}")
        print()

    elif (request == "exit"):
        print("Killing the program...")
        break
    else:
        print("Opcion no válida")
        print()

