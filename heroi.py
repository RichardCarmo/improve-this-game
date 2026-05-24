from personagem import Personagem

class Heroi(Personagem):
    def __init__(self):
        super().__init__(nome = "Ben Tennyson", idade = 10, vida = 100)
        self.aliens_desbloqueados = []

    
    def downgrade_vida(self):
        self.vida -= 10 
        if self.vida <= 0:
            self. vida = 1
            if len(self.aliens_desbloqueados) == 0:
                self.aliens_desbloqueados.append("Quatro_Braços") 
                print(f"Ativando alienígena! {self.aliens_desbloqueados[0]}")
            else:
                print("Ativando alienígena!")

    
    def ataque(self, personagem):
        personagem.vida -= 5
    
    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'

class Quatro_Bracos(Heroi):
    def __init__(self):
        super().__init__()
        self.nome = "Quatro-Braços"
        self.vida = 200
    
    def downgrade_vida(self):
        self.vida -= 10
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado.")
    
    def soco_normal(self, personagem):
        personagem.vida -= 20
    def palmada_sonica(self, personagem):
        personagem.vida -= 30
    def arremessar_objeto(self, personagem):
        personagem.vida -= 10

class Chama(Heroi):
    def __init__(self):
        super().__init__()
        self.nome = "Chama" 
        self.vida = 200
        

    def downgrade_vida(self):
        self.vida -= 10
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado.")

    def bolas_de_fogo(self, personagem):
        personagem.vida -= 10
    def super_nova(self, personagem):
        personagem.vida -= 40
    def tornados_flamejantes(self, personagem):
        personagem.vida -= 20

class Diamante(Heroi):
    def __init__(self):
        super().__init__()
        self.nome = "Diamante"
        self.vida = 200
        self.barreira_ativa = False
    
    def downgrade_vida(self):
        if self.barreira_ativa == True:
            self.vida -= 0 
            print("Barreira de cristais ativa!")
            self.barreira_ativa = False
        else:
            self.vida -= 10
        if self.vida <= 0:
            self.vida = 0 
            print(f"{self.nome} foi derrotado.")
                
    
    def disparo_de_diamantes(self, personagem):
        personagem.vida -= 10
    def cristais_subterraneos(self, personagem):
        personagem.vida -= 30
    def construtos_de_cristais(self):
        self.barreira_ativa = True  