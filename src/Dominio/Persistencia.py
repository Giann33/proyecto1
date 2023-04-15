class Persistencia:
    listaBodegas = []
    listaDistribuidores = []

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
