import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")



janela = ctk.CTk()
janela.geometry("600x400")
janela.title("App Estoque")
janela.minsize(width =600, height =400)
janela.maxsize(width =900, height =550)
janela.iconbitmap(default="icons/python.ico")

#-------------------------------------------

def nova_janela_registro():
    nova_janela = ctk.CTk()
    #nova_janela = ctk.CTkToplevel(nova_janela)
    nova_janela.geometry("900x500")
    nova_janela.minsize(width =900, height =550)
    nova_janela.maxsize(width =900, height =550)
    nova_janela.resizable(width=False, height=False)

    texto = ctk.CTkLabel(janela, text="Cadastrar-se")
    texto.pack(padx=10, pady=10)

    nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome completo")
    nome.pack(padx=10, pady=10)

    usuario = ctk.CTkEntry(janela, placeholder_text="Digite seu usuário")
    usuario.pack(padx=10, pady=10)

    email = ctk.CTkEntry(janela, placeholder_text="Digite seu email")
    email.pack(padx=10, pady=10)

    senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
    senha.pack(padx=10, pady=10)

    confirmarSenha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha novamente", show="*")
    senha.pack(padx=10, pady=10)



#-------------------------------------------
texto = ctk.CTkLabel(janela, text="Menu Principal", font=("arial bold", 20))
texto.pack(padx=50, pady=50)

registrar = ctk.CTkButton(janela, text="Registrar-se", command=nova_janela_registro)
registrar.pack(padx=30, pady=10)


logar = ctk.CTkButton(janela, text="Logar-se")
logar.pack(padx=30, pady=10)

janela.mainloop()