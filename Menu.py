import os
from Pila import Pila_1
from Cola import Cola_1
from Lista import Lista_1

class Menu:
    def __init__(self, titulo,  opciones=[]):
         self.titulo = titulo
         self.opciones =opciones

    def menu(self):
         print(self.titulo)
         for opcion in self.opciones:
             print(opcion)
         opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
         print("")
         return opc

opc = ""
while opc != "4":
    os.system("cls")
    men =Menu("Menu Principal",["1). Pila", "2). Cola", "3). Lista", "4). Salir"])
    opc = men.menu()
    if opc == "1":
        os.system("cls")
        Ele = int(input("Ingrese el tamañó de la Pila: "))
        Total = Pila_1(Ele) 
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Pila",["1).Push","2).Pop", "3).Show", "4).Empty", "5).Longitud", "6).Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("PUSH")
                valor = int(input("Agregue el dato:"))
                Resp = Total.push(valor)
                if Resp == True:
                    print("El elemento esta agregado")
                else:
                    print("La pila esta llena.")
                input("Presione una tecla para continuar....")

            elif opc1 == "2":
                os.system("cls")
                print("POP")
                Resp = Total.pop()
                if Resp == None:
                    print("La pila esta vacia")
                else:
                    print("El elemento {} fue eliminado".format(Resp))
                input("Presione una tecla para continuar....")

            elif opc1 == "3":
                os.system("cls")
                print("SHOW")
                Total.show()
                input("Presione una tecla para continuar....")

            elif opc1 == "4":
                os.system("cls")
                print("EMPTY")
                Resp = Total.empty()
                if Resp == True:
                    print("La pila esta vacia")
                else:
                    print("La Pila tiene elementos")
                input("Presione una tecla para continuar....")

            elif opc1 == "5":
                os.system("cls")
                print("LONGITUD")
                Resp = Total.longitud()
                print("La longitud de la Pila es:",Resp)
                input("Presione una tecla para continuar....")
         
    if opc == "2":
        os.system("cls")
        Ele = int(input("Ingrese el tamañó de la Cola: "))
        Total = Cola_1(Ele) 
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Cola",["1).Push","2).Pop", "3).Show", "4).Empty", "5).Longitud", "6).Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("PUSH")
                valor = int(input("Agregue el dato:"))
                Resp = Total.push(valor)
                if Resp == True:
                    print("El elemento esta agregado")
                else:
                    print("La cola esta llena.")
                input("Presione una tecla para continuar....")

            elif opc1 == "2":
                os.system("cls")
                print("POP")
                Resp = Total.pop()
                if Resp == None:
                    print("La cola esta vacia")
                else:
                    print("El elemento {} fue eliminado".format(Resp))
                input("Presione una tecla para continuar....")

            elif opc1 == "3":
                os.system("cls")
                print("SHOW")
                Total.show()
                input("Presione una tecla para continuar....")

            elif opc1 == "4":
                os.system("cls")
                print("EMPTY")
                Resp = Total.empty()
                if Resp == True:
                    print("La cola esta vacia")
                else:
                    print("La cola tiene elementos")
                input("Presione una tecla para continuar....")

            elif opc1 == "5":
                os.system("cls")
                print("LONGITUD")
                Resp = Total.longitud()
                print("La longitud de la cola es:",Resp)
                input("Presionne una tecla para continuar....")

    if opc == "3":
        os.system("cls")
        Ele = int(input("Ingrese el tamañó de la Cola: "))
        Total = Lista_1(Ele) 
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Cola",["1).Push","2).Pop", "3).Show", "4).Empty", "5).Longitud", "6).Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("PUSH") 

    # if opc == "3":
    #     os.system("cls")
    #     valor = (input("Ingrese el tamañó de la Lista: "))
    #     Total = Lista_1(valor) 
    #     opc1 = ""
    #     while opc1 != "6":
    #         os.system("cls")
    #         men1 = Menu("Menu lista",["1).append","2).obtenerEliminado", "3).mostrar", "4).buscar", "5).insertar", "6).eliminar","7).obtener"])
    #         opc1 = men1.menu()
    #         if opc1 == "1":
    #             os.system("cls")
    #             print("append")
    #             valor = int(input("Agregue el dato:"))
    #             Resp = Total.append(valor)
    #             if Resp == True:
    #                 print("El dao esta ingresado")
    #             else:
    #                 print("La lista esta llena")
    #             input("Presionne una tecla para continuar....")

    #         elif opc1 == "2":
    #             os.system("cls")
    #             print("Obtener Eliminado")
    #             valor = int(input("Ingrese Posicion para eliminar el dato:"))
    #             Resp = Total.obtenerEliminado(valor)
    #             if Resp == None:
    #                 print("Posicion no valida...")
    #             else:
    #                 print("Elemento eliminado, lista queda:¨",Resp)
    #             input("Presionne una tecla para continuar....")

    elif opc == "4":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

    print("Lo esperamos pronto")
                
           