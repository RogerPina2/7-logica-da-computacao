class Erros():

    def __init__(self):
        return

    def entrada_nao_aceita(self):
        err = 'Cadeia de soma não aceita'
        raise ValueError(err)

    def operador_no_final(self):
        err = 'Operadores não são aceitos no final da cadeia'
        raise ValueError(err)                    

    def sequencia_de_operadores(self):
        err = 'Sequência de dois operadores não é aceito'
        raise ValueError(err)    