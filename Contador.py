import tkinter as tk

# Cria e configura a janela principal do programa.
janela = tk.Tk()
janela.geometry('300x300')
janela.title('Contador')

# Mostra uma mensagem no topo da janela.
texto = tk.Label(janela, text='Contador básico feito por Kaio372-ops')
texto.pack()

# Guarda o valor do contador e o aumenta em 1 a cada chamada.
contador = tk.IntVar(value=0)

def contagem():
    contador.set(contador.get() + 1)

# O botão chama contagem quando é clicado.
tk.Button(janela, text='Clique para somar +1', command=contagem).pack()

# Exibe o valor atual do contador.
numero = tk.Label(janela, textvariable=contador)
numero.pack()

# Mantém a janela aberta e processa os eventos (como cliques).
tk.mainloop()