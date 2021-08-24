class Cola_1:
    def __init__(self,tamanio):
        self.lista=[]
        self.size=tamanio
        self.top=0

    def push(self,dato):
        if self.top <self.size:
            self.lista = self.lista + [dato]
            self.top += 1
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[0]
            self.lista = self.lista[1:]
            self.top -= 1
            return top
        
    def show(self):
        for top in range(self.top):
            print("[{}]".format(self.lista[top]))
    
    def longitud(self):
        return self.top
        
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

# total = Pila_1(3)
# print(total.push(3))
# print(total.push(4))
# print(total.push(6))
# print(total.push(3))