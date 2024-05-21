import tkinter
import customtkinter
import sqlite3
from tkinter import messagebox


def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 - 150
    y = (altura_tela - altura_janela) // 2 - 50

    janela.geometry(f"+{x}+{y}")  


def main():
    
    def buscar_fornecedor():
        # Conectar ao banco de dados
        conn = sqlite3.connect('fornecedores.db')
        cursor = conn.cursor()

        fornecedor_id = entry_id.get()
        # Consultar o banco de dados para obter os dados do cliente
        cursor.execute("SELECT * FROM fornecedores WHERE id = ?", (fornecedor_id,))
        # Retorna uma tupla com os dados do fornecedor
        fornecedor = cursor.fetchone()  

        # Preenche os campos da tela com os dados do fornecedor, se encontrado
        if fornecedor:
            print(fornecedor)
            entry_nome.delete(0,tkinter.END)
            entry_cnpj.delete(0,tkinter.END)
            entry_email.delete(0,tkinter.END)
            entry_celular.delete(0,tkinter.END)
            entry_endereco.delete(0,tkinter.END)

            entry_nome.insert(0,str(fornecedor[1]))
            entry_cnpj.insert(0,str(fornecedor[2]))
            entry_email.insert(0,str(fornecedor[4]))
            entry_celular.insert(0,str(fornecedor[3]))
            entry_endereco.insert(0,str(fornecedor[5]))
            

        else:
            # Se o fornecedor não for encontrado, limpa os campos
            entry_nome.delete(0,tkinter.END)
            entry_cnpj.delete(0,tkinter.END)
            entry_email.delete(0,tkinter.END)
            entry_celular.delete(0,tkinter.END)
            entry_endereco.delete(0,tkinter.END)
            tkinter.messagebox.showerror(title="Atenção!", message=f"Id não encontrado!")
            janela.focus_force()
        # Fecha a conexão com o banco de dados
        conn.close()
    
    def alterar_fornecedor():

        #conecta no banco de dados
        conn = sqlite3.connect('fornecedores.db')
        cursor = conn.cursor()

        # Obter os novos valores dos campos de entrada e o ID
        fornecedor_id = entry_id.get()

        novo_nome = entry_nome.get()
        novo_cnpj = entry_cnpj.get()
        novo_email = entry_email.get()
        novo_celular = entry_celular.get()
        novo_endereco = entry_endereco.get()

        if "@" not in novo_email:
            return tkinter.messagebox.showerror(title="Aviso", message=f"E-mail inválido!"),janela.focus_force()

        if novo_cnpj.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"CNPJ inválido!Digite apenas números."),janela.focus_force()

        if novo_celular.isnumeric() == False:
            return tkinter.messagebox.showerror(title="Aviso", message=f"Celular inválido!Digite apenas números."),janela.focus_force()


         # Executar a instrução SQL UPDATE
        cursor.execute("UPDATE fornecedores SET nome = ?, cnpj = ?, email = ?, celular = ?, endereco = ? WHERE id = ?", 
                    (novo_nome, novo_cnpj, novo_email, novo_celular, novo_endereco, fornecedor_id))

        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo(title="Sucesso!", message=f"Dados alterados com sucesso!")
        entry_nome.delete(0,tkinter.END)
        entry_cnpj.delete(0,tkinter.END)
        entry_email.delete(0,tkinter.END)
        entry_celular.delete(0,tkinter.END)
        entry_endereco.delete(0,tkinter.END)



    #cria a janela principal
    janela = tkinter.Tk()
    janela.geometry("400x250")
    janela.minsize(width=400, height=250)
    janela.maxsize(width=400, height=250)
    janela.title("Alteração de Fornecedor")



    #cria o frame de fundo da janela,usado para definir a cor de fundo
    frame = customtkinter.CTkFrame(master=janela,
                            width=1920,
                            height=1280,
                            corner_radius=10,fg_color="black"
                            )
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_id_fornecedor = customtkinter.CTkLabel(master=janela,text="Id do fornecedor:",fg_color="black",
                                       bg_color="black",text_color="white",width=130)
    label_id_fornecedor.grid(padx=0.5, pady=0.5,row=0,column =0)

    entry_id = customtkinter.CTkEntry(master=janela,
                            width=250,
                            height=25,
                            corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_id.grid(row=0,column =1)

    button_id = customtkinter.CTkButton(master=janela,text="Buscar id",bg_color="black",command=buscar_fornecedor)
    button_id.grid(padx=0.5, pady=0.5,row=1,column =0,columnspan=2)
    
    #label do nome
    label_nome = customtkinter.CTkLabel(master=janela,text="Nome:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_nome.grid(padx=0.5, pady=0.5,row=2,column =0)

    #campo de entrada do nome
    entry_nome = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_nome.grid(row=2,column =1)
    

    #label do cnpj
    label_cpf = customtkinter.CTkLabel(master=janela,text="CNPJ:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_cpf.grid(padx=0.5, pady=0.5,row=3,column =0)

    #campo de entrada do cnpj
    entry_cnpj = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_cnpj.grid(row=3,column =1)


    #label do email
    label_email = customtkinter.CTkLabel(master=janela,text="E-mail:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_email.grid(padx=0.5, pady=0.5,row=4,column =0)

    #campo de entrada do email
    entry_email = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_email.grid(row=4,column =1)

    #label do celular
    label_celular = customtkinter.CTkLabel(master=janela,text="Celular:",fg_color="black",
                                        bg_color="black",text_color="white",width=60)
    label_celular.grid(padx=0.5, pady=0.5,row=5,column =0)

    #campo de entrada do celular
    entry_celular = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_celular.grid(row=5,column =1)


    #label do endereço
    label_endereco = customtkinter.CTkLabel(master=janela,text="Endereço:",fg_color="black",
                                        bg_color="black",text_color="white",width=80)
    label_endereco.grid(padx=0.5, pady=0.5,row=6,column =0)

    #campo de entrada do endereço
    entry_endereco = customtkinter.CTkEntry(master=janela,
                                width=250,
                                height=25,
                                corner_radius=10,fg_color="gray" ,bg_color="black")
    entry_endereco.grid(row=6,column =1)

#   botão para alteração de fornecedor
    button_cadastrar = customtkinter.CTkButton(master=janela,text="Alterar",bg_color="black",command=alterar_fornecedor)
    button_cadastrar.grid(padx=0.5, pady=0.5,row=7,column =0,columnspan=2)


    centralizar_janela(janela)
    janela.mainloop()
if __name__ =="__main__":
    main()