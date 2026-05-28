class TratadorDeErros:
    def pedir_numero(self, texto_pergunta):
        while True:
            try:
                escolha = int(input(texto_pergunta))
                return escolha 
            except ValueError: 
                print("Digite apenas números!")