import math
import pygame
import pygame_gui 
from personagem import Personagem 
from vilao import Vilao
from heroi import Heroi, Quatro_Bracos, Chama, Diamante 

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ben 10 - Ultimate Battle")
relogio = pygame.time.Clock()
gerenciador_ui = pygame_gui.UIManager((800,600), "tema.json")
botao_jogar = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 400), (200, 80)),
    text='JOGAR',
    manager=gerenciador_ui
) 
vilgax = Vilao()
ben = Heroi()
chama_salvo = Chama()
quatro_bracos_salvo = Quatro_Bracos()
diamante_salvo = Diamante()
oponente_atual = ben
alien_atual = "ben"
fonte_hud = pygame.font.SysFont("Arial", 24, bold=True)
botao_atacar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 520), (220, 50)), text='ATACAR', manager=gerenciador_ui, visible=False)
botao_transformar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 520), (220, 50)), text='TRANSFORMAR', manager=gerenciador_ui, visible=False)
botao_hab1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((90, 470), (290, 45)),
    text='',
    manager=gerenciador_ui,
    visible=False
)
botao_hab2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((420, 470), (290, 45)),
    text='',
    manager=gerenciador_ui,
    visible=False
)
botao_hab3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((90, 530), (290, 45)),
    text='',
    manager=gerenciador_ui,
    visible=False
)
botao_chama = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 480), (220, 40)), text='CHAMA', manager=gerenciador_ui, visible=False)
botao_quatro_bracos = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 480), (220, 40)), text='QUATRO BRAÇOS', manager=gerenciador_ui, visible=False)
botao_diamante = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 530), (220, 40)), text='DIAMANTE', manager=gerenciador_ui, visible=False)
botao_voltar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 530), (220, 40)), text='VOLTAR', manager=gerenciador_ui, visible=False)
img_menu = pygame.image.load("imagens/Capa_ben10.jpg")
img_menu = pygame.transform.scale(img_menu, (800, 600))
img_casa = pygame.image.load("imagens/Casa_ben10.webp")
img_casa = pygame.transform.scale(img_casa, (800, 600))
img_fundo_ui = pygame.image.load("imagens/fundo.jpg").convert()
img_fundo_ui = pygame.transform.scale(img_fundo_ui, (800, 150))
img_ben = pygame.image.load("imagens/ben.png")
img_ben = pygame.transform.scale(img_ben, (120, 150))
img_vilgax = pygame.image.load("imagens/vilgax_isolated_flipped.png")
img_vilgax = pygame.transform.scale(img_vilgax, (180, 220))
tempo_animacao = 0
tela_atual = "menu"
imagens_aliens = {
    "ben": pygame.image.load("imagens/ben.png"),
    "chama": pygame.image.load("imagens/heatblast.png"),
    "quatro_bracos": pygame.image.load("imagens/four_arms.png"),
    "diamante": pygame.image.load("imagens/diamondhead.png")
}
rodando = True 
while rodando:
    tempo_delta = relogio.tick(60) / 1000.0
    tempo_animacao += tempo_delta
    movimento_suave = math.sin(tempo_animacao * 4) * 5

    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            rodando = False
        
        gerenciador_ui.process_events(evento)

        if evento.type == pygame_gui.UI_BUTTON_PRESSED:
            print(f"RADAR: O jogo viu um clique no botão -> {evento.ui_element.text}") # ADICIONE ESTA LINHA
            if evento.ui_element == botao_jogar:
                tela_atual = "jogo"
                botao_jogar.hide()        
                botao_atacar.show()        
                botao_transformar.show()
            elif evento.ui_element == botao_atacar:
                if alien_atual == "ben" and ben.vida <= 1:
                    pass
                else: 
                    botao_atacar.hide()
                    botao_transformar.hide()
                    botao_voltar.show()
                    if alien_atual == "ben":
                        botao_hab1.set_text("Soco")
                        botao_hab1.show()
                    elif alien_atual == "chama":
                        botao_hab1.set_text("Bolas de Fogo")
                        botao_hab2.set_text("Supernova")
                        botao_hab3.set_text("Tornado Flamejante")
                        botao_hab1.show()
                        botao_hab2.show()
                        botao_hab3.show()
                    elif alien_atual == "quatro_bracos":
                        botao_hab1.set_text("Soco Quádruplo")
                        botao_hab2.set_text("Palmada Sônica")
                        botao_hab3.set_text("Arremesso de Objeto")
                        botao_hab1.show()
                        botao_hab2.show()
                        botao_hab3.show()
                    elif alien_atual == "diamante":
                        botao_hab1.set_text("Cristais Subterrâneos")
                        botao_hab2.set_text("Disparo de Diamantes")
                        botao_hab3.set_text("Construtos de Cristais")
                        botao_hab1.show()
                        botao_hab2.show()
                        botao_hab3.show()
            elif evento.ui_element in [botao_hab1, botao_hab2, botao_hab3]:
                if alien_atual == "ben":
                    if evento.ui_element == botao_hab1: 
                        oponente_atual.ataque(vilgax)
                        print(f"CLIQUE REGISTRADO! Vida do Vilgax no backend: {vilgax.vida}")
                elif alien_atual == "chama":
                    if evento.ui_element == botao_hab1: oponente_atual.bolas_de_fogo(vilgax) 
                    elif evento.ui_element == botao_hab2: oponente_atual.super_nova(vilgax) 
                    elif evento.ui_element == botao_hab3: oponente_atual.tornados_flamejantes(vilgax)
                elif alien_atual == "quatro_bracos":
                    if evento.ui_element == botao_hab1: oponente_atual.soco_normal(vilgax)
                    elif evento.ui_element == botao_hab2: oponente_atual.palmada_sonica(vilgax)
                    elif evento.ui_element == botao_hab3: oponente_atual.arremessar_objeto(vilgax)
                elif alien_atual == "diamante":
                    if evento.ui_element == botao_hab1: oponente_atual.cristais_subterraneos(vilgax)
                    elif evento.ui_element == botao_hab2: oponente_atual.disparo_de_diamantes(vilgax)
                    elif evento.ui_element == botao_hab3: oponente_atual.construtos_de_cristais()
                
                timer_dano_vilgax = 0.2
                print(f"Ataque realizado! Vida do Vilgax: {vilgax.vida}")
                
                if vilgax.vida <= 485 and "Quatro_Bracos" not in ben.aliens_desbloqueados:
                    ben.aliens_desbloqueados.append("Quatro_Bracos")
                    print("SISTEMA: Quatro Braços Desbloqueado!")
                if vilgax.vida <= 425 and "Chama" not in ben.aliens_desbloqueados:
                    ben.aliens_desbloqueados.append("Chama")
                    print("SISTEMA: Chama Desbloqueado!")
                if vilgax.vida <= 365 and "Diamante" not in ben.aliens_desbloqueados:
                    ben.aliens_desbloqueados.append("Diamante")
                    print("SISTEMA: Diamante Desbloqueado!")
                if vilgax.vida > 0:
                    vilgax.ataque(oponente_atual)
                    timer_dano_ben = 0.2
                    print(f"Vilgax revidou! Vida do Herói: {oponente_atual.vida}")
                
                botao_hab1.hide()
                botao_hab2.hide()
                botao_hab3.hide()
                botao_voltar.hide()
                botao_atacar.show()
                botao_transformar.show()
            
            elif evento.ui_element == botao_transformar:
                botao_atacar.hide()
                botao_transformar.hide()
                botao_voltar.show()
                
                if "Chama" in ben.aliens_desbloqueados:
                    botao_chama.show()
                if "Quatro_Bracos" in ben.aliens_desbloqueados:
                    botao_quatro_bracos.show()
                if "Diamante" in ben.aliens_desbloqueados:
                    botao_diamante.show()
            
            elif evento.ui_element == botao_voltar:
                botao_chama.hide()
                botao_quatro_bracos.hide()
                botao_diamante.hide()
                botao_voltar.hide()
                botao_hab1.hide()
                botao_hab2.hide()
                botao_hab3.hide()
                botao_atacar.show()
                botao_transformar.show()
            elif evento.ui_element == botao_chama:
                oponente_atual = chama_salvo
                alien_atual = "chama"
                print("Ben se transformou no Chama!")
                botao_chama.hide()
                botao_quatro_bracos.hide()
                botao_diamante.hide()
                botao_voltar.hide()
                botao_atacar.show()
                botao_transformar.show()
            elif evento.ui_element == botao_quatro_bracos:
                oponente_atual = quatro_bracos_salvo
                alien_atual = "quatro_bracos"
                print("Ben se transformou no Quatro Braços!")
                botao_chama.hide()
                botao_quatro_bracos.hide()
                botao_diamante.hide()
                botao_voltar.hide()
                botao_atacar.show()
                botao_transformar.show()
            elif evento.ui_element == botao_diamante:
                oponente_atual = diamante_salvo
                alien_atual = "diamante"
                print("Ben se transformou no Diamante!")
                botao_chama.hide()
                botao_quatro_bracos.hide()
                botao_diamante.hide()
                botao_voltar.hide()
                botao_atacar.show()
                botao_transformar.show()
            
    if tela_atual == "menu":
        tela.blit(img_menu, (0, 0))
   
    elif tela_atual == "jogo":
        tela.blit(img_casa, (0, 0))
        sprite_atual = imagens_aliens[alien_atual]
        tela.blit(sprite_atual, (150, 250 + movimento_suave))
        tela.blit(img_vilgax, (500, 200 - movimento_suave))
        tela.blit(img_fundo_ui, (0, 450))
        pygame.draw.rect(tela, (255, 255, 255), (0, 450, 800, 150), 3)
        vida_max_heroi = 100 if alien_atual == "ben" else 200
        texto_ben = fonte_hud.render(f"{oponente_atual.nome.upper()}: {max(0, oponente_atual.vida)}/{vida_max_heroi}", True, (255, 255, 255))
        tela.blit(texto_ben, (50, 20))
        largura_max_barra = 350 
        largura_verde_proporcional = max(0, int((oponente_atual.vida / vida_max_heroi) * largura_max_barra))
        pygame.draw.rect(tela, (0, 0, 0), (50, 50, largura_max_barra, 25))
        pygame.draw.rect(tela, (0, 255, 0), (50, 50, largura_verde_proporcional, 25))
        texto_vilgax = fonte_hud.render(f"VILGAX: {max(0, vilgax.vida)}/{vilgax.vida_maxima}", True, (255, 255, 255))
        tela.blit(texto_vilgax, (450, 20))
        largura_barra_vilgax = max(0, int((vilgax.vida / vilgax.vida_maxima) * 300))
        pygame.draw.rect(tela, (50, 50, 50), (450, 50, 300, 30))
        pygame.draw.rect(tela, (220, 20, 60), (450, 50, largura_barra_vilgax, 30))
        pygame.draw.rect(tela, (0, 0, 0), (450, 50, 300, 30), 4)
        
        if vilgax.vida <= 0:
            botao_hab1.hide()
            botao_hab2.hide()
            botao_hab3.hide()
            botao_voltar.hide()
            botao_atacar.hide()
            botao_transformar.hide()
            pelicula = pygame.Surface((800, 600))
            pelicula.set_alpha(180) 
            pelicula.fill((0, 0, 0))
            tela.blit(pelicula, (0, 0))
            largura_card = 500
            altura_card = 200
            pos_x_card = (800 - largura_card) // 2
            pos_y_card = (600 - altura_card) // 2
            pygame.draw.rect(tela, (20, 50, 20), (pos_x_card, pos_y_card, largura_card, altura_card), border_radius=15)
            pygame.draw.rect(tela, (50, 255, 50), (pos_x_card, pos_y_card, largura_card, altura_card), 4, border_radius=15)
            fonte_vitoria = pygame.font.SysFont("Arial", 45, bold=True)
            fonte_subtitulo = pygame.font.SysFont("Arial", 30)
            texto_titulo = fonte_vitoria.render("VILGAX DERROTADO!", True, (255, 255, 255))
            texto_sub = fonte_subtitulo.render("Você salvou o Universo!", True, (150, 255, 150))
            tela.blit(texto_titulo, (pos_x_card + (largura_card - texto_titulo.get_width()) // 2, pos_y_card + 50))
            tela.blit(texto_sub, (pos_x_card + (largura_card - texto_sub.get_width()) // 2, pos_y_card + 110))
        elif oponente_atual.vida <= 0 and alien_atual != "ben":
            botao_hab1.hide()
            botao_hab2.hide()
            botao_hab3.hide()
            botao_voltar.hide()
            botao_atacar.hide()
            botao_transformar.hide()
            pelicula = pygame.Surface((800, 600))
            pelicula.set_alpha(180)
            pelicula.fill((0, 0, 0))
            tela.blit(pelicula, (0, 0))
            largura_card = 600  
            altura_card = 200
            pos_x_card = (800 - largura_card) // 2
            pos_y_card = (600 - altura_card) // 2
            pygame.draw.rect(tela, (50, 20, 20), (pos_x_card, pos_y_card, largura_card, altura_card), border_radius=15)
            pygame.draw.rect(tela, (255, 50, 50), (pos_x_card, pos_y_card, largura_card, altura_card), 4, border_radius=15)
            fonte_derrota = pygame.font.SysFont("Arial", 45, bold=True)
            fonte_sub_derrota = pygame.font.SysFont("Arial", 30)
            texto_titulo_derrota = fonte_derrota.render("VOCÊ PERDEU!", True, (255, 255, 255))
            texto_sub_derrota = fonte_sub_derrota.render("Vilgax conseguiu o Omnitrix!", True, (255, 150, 150))
            tela.blit(texto_titulo_derrota, (pos_x_card + (largura_card - texto_titulo_derrota.get_width()) // 2, pos_y_card + 50))
            tela.blit(texto_sub_derrota, (pos_x_card + (largura_card - texto_sub_derrota.get_width()) // 2, pos_y_card + 110))
        elif alien_atual == "ben" and oponente_atual.vida <= 1:
            largura_card, altura_card = 650, 110
            x_card = (800 - largura_card) // 2
            y_card = (600 - altura_card) // 2 - 50
            pygame.draw.rect(tela, (20, 20, 20), (x_card, y_card, largura_card, altura_card))
            pygame.draw.rect(tela, (255, 0, 0), (x_card, y_card, largura_card, altura_card), 3)
            texto_linha1 = fonte_hud.render("!!! OMNITRIX: ALERTA CRÍTICO !!!", True, (255, 50, 50))
            texto_linha2 = fonte_hud.render("Forma humana incapacitada. TRANSFORME-SE!", True, (255, 255, 255))
            pos_x_linha1 = x_card + (largura_card - texto_linha1.get_width()) // 2
            pos_x_linha2 = x_card + (largura_card - texto_linha2.get_width()) // 2
            tela.blit(texto_linha1, (pos_x_linha1, y_card + 20))
            tela.blit(texto_linha2, (pos_x_linha2, y_card + 60))
    
    gerenciador_ui.update(tempo_delta)
    gerenciador_ui.draw_ui(tela)            

    pygame.display.update()

pygame.quit()    