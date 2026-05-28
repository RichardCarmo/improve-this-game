# ⌚ Ben 10: Ultimate Terminal Battle

Um jogo de RPG por turnos totalmente jogável pelo terminal, construído em Python. Enfrente o temível Vilgax, mude de forma usando o Omnitrix e salve o universo!

---

## 🧬 1. Sobre a Refatoração com POO
Este projeto foi evoluído de um modelo procedural estruturado em blocos condicionais aninhados (`if/elif/else`) para o paradigma de **Programação Orientada a Objetos (POO)**. 

A arquitetura antiga (conhecida como *Spaghetti Code*) centralizava todas as decisões de batalha e menus dentro do arquivo principal. Com a refatoração, o projeto passou a utilizar conceitos sólidos de design de software:
* **Encapsulamento:** Cada entidade (Ben, Vilgax e os Alienígenas) gerencia seu próprio estado de vida, sistema de danos e lógica interna de menu.
* **Polimorfismo:** O loop de jogo no `main.py` foi drasticamente reduzido. O arquivo principal agora atua apenas como o juiz da arena, invocando o método `.executar_turno()` de forma dinâmica, sem precisar saber qual herói ou alienígena está ativo naquele exato momento.
* **Herança:** Os alienígenas e o herói base herdam propriedades e comportamentos comuns, evitando a repetição de código (Princípio D.R.Y. - *Don't Repeat Yourself*).

---

## 👽 2. Personagens Jogáveis

Aqui estão os guerreiros disponíveis para a batalha pelos quais você pode alternar livremente usando o DNA do relógio:

* **👦🏻 Ben Tennyson:** A forma humana inicial. Embora não possua superpoderes físicos, tem acesso total ao Omnitrix e conta com um protocolo de emergência secreto caso sua vida chegue ao limite crítico.
* **💪🔴 Quatro-Braços:** O titã de força bruta da raça Tetramand. Especialista em combate corpo a corpo, focado em causar danos massivos e esmagar as defesas do oponente.
* **🔥 Chama:** Um ser feito de puro fogo vivo (Pyronita). Seus ataques utilizam manipulação térmica, esferas ardentes e ondas de calor devastadoras.
* **💎 Diamante:** Composto por cristais ultra-resistentes (Petrosapien). Equilibra perfeitamente ataque e defesa, sendo capaz de erguer barreiras de cristal que bloqueiam totalmente o próximo ataque inimigo.

### 🦑👹 O Nêmesis: Vilgax
O conquistador de mundos está obstinado a arrancar o Omnitrix do seu pulso. Ele possui uma quantidade massiva de pontos de vida e ataques implacáveis que testarão a sua estratégia a cada turno.

---

## 📁 3. Organização dos Arquivos

O projeto está estruturado de forma modular para facilitar a manutenção e a adição de novos conteúdos:

```text
├── main.py          # O coração do jogo. Controla o loop principal, turnos e condições de vitória/derrota.
├── personagem.py    # Classe base mãe contendo os atributos e métodos compartilhados por todas as entidades.
├── heroi.py         # Contém a classe principal do Ben Tennyson e todas as subclasses dos Alienígenas.
├── vilao.py         # Contém a inteligência e os comportamentos de ataque do Vilgax.
└── utils.py         # Ferramentas auxiliares, como o tratador de entradas numéricas e a renderização gráfica da barra de vida.

## 🚀 4. Como Executar o Jogo

Para iniciar sua jornada e rodar o jogo na sua máquina local, você só precisará do **Python 3** instalado. Siga o passo a passo:

* **Download dos Arquivos:** Baixe o código fonte ou faça um `git clone` deste repositório para uma pasta no seu computador.
* **Abertura do Terminal:** Navegue até a pasta do projeto e abra o seu terminal exatamente nesse local.
* **Comando de Execução:** Com o terminal aberto na pasta raiz do jogo, digite o seguinte comando e aperte Enter:

```bash
python main.py



