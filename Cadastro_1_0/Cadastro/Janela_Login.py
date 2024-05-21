import tkinter
import customtkinter
import Criar_Conta
import Janela_Principal
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

def logar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    usuario_nome = entry_usuario.get()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM usuarios
                   WHERE usuario = ? AND senha = ?''', (usuario, senha))
    usuario = cursor.fetchone()
    if usuario:
        tkinter.messagebox.showinfo(title="Bem-vindo!", message=f"Logado com sucesso!\nOlá, {usuario_nome}.")
        return janela.destroy(),Janela_Principal.main()
        
    elif usuario == "" or senha =="":
         tkinter.messagebox.showerror(title="Atenção!", message=f"Preencha todos os campos!")
    else:
        tkinter.messagebox.showerror(title="Atenção!", message=f"Usuário e/ou senha incorretos!")
#cria a janela principal
janela = tkinter.Tk()
janela.geometry("325x125")
janela.minsize(width=325, height=125)
janela.maxsize(width=325, height=125)
janela.title("Login")

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

#botão para logar 
button_login = customtkinter.CTkButton(master=janela,text="Login",bg_color="black",command=logar)
button_login.grid(padx=0.5, pady=0.5,row=3,column =2)

#botão para criação de conta
button_criar = customtkinter.CTkButton(master=janela,text="Criar conta",bg_color="black",command=Criar_Conta.main)
button_criar.grid(padx=0.5, pady=0.5,row=4,column =2)

centralizar_janela(janela)
janela.mainloop()