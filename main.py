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

# INIT
os.system('cls')
root = tk.Tk()

# GUI
tk.Label(root, text='Gerador de Aventuras', font=('Tahoma',14,'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=0, columnspan=2, sticky=tk.W)
tk.Label(root, text='O(s) Herói(s) precisam...: ').grid(row=1, column=0, sticky=tk.E)
tk.Label(root, text='um(a)...: ').grid(row=2, column=0, sticky=tk.E)
tk.Label(root, text='que foi...: ').grid(row=3, column=0, sticky=tk.E)
tk.Label(root, text='e está...: ').grid(row=4, column=0, sticky=tk.E)

opcaoUm = tk.StringVar()
tk.Entry(root, textvariable=opcaoUm, width=32, state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)
opcaoDois = tk.StringVar()
tk.Entry(root, textvariable=opcaoDois, width=32, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)
opcaoTres = tk.StringVar()
tk.Entry(root, textvariable=opcaoTres, width=32, state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)
opcaoQuatro = tk.StringVar()
tk.Entry(root, textvariable=opcaoQuatro, width=32, state=tk.DISABLED).grid(row=4, column=1, sticky=tk.W)

tk.Button(root, text='Gerar Aventura', command=gerarAventura).grid(row=5, column=0, sticky=tk.W)

tk.Label(root, text='Clima', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=3, sticky=tk.W)
opcaoClima = tk.StringVar()
tk.Entry(root, textvariable=opcaoClima, width=32, state=tk.DISABLED).grid(row=1, column=3, sticky=tk.W)
opcaoHorario = tk.StringVar()
tk.Entry(root, textvariable=opcaoHorario, width=32, state=tk.DISABLED).grid(row=2, column=3, sticky=tk.W)

tk.Button(root, text='Gerar Clima', command=gerarClima).grid(row=5, column=3, sticky=tk.W)

tk.Label(root, text='Resposta', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=4, sticky=tk.W)
opcaoResposta = tk.StringVar()
tk.Entry(root, textvariable=opcaoResposta, width=32, state=tk.DISABLED).grid(row=1, column=4, sticky=tk.W)

tk.Button(root, text='Gerar Resposta', command=gerarResposta).grid(row=5, column=4, sticky=tk.W)

tk.Label(root, text='Eventos', font=('Tahoma', 14, 'bold'), relief=tk.SUNKEN, bd=3, padx=4, pady=4).grid(row=0, column=5, sticky=tk.W)
opcaoEvento = tk.StringVar()
tk.Entry(root, textvariable=opcaoEvento, width=32, state=tk.DISABLED).grid(row=1, column=5, sticky=tk.W)

tk.Button(root, text='Gerar Evento', command=gerarEvento).grid(row=5, column=5, sticky=tk.W)

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