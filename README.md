# 👽 Ben 10: Ultimate Battle

Um jogo de RPG por turnos construído em Python. O que antes era jogável apenas pelo terminal, agora possui uma interface gráfica completa e imersiva! Enfrente o temível Vilgax, mude de forma usando o Omnitrix e salve o universo!

---

## 🧠 1. Da Refatoração POO à Interface Gráfica
Este projeto evoluiu de um modelo procedural estruturado em blocos condicionais aninhados (`if/elif/else`) para o paradigma de **Programação Orientada a Objetos (POO)**. Recentemente, o jogo recebeu sua maior atualização, migrando do terminal para uma interface visual interativa com Pygame.

* **Encapsulamento:** Cada entidade (Ben, Vilgax e os Alienígenas) gerencia seu próprio estado de vida, sistema de danos e lógica interna de menu.
* **Polimorfismo:** O loop de jogo no novo `jogo_grafico.py` foi drasticamente reduzido. O arquivo principal agora atua apenas como o juiz da arena, invocando o método `.executar_turno()` de forma dinâmica, sem precisar saber qual herói ou alienígena está ativo naquele exato momento.
* **Herança:** Os alienígenas e o herói base herdam propriedades e comportamentos comuns, evitando a repetição de código (Princípio D.R.Y. - *Don't Repeat Yourself*).
* **Interface Gráfica (Novo):** Implementação da biblioteca `pygame` e `pygame_gui` para renderização de sprites, gerenciamento de cliques em botões interativos de habilidades e barras de vida dinâmicas.

---

## 👽 2. Personagens Jogáveis

Aqui estão os guerreiros disponíveis para a batalha pelos quais você pode alternar livremente usando o DNA do relógio:

* **👦🏻 Ben Tennyson:** A forma humana inicial. Embora não possua superpoderes físicos, tem acesso total ao Omnitrix e conta com um protocolo de emergência secreto caso sua vida chegue ao limite crítico.
* **💪🏼 Quatro-Braços:** O titã de força bruta da raça Tetramand. Especialista em combate corpo a corpo, focado em causar danos massivos e esmagar as defesas do oponente.
* **🔥 Chama:** Um ser feito de puro fogo vivo (Pyronita). Seus ataques utilizam manipulação térmica, esferas ardentes e ondas de calor devastadoras.
* **💎 Diamante:** Composto por cristais ultra-resistentes (Petrosapien). Equilibra perfeitamente ataque e defesa, sendo capaz de erguer barreiras de cristal que bloqueiam totalmente o próximo ataque inimigo.

### 🦑 😈 O Nêmesis: Vilgax
O conquistador de mundos está obstinado a arrancar o Omnitrix do seu pulso. Ele possui uma quantidade massiva de pontos de vida e ataques implacáveis que testarão a sua estratégia a cada turno.

---

## 📁 3. Organização dos Arquivos

O projeto está estruturado de forma modular para facilitar a manutenção e a adição de novos conteúdos:

```text
├── jogo_grafico.py  # Novo coração do jogo. Controla a janela visual, botões de UI, turnos e condições de vitória/derrota.
├── personagem.py    # Classe base mãe contendo os atributos e métodos compartilhados por todas as entidades.
├── heroi.py         # Contém a classe principal do Ben Tennyson e todas as subclasses dos Alienígenas.
├── vilao.py         # Contém a inteligência e os comportamentos de ataque do Vilgax.
├── tema.json        # Arquivo de configuração de estilo visual para os botões do Pygame GUI.
└── .gitignore       # Configuração para evitar o envio de arquivos temporários de compilação (__pycache__) para o repositório.