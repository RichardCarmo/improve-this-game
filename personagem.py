class Personagem:
    
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def downgrade_vida(self, dano=10):
        self.vida -= dano 
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado, sua vida ficou {self.vida}.")

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'