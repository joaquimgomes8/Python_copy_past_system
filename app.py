import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

root = tk.Tk()
root.title("AZShip System")
root.geometry("400x420")
root.attributes('-topmost', True)
root.configure(bg='#5D3FD3')  # roxo principal
root.resizable(False, False)

#===============================
BUTTONS = {
    'bom_dia': {
        'label': 'Bom dia',
        'text': 'Olá, bom dia! Meu nome é Joaquim e serei responsável pelo seu atendimento. Como posso ajudá-lo?'
    },
    'boa_tarde': {
        'label': 'Boa tarde',
        'text': 'Olá, boa tarde! Meu nome é Joaquim e serei responsável pelo seu atendimento. Como posso ajudá-lo?'
    },
    'encerramento': {
        'label': 'Encerramento',
        'text': 'Irei finalizar o atendimento. Permanecemos à disposição para quaisquer dúvidas ou necessidades futuras. Obrigado!'
    },
    'inatividade': {
        'label': 'Inatividade',
        'text': 'Visto que a solicitação inicial foi atendida/resolvida, e estamos há um tempo sem interação, vou finalizar esse chat, mas se houver alguma outra demanda, ou futura dúvida, é só nos chamar que estaremos à disposição! Obrigado!'
    },
    'ajudo_algo_mais': {
        'label': 'Ajudo algo mais',
        'text': 'Ajudo em algo mais?'
    }
}


def copiar_texto(texto):
    root.clipboard_clear()
    root.clipboard_append(texto)
    root.update()


def criar_callback(chave):
    return lambda: copiar_texto(BUTTONS[chave]['text'])


def abrir_editor_textos():
    editor = tk.Toplevel(root)
    editor.title('Editar textos')
    editor.configure(bg='#5D3FD3')
    editor.transient(root)
    editor.grab_set()
    editor.resizable(False, False)

    container = ttk.Frame(editor, padding=12)
    container.pack(fill='both', expand=True)

    campos = {}

    for chave, botao in BUTTONS.items():
        linha = ttk.Frame(container)
        linha.pack(fill='x', pady=6)

        ttk.Label(linha, text='Botão:', width=12).pack(side='left')
        entrada_label = ttk.Entry(linha, width=20)
        entrada_label.insert(0, botao['label'])
        entrada_label.pack(side='left', padx=(4, 8))

        ttk.Label(linha, text='Texto:', width=10).pack(side='left')
        entrada_texto = ttk.Entry(linha, width=32)
        entrada_texto.insert(0, botao['text'])
        entrada_texto.pack(side='left', padx=(4, 0))

        campos[chave] = {'label': entrada_label, 'text': entrada_texto}

    def salvar():
        for chave, campo in campos.items():
            novo_label = campo['label'].get().strip() or BUTTONS[chave]['label']
            novo_texto = campo['text'].get().strip() or BUTTONS[chave]['text']
            BUTTONS[chave]['label'] = novo_label
            BUTTONS[chave]['text'] = novo_texto

            if 'botao_' + chave in globals():
                globals()['botao_' + chave].config(text=novo_label)

        editor.destroy()

    botoes = ttk.Frame(container)
    botoes.pack(fill='x', pady=(10, 0))
    ttk.Button(botoes, text='Salvar', command=salvar).pack(side='right', padx=(0, 6))
    ttk.Button(botoes, text='Cancelar', command=editor.destroy).pack(side='right')

    center_window(editor, 560, 320)

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
container.pack(fill='both', expand=True, padx=18, pady=(8, 12))

for chave, dados in BUTTONS.items():
    nome_botao = f'botao_{chave}'
    botao = ttk.Button(container, text=dados['label'], style='Purple.TButton', command=criar_callback(chave))
    botao.pack(fill='x', pady=6)
    botao.configure(cursor='hand2')
    globals()[nome_botao] = botao

editar_button = ttk.Button(root, text='Editar textos', style='Purple.TButton', command=abrir_editor_textos)
editar_button.pack(fill='x', padx=18, pady=(0, 14))
editar_button.configure(cursor='hand2')

# Centralizar janela na tela
def center_window(win, target_w, target_h):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (target_w // 2)
    y = (hs // 2) - (target_h // 2)
    win.geometry(f"{target_w}x{target_h}+{x}+{y}")

center_window(root, 400, 420)

#===============================
root.mainloop()