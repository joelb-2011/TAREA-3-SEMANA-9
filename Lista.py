class Lista_1:
    def _init_(self,tamanio):
        self.lista = []
        self.longuitud = 0
        self.size = tamanio

    def append(self,dato):
        if self.longuitud < self.size:
            self.lista += [dato]
            self.longuitud += 1
            return True
        else:
            return False
    
    def obtenerEliminado(self,pos):
        self.mostrar()
        if pos < 0 or pos >= self.longuitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longuitud):
                listaAux += [self.lista[indice]]
            self.longuitud -=1
            self.lista = listaAux

            return eliminado,self.lista

    def mostrar(self):
        print("{:3}{:9} {}".format("","Lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:4}".format(ele,pos))
            
    def buscar(self, valor):
        if valor in self.lista:
            print("si esta en lista  ", valor)
            return True
        else:
            print("no esta en lista ", valor)
            return False
    
    def insertar(self, valor):
        if (self.buscar(valor)):
            print("lo siento , ese dato ya esta")
        else:
            self.lista.append(valor)
            
    def eliminarLista(self, valor):
        print("Lista original :", self.lista)
        for item in self.lista:
            if (item == valor):
                self.lista.remove(valor) 
        print(self.lista)                        
    
    def obtener(self, pos):
        if pos <0 or pos>=self.longuitud:
            return None
        else:
            return self.lista[pos]