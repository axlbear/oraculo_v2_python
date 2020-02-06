# IMPORTS
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as ms
import os
import random

# FUNCTIONS
def creditos():
    ms.showinfo('Oráculo II - RPG SOLO', 'ORÁCULO II - RPG SOLO - Gerador Aleatório de Campanhas\nIdealizador do sistema: Tiago Alves de Morais - tdetudo3785@gmail.com\nApp desenvolvido por: Alex Marzani Motta - alexmarzanimotta@hotmail.com\nTodos os créditos deste projeto vão ao seu Idealizador,\ncabendo a mim apenas desenvolver o aplicativo.')

def gerarAventura():
    randomUm = ['Derrotar', 'Destruir', 'Descobrir', 'Escoltar', 'Impedir', 'Proteger', 'Viajar até', 'Transportar', 'Avançar', 'Escapar', 'Explorar', 'Certificar', 'Recuperar', 'Libertar', 'Salvar', 'Resgatar', 'Atrair', 'Desbaratar', 'Executar', 'Seguir']
    randomDois = ['Cidade', 'Vilã(o)', 'Princesa', 'Principe', 'Pessoa', 'Amigo', 'Grupo', 'Fortaleza', 'Monstro', 'Maldição', 'Culto', 'Cidade Perdida', 'Povoado', 'Família', 'Reino', 'Raça', 'Rei', 'Rainha', 'Monstro', 'Animal Mágico', 'Espírito']
    randomTres = ['Esquecido(a)', 'Construído', 'Formado', 'Criado(a)', 'Atacado(a)', 'Morto(a)', 'Aprisionado(a)', 'Enfeiticiado(a)', 'Amaldiçoado(a)', 'Preso(a)', 'Raptado(a)', 'Destruído(a)', 'Feito', 'Eleito(a)', 'Escondido(a)', 'Escrita', 'Definhado', 'Confinado(a)', 'Levado(a)', 'Exilado(a)']
    randomQuatro = ['No fundo do mar', 'Escondido(a) em uma masmorra', 'Em um reino secreto', 'Em um reino mágico', 'Em uma floresta', 'Em uma mina abandonada', 'Em um castelo', 'Em um covíl', 'Em uma torre', 'Em um lugar distante', 'Nas núvens', 'No subterrâneo', 'Em uma ilha', 'Esquecido(a)', 'Em outro plano', 'Em meio a monstros', 'Derrotado(a)', 'Esgotado(a)', 'Sumido(a)']
    opcaoUm.set(random.choice(randomUm))
    opcaoDois.set(random.choice(randomDois))
    opcaoTres.set(random.choice(randomTres))
    opcaoQuatro.set(random.choice(randomQuatro))

def gerarClima():
    randomClima = ['Bom', 'Ruim', 'Péssimo']
    randomHorario = ['Dia', 'Tarde', 'Noite', 'Madrugada']
    opcaoClima.set(random.choice(randomClima))
    opcaoHorario.set(random.choice(randomHorario))

def gerarResposta():
    randomResposta = ['Não', 'Sim', 'Não + Vantagem', 'Sim + Vantagem', 'Não + Desvantagem', 'Sim + Desvantagem', 'Não + Evento', 'Sim + Evento', 'Não', 'Sim']
    opcaoResposta.set(random.choice(randomResposta))

def gerarEvento():
    randomEvento = ['NPC', 'Acidente', 'Vantagem', 'Desvantagem', 'Obstáculo', 'Combate', 'Perdido?']
    opcaoEvento.set(random.choice(randomEvento))

def gerarNPC():
    randomInfluencia = ['Não', 'Não', 'Não', 'Não', 'Não', 'Sim']
    randomRaca = ['Humano', 'Orc', 'Anão', 'Elfo', 'Gnomo', 'Halfling', 'Meio-Orc', 'Meio-Elfo', 'Raça Específica', 'Raça Mecânica (Se Possível)']
    randomGenero = ['Homem', 'Mulher', 'Andrógino', 'Difícil de Identificar']
    randomAparencia = ['Nobre', 'Plebeu', 'Mendigo', 'Comerciante', 'Desleixado', 'Militar', 'Suspeito', 'Boa parte do corpo coberta']
    randomPersonalidade = ['Carismático', 'Introvertido', 'Sério', 'Corajoso', 'Covarde', 'Ganancioso', 'Generoso', 'Educado', 'Grosso', 'Beberrão', 'Religioso', 'Apostador', 'Brigão', 'Simpático', 'Mentiroso', 'Niilista', 'Culto', 'Curioso', 'Desafiador', 'Desanimado', 'Desesperado', 'Desmotivado', 'Determinado', 'Diplomático', 'Distraído']
    randomAlinhamento = ['Leal/Bom', 'Leal/Neutro', 'Leal/Mau', 'Neutro/Bom', 'Verdadeiro Neutro', 'Neutro/Mau', 'Caótico/Bom', 'Caótico/Neutro', 'Caótico/Mau']
    randomCaracteristica = ['Muitas Cicatrizes', 'Amuleto Mágico', 'Símbolo de Família Nobre', 'Muito Forte', 'Doente', 'Amaldiçoado', 'Arma Mágica', 'Arma furtiva', 'Tatuagem de Tribo', 'Tatuagem de Gangue', 'Tatuagens', 'Ferida recente', 'Mochila de Comerciante', 'Doente']

    opcaoInfluencia.set(random.choice(randomInfluencia))
    opcaoRaca.set(random.choice(randomRaca))
    opcaoGenero.set(random.choice(randomGenero))
    opcaoAparencia.set(random.choice(randomAparencia))
    opcaoPersonalidade.set(random.choice(randomPersonalidade))
    opcaoAlinhamento.set(random.choice(randomAlinhamento))
    opcaoCaracteristica.set(random.choice(randomCaracteristica))

def gerarEvento2():
    randomEvento1 = ['Identidade Enganosa', 'Álguem que você achou que estava morto, não está', 'Alguém que você achou que estava vivo, está morto', 'Alguém inesperado quer ferir/roubar você', 'Alguém com que você se importa está em perigo']
    randomEvento2 = ['As autoridade se envolveram ou fazem vista grossa (O que for pior)', 'Distração de violência aleatória', 'Sequestrado (Você ou alguém próximo)', 'Reforços chegam em momentos oportunos/inoportunos', 'É um disfarce', 'É uma armadilha']
    randomEvento3 = ['Algo inesperado acontece', 'Novo adorador', 'Forçado inesperadamente em uma nova responsabilidade', 'Uma velha responsabilidade desaparece (ou muda)', 'Seu objetivo imediato gira em sua cabeça', 'Um suporte que você precisa para o sucesso é tirado']
    randomEvento4 = ['Alguém que você pensou que estava ajudando você, tem algo a mais em mente', 'Uma pessoa que você pensou que conhecia acabou se mostrando diferente', 'Uma nova pessoa inesperadamente aparece para complicar', 'Uma pessoa inesperadamente aparece para ajudar', 'Uma pessoa em quem você confia vai te trair', 'Algo explode (Figurativa ou Literal)']
    randomEvento5 = ['É uma farsa', 'É uma mentira', 'A natureza de algo que você deu como é certo esta errada', 'Uma nova trama surge', 'Um superior se torna seu subordinado (ou oposto)', 'Alguém inesperadamente lhe dá um item misterioso']
    randomEvento6 = ['Um suporte que você precisa para sucesso é tirado', 'Um novo obstáculo inesperado fica no seu caminho', 'Você acorda/Chega em um lugar inesperado', 'Um amigo se torna um inimigo', 'Um inimigo se torna um aliado']

    eventoUm.set(random.choice(randomEvento1))
    eventoDois.set(random.choice(randomEvento2))
    eventoTres.set(random.choice(randomEvento3))
    eventoQuatro.set(random.choice(randomEvento4))
    eventoCinco.set(random.choice(randomEvento5))
    eventoSeis.set(random.choice(randomEvento6))

def gerarTerreno():
    randomTamanho = ['Pequeno', 'Médio', 'Grande', 'Enorme', 'Pequeno', 'Médio']
    randomTerreno = ['Casa', 'Cidade', 'Vila', 'Floresta', 'Torre', 'Pântano', 'Montanhas', 'Desfiladeiros', 'Deserto', 'Mina', 'Caverna Natural', 'Vale', 'Guilda', 'Torre de Magos', 'Cidade', 'Acesso Subterrâneo', 'Forte', 'Castelo', 'Vila', 'Cidade']
    opcaoTerreno.set(random.choice(randomTerreno))
    setTamanho = random.choice(randomTamanho)
    opcaoTamanho.set(setTamanho)

    if setTamanho == 'Pequeno':
        opcaoSalas.set(random.choice(range(1, 5)))
        opcaoAndares.set(random.choice(range(1, 3)))
        opcaoSubterraneos.set(random.choice(range(1, 3)))

    elif setTamanho == 'Médio':
        opcaoSalas.set(random.choice(range(1, 7)))
        opcaoAndares.set(random.choice(range(1, 3)))
        opcaoSubterraneos.set(random.choice(range(1, 3)))

    elif setTamanho == 'Grande':
        opcaoSalas.set(random.choice(range(1, 7)))
        opcaoAndares.set(random.choice(range(1, 4)))
        opcaoSubterraneos.set(random.choice(range(1, 3)))
    
    elif setTamanho == 'Enorme':
        opcaoSalas.set(random.choice(range(1, 11)))
        opcaoAndares.set(random.choice(range(1, 6)))
        opcaoSubterraneos.set(random.choice(range(1, 5)))

def gerarVilajo():
    randomAspecto = ['Velha', 'Antiga', 'Destruída', 'Reconstruída', 'Pobre', 'Rica', 'Abandonada', 'Outras Raças', 'Refém', 'Tribal', 'Portuária', 'Baseada em Comércio', 'Baseada em Religião']
    randomSociedade = ['Monarquica', 'Ditatorial', 'Democrática', 'Liderada por Senhor da Guerra', 'Anarquica', 'Coletivista', 'Sem Organização']
    randomConhecida = ['População rude', 'População agradável', 'Centro Comercial', 'Cidade Modelo', 'Capital', 'Excelente Culinária', 'Magia', 'Ignorância', 'Atrito Racial/Religioso', 'Fé Fervorosa', 'Muito Explorada', 'Mercado de Escravos']
    randomSituaçãoAtual = ['Pessoa influente está morta', 'Guerra de gangues', 'Fome', 'Feiticeiros', 'Início de Guerra Civil', 'Lojistas Quebrando', 'Inflação', 'Medo da População', 'Escassez', 'Riqueza', 'Paz depois de anos de guerra', 'Monstros/Mercenários atacando constantemente', 'Fonte principal de água está envenenada', 'Rituais Norturnos suspeitos']
    randomTaverna2 = ['Calma', 'Cheia', 'Badalada', 'Promíscua', 'Nobre', 'Barulhenta', 'Perigosa', 'Vazia', 'Comum']
    randomTaverna= ['de Luxo', 'Caíndo aos pedaços', 'Palco de apresentações', 'Mal-vista', 'Prostíbulo', 'De uma família', 'Reformada', 'Símbolos tribais/outros Deuses', 'Antro de Mercenários/Ladrões']
    randomLojaItens = ['Velha/Antiquada', 'Itens mágicos', 'Itens caros', 'Itens Raros', 'Falídos', 'Ambulantes', 'Mercadores Itinerantes']
    randomExercito = ['Não tem', 'Fraco', 'Abatido', 'Numeroso', 'Famoso', 'Bem armado', 'Pouco na Região', 'Corruptos', 'Honrados']
    randomMercado = ['de Ladrões', 'de Mendigos', 'Itens Falsos', 'Itens Amaldiçoados', 'Itens Raros e Caros', 'Itens Usados', 'de Escravos', 'Influente', 'Muito Vasto', 'Bem Frequentado', 'Rota de Caravanas']
    randomTorreQuartel = ['Não tem', 'de Vigia', 'Abandonada(o)', 'Caindo aos Pedaços', 'Resistente e Influente', 'Reconstruindo', 'Sendo Construída(o)', 'Corruptos']
    randomGuilda = ['de Ladrões', 'de Magos', 'de Mercenários', 'Não tem']
    randomTemplo = ['Enorme', 'Manda na cidade', 'Corrupta', 'Deus Pagões', 'Antro de fanáticos', 'Caindo aos pedaços', 'Sendo Criada', 'Possui um Avatar', 'Deus específico', 'Não tem']
    randomCastelo = ['Não tem', 'Enorme', 'de Luxo', 'Difícil o acesso de quem não é Nobre', 'Apenas Convidados', 'Apenas Heróis', 'Ninguém entra', 'Abandonado', 'Boa/Má Fama', 'Portões abertos']

    opcaoAspecto.set(random.choice(randomAspecto))
    opcaoSociedade.set(random.choice(randomSociedade))
    opcaoConhecida.set(random.choice(randomConhecida))
    opcaoSituacaoAtual.set(random.choice(randomSituaçãoAtual))
    opcaoTaverna.set(random.choice(randomTaverna))
    opcaoTaverna2.set(random.choice(randomTaverna2))
    opcaoLojaItens.set(random.choice(randomLojaItens))
    opcaoExercito.set(random.choice(randomExercito))
    opcaoMercado.set(random.choice(randomMercado))
    opcaoTorreQuartel.set(random.choice(randomTorreQuartel))
    opcaoGuilda.set(random.choice(randomGuilda))
    opcaoTemplo.set(random.choice(randomTemplo))
    opcaoCastelo.set(random.choice(randomCastelo))

def gerarVilao():
    randomTipo = ['Um único Vilão', 'Uma Criatura Mística', 'Um Monstro Específico', 'Um grupo de indivíduos', 'Um fenômeno', 'Entidade', 'Avatar de um Deus', 'Semi-Deus', 'Mago Poderoso', 'Um Lich', 'Guerreiro Poderoso', 'Uma Maldição']
    randomOrigem = ['Mundo do Crime', 'Riqueza', 'Sobrenatural', 'Acidente', 'Desconhecida', 'Inata', 'do Passado', 'Patriotismo', 'de um Erro', 'da Miséria', 'Feitiço']
    randomObjetivo = ['Conquista', 'Fortuna', 'Sobrevivência', 'Provar Valor', 'Anarquia', 'Violência', 'Caos', 'Diversão', 'Destruição', 'Fins justificaram os meios', 'Intenção boa, execução ruim', 'Algo deu errado']
    randomPersonalidadeVilao = ['Gentil', 'Habilidoso', 'Honesto', 'Idealista', 'Líder Nato', 'Ignorante', 'Impaciente', 'Impetuoso', 'Inconsequente', 'Inconstante', 'Caótico']
    randomTesouro = ['XP em Dobro', 'Arma mágica', 'Munição', 'Armadura Mágica', 'Tesouro', 'Sorteie 2x', 'Poções Mágicas']
    
    opcaoTipo.set(random.choice(randomTipo))
    opcaoOrigem.set(random.choice(randomOrigem))
    opcaoObjetivo.set(random.choice(randomObjetivo))
    opcaoPersonalidadeVilao.set(random.choice(randomPersonalidadeVilao))
    opcaoTesouro.set(random.choice(randomTesouro))

def gerarMapa():
    opcaoVertical.set(random.choice(range(1, 13)))
    opcaoHorizontal.set(random.choice(range(1, 9)))

def visualizarMapa():
    template = tk.Toplevel()
    template.resizable(False, False)
    template.title('Oráculo II - RPG SOLO - Template')
    grid = tk.PhotoImage(file='Grid.png')
    canvas = tk.Label(template, image=grid)
    canvas.image = grid
    canvas.pack()

def gerarEnigma():
    randomAcao = ['Apertar', 'Puxar', 'Segurar', 'Agarrar e Soltar', 'Empurrar', 'Comparar com outro objeto', 'Ler em voz alta', 'Acertar', 'Concentrar o poder', 'Pisar']
    randomEnigma = ['Um botão', 'Um mecanismo', 'Runas', 'Peças', 'Pedras', 'Objeto', 'Pergaminho', 'Sensor', 'Cristais', 'Invocação', 'Alavanca']

    opcaoAcao.set(random.choice(randomAcao))
    opcaoEnigma.set(random.choice(randomEnigma))

def rolarDados():
    valorTotal = 0
    
    if box.get() == 'd4':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 5))

        opcaoDado.set(valorTotal)
        
    elif box.get() == 'd6':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 7))

        opcaoDado.set(valorTotal)

    elif box.get() == 'd10':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 11))

        opcaoDado.set(valorTotal)

    elif box.get() == 'd12':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 13))

        opcaoDado.set(valorTotal)

    elif box.get() == 'd20':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 21))

        critico = 20 * opcaoQuantidade.get()
        if valorTotal == critico:
            ms.showinfo('Crítico', 'Acerto Crítico!')
        elif valorTotal == 1:
            ms.showerror('Crítico', 'Falha Crítica!')

        opcaoDado.set(valorTotal)

    elif box.get() == 'd100':
        for i in range(0, opcaoQuantidade.get()):
            valorTotal += random.choice(range(1, 101))

        opcaoDado.set(valorTotal)

def gerarDungeon():
    randomSalaDungeon = ['Vazia', 'Inimigo', '1d6 Inimigos', 'Enigma/Pista', 'Armadilha', 'Objetivo da Missão', 'NPC', 'Missão Extra', 'Tesouro']
    randomMissaoExtra = ['Levar NPC para fora', 'Matar 1d6 Monstros', 'Destruír 1 Inimigo específico', 'Transportar item para fora/dentro', 'Proteger NPC', 'Invadir 1d6 Salas Trancadas', 'Fugir']
    randomInimigo = ['Goblin', 'Orc', 'Troll', 'Gnoll', 'Esqueleto', 'Morto-Vivo', 'Homem-Lagarto', 'Minotauro', 'Lesma Gigante', 'Hobgoblin', 'Bandido Comum', 'Espírito']
    randomArmadilha = ['Lâminas', 'Fosso', 'Dardo Venenoso', 'Explosão', 'Emboscada', 'Veneno', 'Armadilha Mágica', 'Buraco', 'Fogo', 'Espinhos']
    randomTesouroDungeon = ['Cura', 'Itens Específicos', 'Gemas', 'Objetos de Arte', 'Armas', 'Itens Diversos', 'Armaduras', 'Materiais especiais', 'Pergaminhos', 'Armas Mágicas']

    opcaoSalaDungeon.set(random.choice(randomSalaDungeon))
    opcaoMissaoExtra.set(random.choice(randomMissaoExtra))
    opcaoInimigo.set(random.choice(randomInimigo))
    opcaoArmadilha.set(random.choice(randomArmadilha))
    opcaoTesouroDungeon.set(random.choice(randomTesouroDungeon))

# INIT
os.system('cls')
######################################## ROOT
root = tk.Tk()
######################################## Painel Um
painelUm = tk.Frame(root, relief=tk.RAISED, bd=5, padx=4, pady=4)
painelUm.grid(row=0, column=0, sticky=tk.N)

######################################## Conteúdo do Painel Um
geradorAventurasFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorAventurasFrame.grid(row=0, column=0, sticky=tk.E)

geradorClimaFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorClimaFrame.grid(row=1, column=0, sticky=tk.E)

geradorEventoFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorEventoFrame.grid(row=2, column=0, sticky=tk.E)

geradorEnigma = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorEnigma.grid(row=3, column=0, sticky=tk.E)

geradorNPCFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorNPCFrame.grid(row=4, column=0, sticky=tk.E)

######################################## Painel Dois
painelDois = tk.Frame(root, padx=4, pady=4)
painelDois.grid(row=0, column=1, sticky=tk.N)

######################################## Conteúdo do Painel Dois
geradorTerreno = tk.Frame(painelDois, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorTerreno.grid(row=0, column=0)

geradorVilao = tk.Frame(painelDois, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorVilao.grid(row=1, column=0)

geradorDungeon = tk.Frame(painelDois, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorDungeon.grid(row=3, column=0)

geradorRespostaFrame = tk.Frame(painelDois, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorRespostaFrame.grid(row=4, column=0)

######################################## Painel Três
painelTres = tk.Frame(root, relief=tk.RAISED, bd=5, padx=4, pady=4)
painelTres.grid(row=0, column=2, sticky=tk.N)

######################################## Conteúdo do Painel Três
geradorEventoFrame2 = tk.Frame(painelTres, relief=tk.GROOVE, bd=3, padx=4, pady=4,)
geradorEventoFrame2.grid(row=0, column=0, columnspan=2)

geradorVilarejo = tk.Frame(painelTres, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorVilarejo.grid(row=1, column=0, columnspan=2)

geradorMapa = tk.Frame(painelTres, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorMapa.grid(row=2, column=0, sticky=tk.W)

geradorDados = tk.Frame(painelTres, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorDados.grid(row=2, column=1, sticky=tk.E)

# GUI
######################################## Conteúdo do Painel Um
#### Gerador Aventura
tk.Label(geradorAventurasFrame, text='Gerador de Aventuras', font=('Tahoma', 12,'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorAventurasFrame, text='O(s) Herói(s) precisam...: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorAventurasFrame, text='um(a)...: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorAventurasFrame, text='que foi...: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorAventurasFrame, text='e está...: ').grid(row=4, column=0, sticky=tk.E)
opcaoUm = tk.StringVar()
tk.Entry(geradorAventurasFrame, textvariable=opcaoUm, width=32, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoDois = tk.StringVar()
tk.Entry(geradorAventurasFrame, textvariable=opcaoDois, width=32, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoTres = tk.StringVar()
tk.Entry(geradorAventurasFrame, textvariable=opcaoTres, width=32, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoQuatro = tk.StringVar()
tk.Entry(geradorAventurasFrame, textvariable=opcaoQuatro, width=32, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)

tk.Button(geradorAventurasFrame, text='Gerar Aventura', command=gerarAventura).grid(row=5, column=0, columnspan=2)
####
#### Gerador Clima
tk.Label(geradorClimaFrame, text='Clima', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoClima = tk.StringVar()
tk.Entry(geradorClimaFrame, textvariable=opcaoClima, width=32, state=tk.DISABLED).grid(row=1, column=1)
opcaoHorario = tk.StringVar()
tk.Entry(geradorClimaFrame, textvariable=opcaoHorario, width=32, state=tk.DISABLED).grid(row=2, column=1)

tk.Button(geradorClimaFrame, text='Gerar Clima', command=gerarClima).grid(row=1, column=0, rowspan=2)
####
#### Gerador Evento
tk.Label(geradorEventoFrame, text='Eventos', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoEvento = tk.StringVar()
tk.Entry(geradorEventoFrame, textvariable=opcaoEvento, width=32, state=tk.DISABLED).grid(row=1, column=1)

tk.Button(geradorEventoFrame, text='Gerar Evento', command=gerarEvento).grid(row=1, column=0)
####
#### Gerador Enigma
tk.Label(geradorEnigma, text='Gerador de Enigma', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorEnigma, text='Ação: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorEnigma, text='Enigma: ').grid(row=2, column=0, sticky=tk.E)

opcaoAcao = tk.StringVar()
tk.Entry(geradorEnigma, textvariable=opcaoAcao, width=35, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoEnigma = tk.StringVar()
tk.Entry(geradorEnigma, textvariable=opcaoEnigma, width=35, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)

tk.Button(geradorEnigma, text='Gerar Enigma', command=gerarEnigma).grid(row=3, column=0, columnspan=2)
####
#### Gerador NPC
tk.Label(geradorNPCFrame, text='NPC', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorNPCFrame, text='Este NPC é Influente?: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Raça: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Gênero: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Aparência: ').grid(row=4, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Personalidade: ').grid(row=5, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Alinhamento: ').grid(row=6, column=0, sticky=tk.E)
tk.Label(geradorNPCFrame, text='Característica chamativa: ').grid(row=7, column=0, sticky=tk.E)

opcaoInfluencia = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoInfluencia, width=32, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoRaca = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoRaca, width=32, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoGenero = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoGenero, width=32, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoAparencia = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoAparencia, width=32, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)
opcaoPersonalidade = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoPersonalidade, width=32, state=tk.DISABLED).grid(row=5, column=1, sticky=tk.W)
opcaoAlinhamento = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoAlinhamento, width=32, state=tk.DISABLED).grid(row=6, column=1, sticky=tk.W)
opcaoCaracteristica = tk.StringVar()
tk.Entry(geradorNPCFrame, textvariable=opcaoCaracteristica, width=32, state=tk.DISABLED).grid(row=7, column=1, sticky=tk.W)

tk.Button(geradorNPCFrame, text='Gerar NPC', command=gerarNPC).grid(row=8, column=0, columnspan=2)
####
########################################

######################################## Conteúdo do Painel Dois
#### Gerador Terreno
tk.Label(geradorTerreno, text='Gerador de Terreno', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorTerreno, text='Tipo de Terreno: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Tamanho: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Salas/Passagens: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Andares (Opcional): ').grid(row=4, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Subterrâneos (Opcional): ').grid(row=5, column=0, sticky=tk.E)

opcaoTerreno = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoTerreno, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoTamanho = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoTamanho, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoSalas = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoSalas, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoAndares = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoAndares, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)
opcaoSubterraneos = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoSubterraneos, state=tk.DISABLED).grid(row=5, column=1, sticky=tk.W)

tk.Button(geradorTerreno, text='Gerar Terreno', command=gerarTerreno).grid(row=6, column=0, columnspan=2)
####
#### Gerador Vilão
tk.Label(geradorVilao, text='Gerador de Vilão', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorVilao, text='Tipo de Vilão: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorVilao, text='Origem: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorVilao, text='Objetivo: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorVilao, text='Alinhamento: ').grid(row=4, column=0, sticky=tk.E)
tk.Label(geradorVilao, text='Tesouro ao ser derrotado: ').grid(row=5, column=0, sticky=tk.E)

opcaoTipo = tk.StringVar()
tk.Entry(geradorVilao, textvariable=opcaoTipo, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoOrigem = tk.StringVar()
tk.Entry(geradorVilao, textvariable=opcaoOrigem, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoObjetivo = tk.StringVar()
tk.Entry(geradorVilao, textvariable=opcaoObjetivo, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoPersonalidadeVilao = tk.StringVar()
tk.Entry(geradorVilao, textvariable=opcaoPersonalidadeVilao, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)
opcaoTesouro = tk.StringVar()
tk.Entry(geradorVilao, textvariable=opcaoTesouro, state=tk.DISABLED).grid(row=5, column=1, sticky=tk.W)

tk.Button(geradorVilao, text='Gerar Vilão', command=gerarVilao).grid(row=6, column=0, columnspan=2)
####
#### Gerador Dungeon
tk.Label(geradorDungeon, text='Gerador de Dungeon', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorDungeon, text='Sala :').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorDungeon, text='Missão Extra: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorDungeon, text='Inimigo: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorDungeon, text='Armadilha').grid(row=4, column=0, sticky=tk.E)
tk.Label(geradorDungeon, text='Tesouros: ').grid(row=5, column=0, sticky=tk.E)

opcaoSalaDungeon = tk.StringVar()
tk.Entry(geradorDungeon, textvariable=opcaoSalaDungeon, width=31, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoMissaoExtra = tk.StringVar()
tk.Entry(geradorDungeon, textvariable=opcaoMissaoExtra, width=31, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoInimigo = tk.StringVar()
tk.Entry(geradorDungeon, textvariable=opcaoInimigo, width=31, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoArmadilha = tk.StringVar()
tk.Entry(geradorDungeon, textvariable=opcaoArmadilha, width=31, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)
opcaoTesouroDungeon = tk.StringVar()
tk.Entry(geradorDungeon, textvariable=opcaoTesouroDungeon, width=31, state=tk.DISABLED).grid(row=5, column=1, sticky=tk.W)

tk.Button(geradorDungeon, text='Gerar Dungeon', command=gerarDungeon).grid(row=6, column=0, columnspan=2)
####
#### Gerador Resposta
tk.Label(geradorRespostaFrame, text='Resposta', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoResposta = tk.StringVar()
tk.Entry(geradorRespostaFrame, textvariable=opcaoResposta, state=tk.DISABLED).grid(row=1, column=1)

tk.Button(geradorRespostaFrame, text='Gerar Resposta', command=gerarResposta).grid(row=1, column=0)
####
########################################

######################################## Conteúdo do Painel Três
#### Gerador Evento Complexo
tk.Label(geradorEventoFrame2, text='Gerador de Evento Complexo', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
eventoUm = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoUm, width=75, state=tk.DISABLED).grid(row=1, column=0, columnspan=2)
eventoDois = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoDois, width=75, state=tk.DISABLED).grid(row=2, column=0, columnspan=2)
eventoTres = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoTres, width=75, state=tk.DISABLED).grid(row=3, column=0, columnspan=2)
eventoQuatro = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoQuatro, width=75, state=tk.DISABLED).grid(row=4, column=0, columnspan=2)
eventoCinco = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoCinco, width=75, state=tk.DISABLED).grid(row=5, column=0, columnspan=2)
eventoSeis = tk.StringVar()
tk.Entry(geradorEventoFrame2, textvariable=eventoSeis, width=75, state=tk.DISABLED).grid(row=6, column=0, columnspan=2)

tk.Button(geradorEventoFrame2, text='Gerar Evento', command=gerarEvento2).grid(row=7, column=0, columnspan=2)
####
#### Gerador Vilarejo
tk.Label(geradorVilarejo, text='Gerador de Vilarejo', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorVilarejo, text='Aspecto: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Sociedade: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Conhecida por...: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Situação Atual: ').grid(row=4, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Taverna: ').grid(row=5, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='A Taverna está...: ').grid(row=6, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Loja de itens: ').grid(row=7, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Exército: ').grid(row=8, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Mercado: ').grid(row=9, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Torre/Quartel: ').grid(row=10, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Guilda: ').grid(row=11, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Templo/Igreja: ').grid(row=12, column=0, sticky=tk.E)
tk.Label(geradorVilarejo, text='Castelo: ').grid(row=13, column=0, sticky=tk.E)

opcaoAspecto = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoAspecto, width=58, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoSociedade = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoSociedade, width=58, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoConhecida = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoConhecida, width=58, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoSituacaoAtual = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoSituacaoAtual, width=58, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)
opcaoTaverna = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoTaverna, width=58, state=tk.DISABLED).grid(row=5, column=1, sticky=tk.W)
opcaoTaverna2 = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoTaverna2, width=58, state=tk.DISABLED).grid(row=6, column=1, sticky=tk.W)
opcaoLojaItens = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoLojaItens, width=58, state=tk.DISABLED).grid(row=7, column=1, sticky=tk.W)
opcaoExercito = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoExercito, width=58, state=tk.DISABLED).grid(row=8, column=1, sticky=tk.W)
opcaoMercado = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoMercado, width=58, state=tk.DISABLED).grid(row=9, column=1, sticky=tk.W)
opcaoTorreQuartel = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoTorreQuartel, width=58, state=tk.DISABLED).grid(row=10, column=1, sticky=tk.W)
opcaoGuilda = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoGuilda, width=58, state=tk.DISABLED).grid(row=11, column=1, sticky=tk.W)
opcaoTemplo = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoTemplo, width=58, state=tk.DISABLED).grid(row=12, column=1, sticky=tk.W)
opcaoCastelo = tk.StringVar()
tk.Entry(geradorVilarejo, textvariable=opcaoCastelo, width=58, state=tk.DISABLED).grid(row=13, column=1, sticky=tk.W)

tk.Button(geradorVilarejo, text='Gerar Vilarejo', command=gerarVilajo).grid(row=14, column=0, columnspan=2)
####
#### Gerador Mapa
tk.Label(geradorMapa, text='Gerador de Mapa', font=('Tahoma', 12, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorMapa, text='VERTICAL: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorMapa, text='HORIZONTAL: ').grid(row=2, column=0, sticky=tk.E)

opcaoVertical = tk.StringVar()
tk.Entry(geradorMapa, textvariable=opcaoVertical, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoHorizontal = tk.StringVar()
tk.Entry(geradorMapa, textvariable=opcaoHorizontal, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)

tk.Button(geradorMapa, text='Gerar Mapa', command=gerarMapa).grid(row=3, column=0)
tk.Button(geradorMapa, text='Visualizar Template', command=visualizarMapa).grid(row=3, column=1)
####
#### Gerador Dados
tk.Label(geradorDados, text='Rolar Dados', relief=tk.SUNKEN, font=('Tahoma', 12, 'bold'), bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorDados, text='Tipo: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorDados, text='Quantidade: ').grid(row=2, column=0, sticky=tk.E)

opcaoDado = tk.IntVar()
tk.Entry(geradorDados, textvariable=opcaoDado, state=tk.DISABLED).grid(row=3, column=1)

tipoDado = ['d4', 'd6', 'd10', 'd12', 'd20', 'd100']
box = ttk.Combobox(geradorDados, values=tipoDado)
box.set('d20')
box.grid(row=1, column=1, sticky=tk.W)

opcaoQuantidade = tk.IntVar()
opcaoQuantidade.set(1)
tk.Entry(geradorDados, textvariable=opcaoQuantidade).grid(row=2, column=1, sticky=tk.W)

tk.Button(geradorDados, text='Rolar Dado(s)', command=rolarDados).grid(row=3, column=0)
####
########################################

# MENU
menuBar = tk.Menu(root)
opcaoMenu = tk.Menu(menuBar, tearoff=0)
sobreMenu = tk.Menu(menuBar, tearoff=0)

menuBar.add_cascade(label='Sobre', menu=sobreMenu)

sobreMenu.add_command(label='Sobre os Desenvolvedores', command=creditos)

# CONFIG
if __name__ == "__main__":
    root.title('Oráculo II - RPG Solo - Criador de Campanhas')
    root.resizable(False, False)
    root.config(menu=menuBar)
    root.mainloop()
