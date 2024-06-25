import json

def  agregar_cliente(credito:int,nombre:str):
    
    with open("compras.json", mode = "r") as lecturaJson:
        leerjson = json.load(lecturajson)  
        cliente_nuevo= {
            "id": len(leerjson["clientes"])+ 1,
            "nombre": nombre,
            "credito": credito
        }

        leerjson["clientes"].append(cliente_nuevo)

        with open("compras.json", mode = "w") as escrituraJson:
            json.dump(leerjson, escrituraJson, indent= 4)
            print("cliente agregado correctamente")
        
newnombre = input("Ingrese un nombre nuevo :")
newcredito = int(input("ingrese un nuevo credito :"))
agregar_cliente(credito=newnombre,nombre=newnombre)
    
    
    
    
    