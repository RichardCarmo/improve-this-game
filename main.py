from personagem import Personagem
from vilao import Vilao
from heroi import Heroi, Quatro_Bracos, Chama, Diamante

def main():
    ben = Heroi()
    oponente_atual = ben 
    vilgax = Vilao()
    
    print(ben)
    print(vilgax)

    print('\n' + "="*30)
    print("FIGHT!")
    print("="*30)
    print("VILGAX: Entregue o Omnitrix, criança, e eu prometo que sua morte será rápida!")
    print("BEN TENNYSON: Acho que o relógio não combina com alguém feio como você. TÁ NA HORA DE VIRAR HERÓI!")
    print("="*30 + '\n')

    while vilgax.vida > 0 and oponente_atual.vida > 0:
        print(f" Vida do Ben: {oponente_atual.vida}")
        print(f" Vida do Vilgax: {vilgax.vida}")
        if vilgax.vida <= 485 and "Quatro_Braços" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Quatro_Braços")
            print("QUATRO-BRAÇOS DESBLOQUEADO!")
        if vilgax.vida <= 425 and "Chama" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Chama")
            print("CHAMA DESBLOQUEADO!")
        if vilgax.vida <= 365 and "Diamante" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Diamante")
            print("DIAMANTE DESBLOQUEADO!")

        if oponente_atual.nome == "Ben Tennyson":
            if oponente_atual.vida == 1:
                oponente_atual = Quatro_Bracos()
                print("Omnitrix ativado devido ao código de emergência!")
                continue 
            print("1. Atacar")
            print("2. Acessar Omntrix" + '\n')
            escolha = int(input("Escolha sua opção: "))

            if escolha == 1:
                oponente_atual.ataque(vilgax)
                
            elif escolha == 2:
                if len(ben.aliens_desbloqueados) == 0:
                    print("Lista de DNA vazia. Colete alienígenas!") 
                    continue 
                else:
                    for indice, alien in enumerate(ben.aliens_desbloqueados):
                        print(f"{indice + 1} - {alien}")
                    escolha_alien = int(input("Digite o número do alien: "))
                    if 1 <= escolha_alien <= len(ben.aliens_desbloqueados):
                        nome_escolhido = ben.aliens_desbloqueados[escolha_alien - 1]
                        if nome_escolhido == "Quatro_Braços":
                            oponente_atual = Quatro_Bracos()
                            print("\nQUATRO-BRAÇOS!!")
                        elif nome_escolhido == "Chama":
                            oponente_atual = Chama()
                            print("\nCHAMA!!")
                        elif nome_escolhido == "Diamante":
                            oponente_atual = Diamante()
                            print("\nDIAMANTE!!")
                    else:
                        print("Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                        continue 
            else:
                print("Escolha uma opção válida.")
                continue
            
        elif oponente_atual.nome == "Quatro-Braços": 
            print("1. Socar")
            print("2. Palmada sônica")
            print("3. Arremessar objeto")
            print("4. Acessar Omnitrix")
            escolha_habilidade = int(input("Escolha sua habilidade: "))

            if escolha_habilidade == 1:
                oponente_atual.soco_normal(vilgax)
            elif escolha_habilidade == 2:
                oponente_atual.palmada_sonica(vilgax) 
            elif escolha_habilidade == 3:
                oponente_atual.arremessar_objeto(vilgax)
            elif escolha_habilidade == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien2 = int(input("Digite o número do alien: "))
                if 1 <= escolha_alien2 <= len(ben.aliens_desbloqueados):
                    nome_escolhido2 = ben.aliens_desbloqueados[escolha_alien2 - 1]
                    if nome_escolhido2 == "Quatro_Braços":
                        oponente_atual = Quatro_Bracos()
                        print("\nQUATRO-BRAÇOS!!")
                    elif nome_escolhido2 == "Chama":
                        oponente_atual = Chama()
                        print("\nCHAMA!!")
                    elif nome_escolhido2 == "Diamante":
                        oponente_atual = Diamante()
                        print("\nDIAMANTE!!")
                else:
                    print("Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue 
            else:
                print("Escolha uma opção válida.")
                continue
        
        elif oponente_atual.nome == "Chama":
            print("1. Bolas de fogo")
            print("2. Super nova")
            print("3. Tornados flamejantes")
            print("4. Acessar Omnitrix")
            escolha_habilidade2 = int(input("Escolha sua habilidade: "))

            if escolha_habilidade2 == 1:
                oponente_atual.bolas_de_fogo(vilgax)
            elif escolha_habilidade2 == 2: 
                oponente_atual.super_nova(vilgax)
            elif escolha_habilidade2 == 3:
                oponente_atual.tornados_flamejantes(vilgax)
            elif escolha_habilidade2 == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien3 = int(input("Digite o número do alien: "))
                if 1 <= escolha_alien3 <= len(ben.aliens_desbloqueados):
                    nome_escolhido3 = ben.aliens_desbloqueados[escolha_alien3 - 1]
                    if nome_escolhido3 == "Quatro_Braços":
                        oponente_atual = Quatro_Bracos()
                        print("\nQUATRO-BRAÇOS!!")
                    elif nome_escolhido3 == "Chama":
                        oponente_atual = Chama()
                        print("\nCHAMA!!")
                    elif nome_escolhido3 == "Diamante":
                        oponente_atual = Diamante()
                        print("\nDIAMANTE!!")
                else:
                    print("Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue  
            else:
                print("Escolha uma opção válida.")
                continue
        
        elif oponente_atual.nome == "Diamante":
            print("1. Disparos de cristais")
            print("2. Cristais subterrâneos")
            print("3. Construtos de cristais")
            print("4. Acessar Omnitrix")
            escolha_habilidade3 = int(input("Escolha sua habilidade: "))

            if escolha_habilidade3 == 1:
                oponente_atual.disparo_de_diamantes(vilgax)
            elif escolha_habilidade3 == 2:
                oponente_atual.cristais_subterraneos(vilgax)
            elif escolha_habilidade3 == 3:
                oponente_atual.construtos_de_cristais()
            elif escolha_habilidade3 == 4:
                for indice, alien in enumerate(ben.aliens_desbloqueados):
                    print(f"{indice + 1} - {alien}")
                escolha_alien4 = int(input("Digite o número do alien: "))
                if 1 <= escolha_alien4 <= len(ben.aliens_desbloqueados):
                    nome_escolhido4 = ben.aliens_desbloqueados[escolha_alien4 - 1]
                    if nome_escolhido4 == "Quatro_Braços":
                        oponente_atual = Quatro_Bracos()
                        print("\nQUATRO-BRAÇOS!!")
                    elif nome_escolhido4 == "Chama":
                        oponente_atual = Chama()
                        print("\nCHAMA!!")
                    elif nome_escolhido4 == "Diamante":
                        oponente_atual = Diamante()
                        print("\nDIAMANTE!!")
                else:
                    print("Escolha uma opção válida. O DNA desse alien ainda não foi escaneado.")
                    continue 
            else:
                print("Escolha uma opção válida.")
                continue
        if vilgax.vida > 0:
            print('\n' + "="*30)
            print("TURNO DO VILGAX!")
            print("="*30)
            vilgax.ataque(oponente_atual)
    
    if vilgax.vida <= 0:
        print("\n" + "VILGAX DERROTADO! Você salvou o Universo!")
    else:
        print("\n" + "Você perdeu! Vilgax conseguiu o Omnitrix!")
main()