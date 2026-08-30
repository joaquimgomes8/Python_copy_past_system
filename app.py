import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

root = tk.Tk()
root.title("AZShip System")
root.geometry("420x380")
root.attributes('-topmost', True)
root.configure(bg='#5D3FD3')  # roxo principal
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

# Estilo e layout
heading_font = tkfont.Font(family='Segoe UI', size=16, weight='bold')
btn_font = tkfont.Font(family='Segoe UI', size=11)

style = ttk.Style()
try:
    style.theme_use('clam')
except Exception:
    pass
style.configure('Purple.TFrame', background='#5D3FD3')
style.configure('Purple.TLabel', background='#5D3FD3', foreground='white', font=heading_font)
style.configure('Purple.TButton', background='#8A79FF', foreground='white', font=btn_font, padding=8)
style.map('Purple.TButton', background=[('active', '#6E5BFF'), ('pressed', '#5746E6')])

header = ttk.Label(root, text='AZShip System', style='Purple.TLabel')
header.pack(pady=(18, 6))

container = ttk.Frame(root, style='Purple.TFrame', padding=(20, 10))
container.pack(fill='both', expand=True, padx=20, pady=10)

btn1 = ttk.Button(container, text='Copiar bom dia', style='Purple.TButton', command=bom_dia)
btn1.pack(fill='x', pady=8)

btn2 = ttk.Button(container, text='Copiar boa tarde', style='Purple.TButton', command=boa_tarde)
btn2.pack(fill='x', pady=8)

btn3 = ttk.Button(container, text='Copiar encerramento', style='Purple.TButton', command=encerramento)
btn3.pack(fill='x', pady=8)

btn4 = ttk.Button(container, text='Copiar ajudo algo mais', style='Purple.TButton', command=ajudo_algo_mais)
btn4.pack(fill='x', pady=8)

# Centralizar janela na tela
def center_window(win):
    win.update_idletasks()
    w = win.winfo_width()
    h = win.winfo_height()
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

center_window(root)

#===============================
root.mainloop()