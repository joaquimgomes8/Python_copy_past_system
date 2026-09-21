import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import tkinter.font as tkfont
import colorsys
import json
import sys
from pathlib import Path

SOFTWARE_TITLE = 'Copy Past System'
WINDOW_COLOR = 'black'
BUTTON_COLOR = '#263238'
BUTTON_HOVER_COLOR = '#37474F'
BUTTON_PRESSED_COLOR = '#1C2529'

APP_DIRECTORY = Path(sys.executable).resolve().parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent
CONFIG_FILE = APP_DIRECTORY / 'config.json'


def cores_dos_botoes(cor_fundo):
    try:
        vermelho, verde, azul = (valor / 65535 for valor in root.winfo_rgb(cor_fundo))
        matiz, saturacao, luminosidade = colorsys.rgb_to_hls(vermelho, verde, azul)

        luminosidade_botao = max(0.18, min(0.38, luminosidade * 0.65))
        luminosidade_hover = min(0.55, luminosidade_botao + 0.12)
        luminosidade_pressionado = max(0.12, luminosidade_botao - 0.08)

        def converter(nova_luminosidade):
            rgb = colorsys.hls_to_rgb(matiz, nova_luminosidade, max(0.25, saturacao))
            return '#{:02X}{:02X}{:02X}'.format(*(round(cor * 255) for cor in rgb))

        return (
            converter(luminosidade_botao),
            converter(luminosidade_hover),
            converter(luminosidade_pressionado),
        )
    except (ValueError, IndexError):
        return BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_PRESSED_COLOR


def aplicar_cores_dos_botoes():
    style.configure(
        'Purple.TButton',
        background=BUTTON_COLOR,
        bordercolor=BUTTON_COLOR,
        lightcolor=BUTTON_COLOR,
        darkcolor=BUTTON_PRESSED_COLOR,
    )
    style.map(
        'Purple.TButton',
        background=[
            ('active', BUTTON_HOVER_COLOR),
            ('pressed', BUTTON_PRESSED_COLOR),
        ],
        bordercolor=[
            ('active', BUTTON_HOVER_COLOR),
            ('pressed', BUTTON_PRESSED_COLOR),
        ],
        lightcolor=[
            ('active', BUTTON_HOVER_COLOR),
            ('pressed', BUTTON_PRESSED_COLOR),
        ],
        darkcolor=[
            ('active', BUTTON_HOVER_COLOR),
            ('pressed', BUTTON_PRESSED_COLOR),
        ],
    )

root = tk.Tk()
root.title(SOFTWARE_TITLE)
root.geometry("360x360")
root.attributes('-topmost', True)
root.configure(bg=WINDOW_COLOR)
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


def carregar_configuracao():
    global SOFTWARE_TITLE, WINDOW_COLOR, BUTTONS

    try:
        with CONFIG_FILE.open('r', encoding='utf-8') as arquivo:
            configuracao = json.load(arquivo)

        if isinstance(configuracao.get('title'), str) and configuracao['title'].strip():
            SOFTWARE_TITLE = configuracao['title'].strip()
        if isinstance(configuracao.get('window_color'), str) and configuracao['window_color'].strip():
            WINDOW_COLOR = configuracao['window_color'].strip()
        if isinstance(configuracao.get('buttons'), dict):
            botoes_salvos = {}
            for chave, botao in configuracao['buttons'].items():
                if (
                    isinstance(chave, str)
                    and isinstance(botao, dict)
                    and isinstance(botao.get('label'), str)
                    and isinstance(botao.get('text'), str)
                ):
                    botoes_salvos[chave] = {
                        'label': botao['label'],
                        'text': botao['text'],
                    }
            BUTTONS = botoes_salvos
    except (OSError, json.JSONDecodeError, AttributeError):
        pass


def salvar_configuracao():
    configuracao = {
        'title': SOFTWARE_TITLE,
        'window_color': WINDOW_COLOR,
        'buttons': BUTTONS,
    }
    try:
        with CONFIG_FILE.open('w', encoding='utf-8') as arquivo:
            json.dump(configuracao, arquivo, ensure_ascii=False, indent=2)
    except OSError:
        pass


carregar_configuracao()
BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_PRESSED_COLOR = cores_dos_botoes(WINDOW_COLOR)
root.title(SOFTWARE_TITLE)
root.configure(bg=WINDOW_COLOR)


def copiar_texto(texto):
    root.clipboard_clear()
    root.clipboard_append(texto)
    root.update()


def criar_callback(chave):
    return lambda: copiar_texto(BUTTONS[chave]['text'])


def criar_botao_interface(chave):
    botao = ttk.Button(
        container,
        text=BUTTONS[chave]['label'],
        style='Purple.TButton',
        command=criar_callback(chave),
    )
    botao.pack(fill='x', pady=4)
    botao.configure(cursor='hand2')
    globals()['botao_' + chave] = botao


def atualizar_tamanho_janela():
    altura = 360 + max(0, len(BUTTONS) - 5) * 42
    center_window(root, 360, altura)


def abrir_editor_textos():
    editor = tk.Toplevel(root)
    editor.title('Editar textos')
    editor.configure(bg=WINDOW_COLOR)
    editor.transient(root)
    editor.grab_set()
    editor.resizable(False, False)

    container = ttk.Frame(editor, padding=8)
    container.pack(fill='both', expand=True)

    campos = {}
    cor_selecionada = WINDOW_COLOR

    ttk.Label(container, text='Título do software:').pack(anchor='w', pady=(0, 2))
    entrada_titulo = ttk.Entry(container, width=54)
    entrada_titulo.insert(0, SOFTWARE_TITLE)
    entrada_titulo.pack(fill='x', pady=(0, 8))

    linha_cor = ttk.Frame(container)
    linha_cor.pack(fill='x', pady=(0, 8))
    ttk.Label(linha_cor, text='Cor da janela:').pack(side='left')
    botao_cor = ttk.Button(linha_cor, text=cor_selecionada)
    botao_cor.pack(side='left', padx=(8, 0))

    def selecionar_cor():
        nonlocal cor_selecionada
        _, nova_cor = colorchooser.askcolor(color=cor_selecionada, parent=editor)
        if nova_cor:
            cor_selecionada = nova_cor
            botao_cor.config(text=cor_selecionada)

    botao_cor.config(command=selecionar_cor)

    lista_campos = ttk.Frame(container)
    lista_campos.pack(fill='x')

    def criar_campo(chave, botao):
        linha = ttk.Frame(lista_campos)
        linha.pack(fill='x', pady=4)

        ttk.Label(linha, text='Botão:', width=9).pack(side='left')
        entrada_label = ttk.Entry(linha, width=16)
        entrada_label.insert(0, botao['label'])
        entrada_label.pack(side='left', padx=(4, 8))

        ttk.Label(linha, text='Texto:', width=8).pack(side='left')
        entrada_texto = ttk.Entry(linha, width=24)
        entrada_texto.insert(0, botao['text'])
        entrada_texto.pack(side='left', padx=(4, 0))

        campos[chave] = {'label': entrada_label, 'text': entrada_texto}

        def excluir_campo():
            campos.pop(chave, None)
            linha.destroy()
            altura = 340 + max(0, len(campos) - 5) * 48
            center_window(editor, 500, altura)

        ttk.Button(linha, text='Excluir', command=excluir_campo).pack(side='left', padx=(8, 0))

    for chave, botao in BUTTONS.items():
        criar_campo(chave, botao)

    def adicionar_campo():
        numero = 1
        while f'novo_{numero}' in campos:
            numero += 1
        chave = f'novo_{numero}'
        criar_campo(chave, {'label': 'Novo botão', 'text': 'Texto para copiar'})
        altura = 340 + max(0, len(campos) - 5) * 48
        center_window(editor, 500, altura)

    def salvar():
        global SOFTWARE_TITLE, WINDOW_COLOR
        global BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_PRESSED_COLOR

        novo_titulo = entrada_titulo.get().strip() or SOFTWARE_TITLE
        SOFTWARE_TITLE = novo_titulo
        WINDOW_COLOR = cor_selecionada
        BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_PRESSED_COLOR = cores_dos_botoes(WINDOW_COLOR)
        root.title(SOFTWARE_TITLE)
        root.configure(bg=WINDOW_COLOR)
        style.configure('Purple.TFrame', background=WINDOW_COLOR)
        style.configure('Purple.TLabel', background=WINDOW_COLOR)
        style.configure('Subtitle.TLabel', background=WINDOW_COLOR)
        style.configure('Card.TFrame', background=WINDOW_COLOR)
        aplicar_cores_dos_botoes()
        header.config(text=SOFTWARE_TITLE)

        for chave in list(BUTTONS):
            if chave not in campos:
                BUTTONS.pop(chave)
                botao = globals().pop('botao_' + chave, None)
                if botao is not None:
                    botao.destroy()

        for chave, campo in campos.items():
            valores_atuais = BUTTONS.get(chave, {})
            novo_label = campo['label'].get().strip() or valores_atuais.get('label', 'Novo botão')
            novo_texto = campo['text'].get().strip() or valores_atuais.get('text', 'Texto para copiar')
            BUTTONS[chave] = {'label': novo_label, 'text': novo_texto}

            if 'botao_' + chave in globals():
                globals()['botao_' + chave].config(text=novo_label)
            else:
                criar_botao_interface(chave)

            salvar_configuracao()
        atualizar_tamanho_janela()
        editor.destroy()

    botoes = ttk.Frame(container)
    botoes.pack(fill='x', pady=(8, 0))
    ttk.Button(botoes, text='Adicionar botão', command=adicionar_campo).pack(side='left')
    ttk.Button(botoes, text='Salvar', command=salvar).pack(side='right', padx=(0, 6))
    ttk.Button(botoes, text='Cancelar', command=editor.destroy).pack(side='right')

    altura_editor = 340 + max(0, len(campos) - 5) * 48
    center_window(editor, 500, altura_editor)

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
style.configure('Purple.TFrame', background=WINDOW_COLOR)
style.configure('Purple.TLabel', background=WINDOW_COLOR, foreground='white', font=heading_font)
style.configure('Subtitle.TLabel', background=WINDOW_COLOR, foreground='#EAE6FF', font=subtitle_font)
style.configure('Card.TFrame', background=WINDOW_COLOR)
style.configure('Purple.TButton', foreground='white', font=btn_font, padding=6)
aplicar_cores_dos_botoes()

header = ttk.Label(root, text=SOFTWARE_TITLE, style='Purple.TLabel')
header.pack(pady=(10, 1))

subtitle = ttk.Label(root, text='Clique para copiar o texto:', style='Subtitle.TLabel')
subtitle.pack(pady=(0, 6))

container = ttk.Frame(root, style='Card.TFrame', padding=(10, 8))
container.pack(fill='both', expand=True, padx=12, pady=(6, 10))

for chave in BUTTONS:
    criar_botao_interface(chave)

editar_button = ttk.Button(root, text='Editar textos/cores', style='Purple.TButton', command=abrir_editor_textos)
editar_button.pack(fill='x', padx=12, pady=(0, 10))
editar_button.configure(cursor='hand2')

# Centralizar janela na tela
def center_window(win, target_w, target_h):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (target_w // 2)
    y = (hs // 2) - (target_h // 2)
    win.geometry(f"{target_w}x{target_h}+{x}+{y}")

atualizar_tamanho_janela()


def fechar_app():
    salvar_configuracao()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', fechar_app)

#===============================
root.mainloop()