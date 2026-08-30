import tkinter as tk
root = tk.Tk()
root.title("AZShip System")
root.geometry("400x300")
root.attributes('-topmost',True)
#===============================
def bom_dia():
    texto_bom_dia = "Bom dia, meu nome é Joaquim e estarei de ajudando neste atendimento. Em que posso ajudar?"

    root.clipboard_clear() 
    root.clipboard_append(texto_bom_dia) 
    root.update()

def boa_tarde():
    texto_boa_tarde = "Boa tarde, meu nome é Joaquim e estarei de ajudando neste atendimento. Em que posso ajudar?"

    root.clipboard_clear() 
    root.clipboard_append(texto_boa_tarde) 
    root.update()

def encerramento():
    texto_encerramento = "Irei encerrar este atendimento, caso precise de ajuda novamente, estarei a disposição. Obrigado!"

    root.clipboard_clear() 
    root.clipboard_append(texto_encerramento) 
    root.update()

def ajudo_algo_mais():
    texto_ajudo_algo_mais = "Posso te ajudar em mais alguma coisa?"

    root.clipboard_clear() 
    root.clipboard_append(texto_ajudo_algo_mais) 
    root.update()

#===============================

button = tk.Button(root, text="Copiar bom dia", command=bom_dia)
button.pack(pady=20)

button = tk.Button(root, text="Copiar boa tarde", command=boa_tarde)
button.pack(pady=20)
    
button = tk.Button(root, text="Copiar encerramento", command=encerramento)
button.pack(pady=20)

button = tk.Button(root, text="Copiar ajudo algo mais", command=ajudo_algo_mais)
button.pack(pady=20)

#===============================
root.mainloop()