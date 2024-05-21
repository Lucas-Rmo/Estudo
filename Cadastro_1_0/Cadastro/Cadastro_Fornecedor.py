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

    
    def cadastrar_fornecedor():
        nome = entry_nome.get()
        cnpj = entry_cnpj.get()
        celular = entry_celular.get()
        email = entry_email.get()
        endereco = entry_endereco.get()

        if "@" not in email:
            return tkinter.messagebox.showerror(title="Aviso", message=f"E-mail inválido!"),janela.focus_force()

        if cnpj.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"CNPJ inválido!Digite apenas números."),janela.focus_force()

        if celular.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"Celular inválido!Digite apenas números."),janela.focus_force()

        if nome =="" or cnpj == "" or celular =="" or email=="" or endereco =="":
            return tkinter.messagebox.showerror(title="Aviso", message=f"Preencha todos os campos!"),janela.focus_force()
        conn = sqlite3.connect('fornecedores.db')
        cursor = conn.cursor()

        # Cria tabela de fornecedores
        cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            cnpj TEXT NOT NULL UNIQUE,
                            celular TEXT NOT NULL,
                            email TEXT NOT NULL,
                            endereco TEXT NOT NULL
                            
                        )''')
        conn.commit()

        try:
            cursor.execute('''INSERT INTO fornecedores (nome , cnpj , celular , email , endereco)
                        VALUES (?, ?, ?, ?, ?)''', (nome , cnpj, celular , email , endereco))
            conn.commit()
            tkinter.messagebox.showinfo(title="Aviso", message=f"Fornecedor cadastrado com sucesso!")
            conn.close()
        except:
            tkinter.messagebox.showerror(title="Aviso", message=f"CNPJ já cadastrado!")
            janela.focus_force()
            conn.close()

        
     #cria a janela de cadastro de fornecedor

    janela = tkinter.Tk()
    janela.geometry("325x125")
    janela.minsize(width=375, height=225)
    janela.maxsize(width=375, height=225)
    janela.title("Cadastro de fornecedor")
    janela.focus_force()

    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,    
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #label do nome
    label_nome = customtkinter.CTkLabel(master=janela,text="Nome:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_nome.grid(padx=0.5, pady=0.5,row=1,column =1)

    #campo de entrada do nome
    entry_nome = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_nome.grid(row=1,column =2)

    #label do cpf
    label_cnpj = customtkinter.CTkLabel(master=janela,text="CNPJ:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_cnpj.grid(padx=0.5, pady=0.5,row=2,column =1)

    #campo de entrada do cnpj
    entry_cnpj = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_cnpj.grid(row=2,column =2)


    #label do email
    label_email = customtkinter.CTkLabel(master=janela,text="E-mail:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_email.grid(padx=0.5, pady=0.5,row=3,column =1)

    #campo de entrada do email
    entry_email = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_email.grid(row=3,column =2)

    #label do celular
    label_celular = customtkinter.CTkLabel(master=janela,text="Celular:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_celular.grid(padx=0.5, pady=0.5,row=4,column =1)

    #campo de entrada do celular
    entry_celular = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_celular.grid(row=4,column =2)


    #label do endereço
    label_endereco = customtkinter.CTkLabel(master=janela,text="Endereço:",fg_color="black",
                                        bg_color="black",text_color="white",width=80)
    label_endereco.grid(padx=0.5, pady=0.5,row=5,column =1)

    #campo de entrada do endereço
    entry_endereco = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_endereco.grid(row=5,column =2)

#   botão para cadastro de fornecedor
    button_cadastrar = customtkinter.CTkButton(master=janela,text="Cadastrar",bg_color="black",command = cadastrar_fornecedor)
    button_cadastrar.grid(padx=0.5, pady=0.5,row=6,column =1,columnspan=2)
    janela.focus_force()
    centralizar_janela(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()