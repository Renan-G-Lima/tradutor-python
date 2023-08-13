from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Especificações da janela
root = tk.Tk()
root.title('Task Copillot')
root.geometry('250x550')
root.resizable(width=True, height=False)
x = root.attributes('-alpha', 0.6)
root.configure(background='#1d1d1d')
translator = Translator()

# Função para traduzir o texto //1c foi o ideal. Se for mais que isso, ele erra a tradução
def translate():
    lang_1 = text_input.get('1.0', 'end-1c').strip()
    pl = pick_language.get()

    if lang_1 == '':
        return

    output = translator.translate(lang_1, dest=pl)
    text_output.delete(1.0, 'end')
    text_output.insert('end', output.text)

# Verifica se há mudança no texto a cada 500ms para traduzir
def on_text_change(_):
    lang_1 = text_input.get(1.0, 'end')
    #se a parte onde escreve estiver vazio, apaga a tradução
    if lang_1.strip() == '':
        text_output.delete(1.0, 'end')
        return

    root.after(500, translate)


# Escolhe a para a qual lingua será feita a tradução
pick_language = tk.StringVar()
pick_language.set('English')

pick_language_box = ttk.Combobox(root, width=14, textvariable=pick_language, state='readonly', font=('Arial', 8, 'bold'))
pick_language_box['values'] = ('English', 'Portuguese')  # Usar 'en' para Inglês e 'pt' para Português
pick_language_box.place(x=9, y=260)
pick_language_box.current(0)  # Defina o índice da língua de destino inicial (Inglês)

# Texto do usuário
text_input = Text(root, width=32, height=12, borderwidth=0.5, relief=RIDGE, fg='gray', bg='#1c1c1c', font=('italic', 10, 'bold'))
text_input.place(x=9, y=40)

# Saída do texto do usuário
text_output = Text(root, width=32, height=12, borderwidth=0.5, relief=RIDGE, fg='gray', bg='#1c1c1c', font=('italic', 10, 'bold'))
text_output.place(x=9, y=280)

# Chama a função para verificar o texto (on_text_change)
text_input.bind('<KeyRelease>', on_text_change)

root.mainloop()
