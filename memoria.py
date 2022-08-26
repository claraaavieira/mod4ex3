class getset:
    def __int__(self):
        self._id = 0

    @property
    def id(self):
        print("Sua memória: ")
        return self._id

    @id.setter
    def id(self, i):
        if  (i < 36):
            raise ValueError('Você não tem memória suficiente')
        print('Iniciando instalação')
        self._id = i


pt = getset()

pt.id = 256

print(pt.id)