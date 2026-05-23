from personagem import Personagem  

class Vilao(Personagem):
    
    def __init__(self):
        super().__init__(nome = "Vilgax", idade = 1000, vida = 500)
        
    
    def ataque(self, personagem):
        personagem.downgrade_vida()

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}' 