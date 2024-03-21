'''import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#janela = customtkinter.CTk()
janela.geometry("600x400")
janela.title("App Estoque")
janela.minsize(width =600, height =400)
janela.maxsize(width =900, height =550)

#MENU PRINCIPAL
texto = customtkinter.CTkLabel(janela, text="Estoque")
texto.pack(padx=10, pady=10)

usuario = customtkinter.CTkEntry(janela, placeholder_text="Digite seu usuário")
usuario.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx= 10, pady=10)

#Abrir nova janela

def nova_janela():
    nova_janela = ctk.CTkTopLevel(janela)
    nova_janela.geometry("600x400")
    
#se o usuario e a senha for igual no banco de dados -> executar botao
botao = customtkinter.CTkButton(janela, text="Entrar")
botao.pack(padx=50, pady=50)



janela.mainloop()
