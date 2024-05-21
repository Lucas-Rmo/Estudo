import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox

def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f"+{x}+{y}")  

def main():

    def criar_usuario():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        email = entry_email.get()

        if "@" not in email:
             return tkinter.messagebox.showerror(title="Aviso", message=f"E-mail inválido!"),janela.focus_force()
        if usuario == "" or senha == "" or email== "":
            return tkinter.messagebox.showerror(title="Aviso", message=f"Preencha todos os campos!"),janela.focus_force()
            # Conecta ao banco de dados
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Cria tabela de usuários
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario TEXT NOT NULL UNIQUE,
                            email TEXT NOT NULL UNIQUE,
                            senha TEXT NOT NULL
                        )''')
        conn.commit()

        try:
            cursor.execute('''INSERT INTO usuarios (usuario, email, senha)
                        VALUES (?, ?, ?)''', (usuario, email, senha))
            conn.commit()
            tkinter.messagebox.showinfo(title="Aviso", message=f"Usuário cadastrado com sucesso!")
            janela.destroy()
            
        except sqlite3.IntegrityError:
            # Usuário já existe
            tkinter.messagebox.showerror(title="Aviso", message=f"Usuário ou e-mail já cadastrado!")
            janela.focus_force()
            conn.close()




    #cria a janela de criação de conta

    janela = tkinter.Tk()
    janela.geometry("325x125")
    janela.minsize(width=325, height=225)
    janela.maxsize(width=325, height=225)
    janela.title("Criação de conta")
    janela.focus_force()
    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #label do usuario
    label_usuario = customtkinter.CTkLabel(master=janela,text="Usuário:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_usuario.grid(padx=0.5, pady=0.5,row=1,column =1)

    #campo de entrada do usuario
    entry_usuario = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_usuario.grid(row=1,column =2)

    #label da senha
    label_senha = customtkinter.CTkLabel(master=janela,text="Senha:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_senha.grid(padx=0.5, pady=0.5,row=2,column =1)

    #campo de entrada da senha
    entry_senha = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black",show = "*")
    entry_senha.grid(row=2,column =2)

    #label do e-mail
    label_email = customtkinter.CTkLabel(master=janela,text="E-mail:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_email.grid(padx=0.5, pady=0.5,row=3,column =1)

    #campo de entrada do e-mail
    entry_email = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_email.grid(row=3,column =2)

    #botão para criar a conta
    button_criar = customtkinter.CTkButton(master=janela,text="Criar conta",bg_color="black",command=criar_usuario)
    button_criar.grid(padx=0.5, pady=0.5,row=4,column =2)

    centralizar_janela(janela)
    janela.mainloop()

    

if __name__ == "__main__":
    main()