import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


janela = ctk.CTk()
janela.geometry("600x400")
janela.title("App Estoque")
janela.minsize(width =600, height =400)
#janela.maxsize(width =900, height =550)
janela.iconbitmap(default="icons/python.ico")


tituloMenu = ctk.CTkLabel(janela, text="Menu Principal", font=("arial bold", 20))
tituloMenu.pack(padx=50, pady=50)

logarBotao = ctk.CTkButton(janela, text="Logar-se")
logarBotao.pack(padx=30, pady=10)

#-------------------------------------------

def nova_janela_registro():

    #Removendo opções de login
    logarBotao.place(x=5000)
    registrarBotao.place(x=5000)
    tituloMenu.place(x=5000)

    janela.geometry("950x630")
    #Inserindo botões de registros
    texto = ctk.CTkLabel(janela, text="Cadastrar-se", font=("arial bold", 20))
    texto.pack(padx=10, pady=55)

    nomeLabel= ctk.CTkLabel(janela, text= "Nome:" )
    #nomeLabel.place(x = 345, y = 135)
    nomeLabel.pack()
    nomeEntry = ctk.CTkEntry(janela, placeholder_text="Digite seu nome completo", width=270)
    nomeEntry.pack()

    usuarioLabel = ctk.CTkLabel(janela, text="Usuário:")
    usuarioLabel.pack()
    usuarioEntry = ctk.CTkEntry(janela, placeholder_text="Digite seu usuário", width=270)
    usuarioEntry.pack()

    emailLabel = ctk.CTkLabel(janela, text="Email:")
    emailLabel.pack()
    emailEntry = ctk.CTkEntry(janela, placeholder_text="Digite seu email", width=270)
    emailEntry.pack()

    senhaLabel = ctk.CTkLabel(janela, text="Senha:")
    senhaLabel.pack()
    senhaEntry = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", width=270, show="*")
    senhaEntry.pack()

    confirmarSenhaLabel = ctk.CTkLabel(janela, text="Confirmar senha:")
    confirmarSenhaLabel.pack()
    confirmarSenhaEntry = ctk.CTkEntry(janela, placeholder_text="Digite sua senha novamente", width=270, show="*")
    confirmarSenhaEntry.pack()
    
    cadastrarBotão = ctk.CTkButton(janela, text="Cadastrar", width=100)
    cadastrarBotão.place(x = 422, y = 450)
    voltarBotão = ctk.CTkButton(janela, text="Voltar", width=70)
    voltarBotão.place(x=435, y=500)

#-------------------------------------------

registrarBotao = ctk.CTkButton(janela, text="Registrar-se", command=nova_janela_registro)
registrarBotao.pack(padx=30, pady=10)

janela.mainloop()