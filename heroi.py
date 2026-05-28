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
    
    def executar_turno(self, oponente, tratador, ben):
        while True:
            if self.vida == 1:
                print("⚠️ Omnitrix ativado devido ao código de emergência!")
                return Quatro_Bracos()  
            
            print("1. Atacar")
            print("2. Acessar Omntrix" + '\n')
            escolha = tratador.pedir_numero("Escolha sua opção: ")

            if escolha == 1:
                self.ataque(oponente)
                return self 
                
            elif escolha == 2:
                if len(ben.aliens_desbloqueados) == 0:
                    print("⚠️ Lista de DNA vazia. Colete alienígenas!") 
                    continue 
                else:
                    for indice, alien in enumerate(ben.aliens_desbloqueados):
                        print(f"{indice + 1} - {alien}")
                    escolha_alien = tratador.pedir_numero("Escolha sua opção: ")
                    if 1 <= escolha_alien <= len(ben.aliens_desbloqueados):
                        nome_escolhido = ben.aliens_desbloqueados[escolha_alien - 1]
                        if nome_escolhido == "Quatro_Braços":
                            print("\nQUATRO-BRAÇOS!!💪🔴")
                            return Quatro_Bracos()
                        elif nome_escolhido == "Chama":
                            print("\nCHAMA!!🔥☄️")
                            return Chama()
                        elif nome_escolhido == "Diamante":
                            print("\nDIAMANTE!!💎🧊")
                            return Diamante()
                    else:
                        print("⚠️ Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                        continue 
            else:
                print("❌ Escolha uma opção válida.")
                continue

    
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

    def executar_turno(self, oponente, tratador, ben):
        while True:
            print("1. Socar")
            print("2. Palmada sônica")
            print("3. Arremessar objeto")
            print("4. Acessar Omnitrix")
            escolha_habilidade = tratador.pedir_numero("Escolha sua opção: ") 

            if escolha_habilidade == 1:
                self.soco_normal(oponente)
                return self
            elif escolha_habilidade == 2:
                self.palmada_sonica(oponente)
                return self  
            elif escolha_habilidade == 3:
                self.arremessar_objeto(oponente)
                return self 
            elif escolha_habilidade == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien2 = tratador.pedir_numero("Escolha sua opção: ")
                if 1 <= escolha_alien2 <= len(ben.aliens_desbloqueados):
                    nome_escolhido2 = ben.aliens_desbloqueados[escolha_alien2 - 1]
                    if nome_escolhido2 == "Quatro_Braços":
                        print("\nQUATRO-BRAÇOS!!💪🔴")
                        return Quatro_Bracos()
                    elif nome_escolhido2 == "Chama":
                        print("\nCHAMA!!🔥☄️")
                        return Chama()
                    elif nome_escolhido2 == "Diamante":
                        print("\nDIAMANTE!!💎🧊")
                        return Diamante()
                else:
                    print("⚠️ Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue 
            else:
                print("❌ Escolha uma opção válida.")
                continue

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
    
    def executar_turno(self, oponente, tratador, ben):
        while True:
            print("1. Bolas de fogo")
            print("2. Super nova")
            print("3. Tornados flamejantes")
            print("4. Acessar Omnitrix")
            escolha_habilidade2 = tratador.pedir_numero("Escolha sua opção: ")

            if escolha_habilidade2 == 1:
                self.bolas_de_fogo(oponente)
                return self
            elif escolha_habilidade2 == 2: 
                self.super_nova(oponente)
                return self 
            elif escolha_habilidade2 == 3:
                self.tornados_flamejantes(oponente)
                return self 
            elif escolha_habilidade2 == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien3 = tratador.pedir_numero("Escolha sua opção: ")
                if 1 <= escolha_alien3 <= len(ben.aliens_desbloqueados):
                    nome_escolhido3 = ben.aliens_desbloqueados[escolha_alien3 - 1]
                    if nome_escolhido3 == "Quatro_Braços":
                        print("\nQUATRO-BRAÇOS!!💪🔴")
                        return Quatro_Bracos()
                    elif nome_escolhido3 == "Chama":
                        print("\nCHAMA!!🔥☄️")
                        return Chama()
                    elif nome_escolhido3 == "Diamante":
                        print("\nDIAMANTE!!💎🧊")
                        return Diamante()
                else:
                    print("⚠️ Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue  
            else:
                print("❌ Escolha uma opção válida.")
                continue

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

    def executar_turno(self, oponente, tratador, ben):
        while True:
            print("1. Disparos de cristais")
            print("2. Cristais subterrâneos")
            print("3. Construtos de cristais")
            print("4. Acessar Omnitrix")
            escolha_habilidade3 = tratador.pedir_numero("Escolha sua opção: ")

            if escolha_habilidade3 == 1:
                self.disparo_de_diamantes(oponente)
                return self 
            elif escolha_habilidade3 == 2:
                self.cristais_subterraneos(oponente)
                return self 
            elif escolha_habilidade3 == 3:
                self.construtos_de_cristais()
                return self 
            elif escolha_habilidade3 == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien4 = tratador.pedir_numero("Escolha sua opção: ")
                if 1 <= escolha_alien4 <= len(ben.aliens_desbloqueados):
                    nome_escolhido4 = ben.aliens_desbloqueados[escolha_alien4 - 1]
                    if nome_escolhido4 == "Quatro_Braços":
                        print("\nQUATRO-BRAÇOS!!💪🔴")
                        return Quatro_Bracos()
                    elif nome_escolhido4 == "Chama":
                        print("\nCHAMA!!🔥☄️")
                        return Chama()
                    elif nome_escolhido4 == "Diamante":
                        print("\nDIAMANTE!!💎🧊")
                        return Diamante()
                else:
                    print("⚠️ Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue 
            else:
                print("❌ Escolha uma opção válida.")
                continue