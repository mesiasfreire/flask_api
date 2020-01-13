class Tarefa():
    def __init(self, titulo ,descricao , data_expiracao):
        self.__titulo = titulo
        self.descricao = descricao
        self.data_expiracao = data_expiracao

        @property
        def titulo(self):
            return self.__titulo

        @titulo.setter
        def titulo(self, titulo):
            self__titulo = titulo

        @property
        def descricao(self):
            return self.__descricao

        @descricao.setter
        def descricao(self, descricao):
            self__descricao = descricao

        @property
        def data_expiracao(self):
            return self.__data_expiracao

        @descricao.setter
        def data_expiracao(self, data_expiracao):
            self__data_expiracao = data_expiracao