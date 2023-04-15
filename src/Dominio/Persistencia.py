class Persistencia:
    listaBodegas = []
    listaDistribuidores = []
    listaArticulos = []


    @classmethod
    def agregarBodega(self, objeto):
        self.listaBodegas.append(objeto)

    @classmethod
    def obtenerBodegas(self):
        return self.listaBodegas
    
    @classmethod
    def agregarDistribuidor(self, objeto):
        self.listaDistribuidores.append(objeto)

    @classmethod
    def obtenerDistribuidores(self):
        return self.listaDistribuidores
    
    @classmethod
    def agregarAtriculos(self, objeto):
        self.listaArticulos.append(objeto)

    @classmethod
    def obtenerArticulos(self):
        return self.listaArticulos
