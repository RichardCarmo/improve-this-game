from personagem import Personagem
from vilao import Vilao
from heroi import Heroi, Quatro_Bracos, Chama, Diamante
from utils import TratadorDeErros

tratador = TratadorDeErros()

def main():
    ben = Heroi()
    oponente_atual = ben 
    vilgax = Vilao()
    
    print(ben)
    print(vilgax)

    print('\n' + "="*30)
    print("FIGHT!")
    print("="*30)
    print("VILGAX 🦑👹 : Entregue o Omnitrix, criança, e eu prometo que sua morte será rápida!")
    print("BEN TENNYSON 👦🏻⌚ : Acho que o relógio não combina com alguém feio como você. TÁ NA HORA DE VIRAR HERÓI!")
    print("="*30 + '\n')

    while vilgax.vida > 0 and oponente_atual.vida > 0:
        if vilgax.vida <= 485 and "Quatro_Braços" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Quatro_Braços")
            print("QUATRO-BRAÇOS DESBLOQUEADO!")
        if vilgax.vida <= 425 and "Chama" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Chama")
            print("CHAMA DESBLOQUEADO!")
        if vilgax.vida <= 365 and "Diamante" not in ben.aliens_desbloqueados:
            ben.aliens_desbloqueados.append("Diamante")
            print("DIAMANTE DESBLOQUEADO!")

        print("-" * 30)
        print(f"---- Turno de: {oponente_atual.nome} ----")
        print(f"Sua vida: {oponente_atual.vida}")
        print(f"Vida do Vilgax🦑👹 : {vilgax.vida}")
        print("-" * 30)
        oponente_atual = oponente_atual.executar_turno(vilgax, tratador, ben)
        
        if vilgax.vida <=0:
            break

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