import json
#agregar

"""def agregarCliente(nombre:str,credito:int):
    with open("compras.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)  #.load carga la informacion del json
        cliente_nuevo= {
            "id": len(leerJason["clientes"])+ 1,
            "nombre": nombre,
            "credito": credito
        }

        leerJason["clientes"].append(cliente_nuevo)

    with open("compras.json", mode = "w") as escrituraJson:
        json.dump(leerJason, escrituraJson, indent= 4)
        print("cliente agregado correctamente")

nombreN = input("ingrese el nombre del cliente: ")
creditoN=int(input("ingrese el credito del cliente: "))

agregarCliente(credito=creditoN,nombre=nombreN)

def editarCliente(id:int):
    contador = 0
    with open("compras.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)  #.load carga la informacion del json
        for i in leerJason["clientes"]:
            if i["id"] == id:
                print("encontrado")
                break
            contador+= 1
        leerJason["clientes"][contador]["nombre"]=input("ingrese el nuevo nombre: ")
        leerJason["clientes"][contador]["credito"]=int(input("ingrese nuevo credito: "))
    with open("compras.json", mode = "w") as escrituraJson:
        json.dump(leerJason, escrituraJson, indent= 4)
        print("cliente editado correctamente")

editarCliente(int(input("ingrese una id: ")))"""



def eliminarCliente(id:int):
    with open("compras.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)  #.load carga la informacion del json
        print(leerJason["clientes"])
        id=int(input("ingrese una id: "))
        clientes = leerJason["clientes"]
        
        for i, cliente in enumerate(clientes):
            if cliente["id"] == id:
                clientes.pop(i) 
                print("cliente eliminado correctamente")
                
            else:#else en arreglo
                print("cliente no encontrado")
                break
        for idn, cliente in enumerate(clientes, start=1):
                    cliente["id"] = idn
                    print("la lista se actualizo con exito")
                    break
        

        
       

    with open("compras.json", mode = "w") as escrituraJson:
        json.dump(leerJason, escrituraJson, indent= 4)
        

#eliminarCliente(id)


             

"""def buscarCliente(id:int):
    with open("compras.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)  #.load carga la informacion del json
        for i in leerJason["clientes"]:
            
            if i["id"] == id:
                print("cliente encontrado")
                print(leerJason["clientes"][id-1])
            else:
                print("cliente no encontrado")
                break

            

               
buscarCliente(int(input("ingrese una id: ")))"""