# IMPORTS
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import tkinter.messagebox as ms
import os
import random
import openpyxl

# FUNCTIONS
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
    opcaoTamanho.set(random.choice(randomTamanho))




# INIT
os.system('cls')
root = tk.Tk()

painelUm = tk.Frame(root, relief=tk.RAISED, bd=5, padx=4, pady=4)
painelUm.grid(row=0, column=0, sticky=tk.N)
painelDois = tk.Frame(root, relief=tk.RAISED, bd=5, padx=4, pady=4)
painelDois.grid(row=0, column=1, sticky=tk.N)
painelTres = tk.Frame(root, relief=tk.RAISED, bd=5, padx=4, pady=4)
painelTres.grid(row=0, column=2, sticky=tk.N)

geradorAventurasFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorAventurasFrame.grid(row=0, column=0)

geradorClimaFrame = tk.Frame(painelUm, padx=4, pady=4)
geradorClimaFrame.grid(row=1, column=0)

geradorRespostaFrame = tk.Frame(painelUm, padx=4, pady=4)
geradorRespostaFrame.grid(row=2, column=0)

geradorEventoFrame = tk.Frame(painelUm, padx=4, pady=4)
geradorEventoFrame.grid(row=3, column=0)

geradorNPCFrame = tk.Frame(painelUm, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorNPCFrame.grid(row=4, column=0)

geradorTerreno = tk.Frame(painelDois, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorTerreno.grid(row=0, column=0)

geradorEventoFrame2 = tk.Frame(painelTres, relief=tk.GROOVE, bd=3, padx=4, pady=4)
geradorEventoFrame2.grid(row=0, column=0)





# GUI
tk.Label(geradorAventurasFrame, text='Gerador de Aventuras', font=('Tahoma',14,'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
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

tk.Label(geradorClimaFrame, text='Clima', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoClima = tk.StringVar()
tk.Entry(geradorClimaFrame, textvariable=opcaoClima, width=32, state=tk.DISABLED).grid(row=1, column=0, columnspan=2)
opcaoHorario = tk.StringVar()
tk.Entry(geradorClimaFrame, textvariable=opcaoHorario, width=32, state=tk.DISABLED).grid(row=2, column=0, columnspan=2)

tk.Button(geradorClimaFrame, text='Gerar Clima', command=gerarClima).grid(row=3, column=0, columnspan=2)

tk.Label(geradorRespostaFrame, text='Resposta', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoResposta = tk.StringVar()
tk.Entry(geradorRespostaFrame, textvariable=opcaoResposta, width=32, state=tk.DISABLED).grid(row=1, column=0, columnspan=2)

tk.Button(geradorRespostaFrame, text='Gerar Resposta', command=gerarResposta).grid(row=2, column=0, columnspan=2)

tk.Label(geradorEventoFrame, text='Eventos', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
opcaoEvento = tk.StringVar()
tk.Entry(geradorEventoFrame, textvariable=opcaoEvento, width=32, state=tk.DISABLED).grid(row=1, column=0, columnspan=2)

tk.Button(geradorEventoFrame, text='Gerar Evento', command=gerarEvento).grid(row=2, column=0, columnspan=2)

tk.Label(geradorNPCFrame, text='NPC', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
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

tk.Label(geradorTerreno, text='Gerador de Terreno', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
tk.Label(geradorTerreno, text='Tamanho: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Salas/Passagens: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Andares (Opcional): ').grid(row=3, column=0, sticky=tk.E)
tk.Label(geradorTerreno, text='Subterrâneos (Opcional): ').grid(row=4, column=0, sticky=tk.E)   

opcaoTamanho = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoTamanho, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoSalas = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoSalas, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoAndares = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoAndares, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoSubterraneos = tk.StringVar()
tk.Entry(geradorTerreno, textvariable=opcaoSubterraneos, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)

tk.Button(geradorTerreno, text='Gerar Terreno', command=gerarTerreno).grid(row=5, column=0, columnspan=2)

tk.Label(geradorEventoFrame2, text='Gerador de Evento', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2)
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

# MENU
menuBar = tk.Menu(root)
opcaoMenu = tk.Menu(menuBar, tearoff=0)
sobreMenu = tk.Menu(menuBar, tearoff=0)
ajudaMenu = tk.Menu(sobreMenu, tearoff=0)

menuBar.add_cascade(label='Opções', menu=opcaoMenu)
menuBar.add_cascade(label='Sobre', menu=sobreMenu)
sobreMenu.add_cascade(label='Regras', menu=ajudaMenu)

opcaoMenu.add_command(label='Limpar tudo')
opcaoMenu.add_separator()
opcaoMenu.add_command(label='Limpar Aventura')
opcaoMenu.add_command(label='Limpar Clima')
opcaoMenu.add_command(label='Limpar Resposta')
opcaoMenu.add_command(label='Limpar Evento')

sobreMenu.add_separator()
sobreMenu.add_command(label='Sobre os Desenvolvedores')

# CONFIG
if __name__ == "__main__":
    root.title('Oráculo II - RPG Solo - Criador de Campanhas')
    root.state('zoomed')
    root.config(menu=menuBar)
    root.mainloop()