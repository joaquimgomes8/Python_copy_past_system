import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

root = tk.Tk()
root.title("AZShip System")
root.geometry("360x320")
root.attributes('-topmost', True)
root.configure(bg='#5D3FD3')  # roxo principal
root.resizable(False, False)
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
heading_font = tkfont.Font(family='Segoe UI', size=14, weight='bold')
subtitle_font = tkfont.Font(family='Segoe UI', size=10)
btn_font = tkfont.Font(family='Segoe UI', size=10)

style = ttk.Style()
try:
    style.theme_use('clam')
except Exception:
    pass
style.configure('Purple.TFrame', background='#5D3FD3')
style.configure('Purple.TLabel', background='#5D3FD3', foreground='white', font=heading_font)
style.configure('Subtitle.TLabel', background='#5D3FD3', foreground='#EAE6FF', font=subtitle_font)
style.configure('Card.TFrame', background='#6E57FF')
style.configure('Purple.TButton', background='#8A79FF', foreground='white', font=btn_font, padding=6)
style.map('Purple.TButton', background=[('active', '#6E5BFF'), ('pressed', '#5746E6')])

header = ttk.Label(root, text='AZShip System', style='Purple.TLabel')
header.pack(pady=(14, 2))

subtitle = ttk.Label(root, text='Clique para copiar o texto:', style='Subtitle.TLabel')
subtitle.pack(pady=(0, 8))

container = ttk.Frame(root, style='Card.TFrame', padding=(12, 10))
container.pack(fill='both', expand=True, padx=18, pady=8)

btn1 = ttk.Button(container, text='Bom dia', style='Purple.TButton', command=bom_dia)
btn1.pack(fill='x', pady=6)
btn1.configure(cursor='hand2')

btn2 = ttk.Button(container, text='Boa tarde', style='Purple.TButton', command=boa_tarde)
btn2.pack(fill='x', pady=6)
btn2.configure(cursor='hand2')

btn3 = ttk.Button(container, text='Encerramento', style='Purple.TButton', command=encerramento)
btn3.pack(fill='x', pady=6)
btn3.configure(cursor='hand2')

btn4 = ttk.Button(container, text='Ajudo algo mais', style='Purple.TButton', command=ajudo_algo_mais)
btn4.pack(fill='x', pady=6)
btn4.configure(cursor='hand2')

# Centralizar janela na tela
def center_window(win, target_w, target_h):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (target_w // 2)
    y = (hs // 2) - (target_h // 2)
    win.geometry(f"{target_w}x{target_h}+{x}+{y}")

center_window(root, 360, 320)

#===============================
root.mainloop()