# Copy Past System
Um pequeno utilitário desktop em Python/Tkinter para copiar rapidamente textos prontos de atendimento com um único clique. Ideal para equipes de suporte e atendimento que precisam responder clientes com mensagens padronizadas (saudações, encerramento, avisos de inatividade, etc.).

# 📋 Sobre o Projeto
O Copy Past System exibe uma janela compacta e sempre visível (topmost) com botões que, ao serem clicados, copiam automaticamente um texto pré-definido para a área de transferência. Basta colar (Ctrl+V) no chat ou sistema de atendimento.

# ✨ Funcionalidades
✅ Cópia com um clique — clique no botão e o texto vai direto para o clipboard.

✅ Botões pré-configurados:

Bom dia
Boa tarde
Encerramento
Inatividade
Ajudo algo mais
✅ Editor integrado — edite os rótulos dos botões e os textos copiados sem mexer no código.

✅ Adicionar novos botões dinamicamente pelo editor.

✅ Personalização de cores — escolha a cor da janela e o software gera automaticamente tons harmônicos para os botões 
(normal, hover e pressionado).

✅ Janela sempre no topo — não perde o foco durante o atendimento.

✅ Redimensionamento automático conforme o número de botões.

# 🚀 Como Usar
Você tem duas formas de executar o software:

🟡Opção 1 — Executável (sem precisar instalar Python)
Vá até a pasta /dist.

Execute o arquivo app.py (ou o executável gerado, caso tenha sido compilado com PyInstaller).

A janela do Copy Past System abrirá automaticamente.

💡 Nenhuma instalação adicional é necessária nessa modalidade.

🟡Opção 2 — Executar pelo código-fonte (requer Python)
Pré-requisito: Python 3.8 ou superior instalado.

Clone o repositório
git clone [https://github.com/seu-usuario/copy-past-system.git](https://github.com/joaquimgomes8/Python_copy_past_system)

Entre na pasta
cd copy-past-system
Execute
python app.py
