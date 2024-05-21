import tkinter
from tkinter import ttk
import sqlite3

def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2 - 100
    y = (altura_tela - altura_janela) // 3

    janela.geometry(f"+{x}+{y}")  

def ajustar_colunas(treeview):
    total_largura = treeview.winfo_width()
    num_colunas = len(treeview["columns"])
    largura_coluna = total_largura // num_colunas

    for coluna in treeview["columns"]:
        treeview.column(coluna, width=largura_coluna)

def main():
    janela = tkinter.Tk()
    janela.geometry("600x400")
    janela.title("Histórico do estoque")
    janela.minsize(width=600, height=400)
    janela.maxsize(width=600, height=400)
    
    # Configurar cores da janela
    janela.configure(bg='black')

    frame = tkinter.Frame(master=janela, width=600, height=400, bg='white')
    frame.pack(fill=tkinter.BOTH, expand=True)

    # Cabeçalhos das colunas
    colunas = ("ID", "Nome", "Quantidade", "Preço_compra", "Preço_venda", "Id_Fornecedor", "Descrição")

    # Criar o Treeview
    treeview = ttk.Treeview(master=frame, columns=colunas, show="headings", style="Treeview")
    treeview.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    # Adicionar Scrollbar vertical
    scrollbar_y = tkinter.Scrollbar(master=frame, orient=tkinter.VERTICAL, command=treeview.yview, bg='black')
    scrollbar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    treeview.configure(yscroll=scrollbar_y.set)

    # Adicionar Scrollbar horizontal
    scrollbar_x = tkinter.Scrollbar(master=frame, orient=tkinter.HORIZONTAL, command=treeview.xview, bg='black')
    scrollbar_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    treeview.configure(xscroll=scrollbar_x.set)
    
 # Configurar os cabeçalhos das colunas
    for coluna in colunas:
        treeview.heading(coluna, text=coluna)

    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    # Limpar a tabela antes de preenchê-la novamente
    for i in treeview.get_children():
        treeview.delete(i)

    for produto in produtos:
        treeview.insert('', 'end', values=produto)

    conn.close()

    # Centralizar janela
    centralizar_janela(janela)

    # Ajustar colunas após a janela ser carregada
    janela.after(100, ajustar_colunas, treeview)

    # Reajustar as colunas quando a janela for redimensionada
    janela.bind("<Configure>", lambda event: ajustar_colunas(treeview))

    janela.mainloop()

if __name__ == "__main__":
    main()
