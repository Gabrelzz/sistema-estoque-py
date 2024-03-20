import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("600x400")
janela.title("App Estoque")
janela.minsize(width =600, height =400)
janela.maxsize(width =900, height =550)

texto = customtkinter.CTkLabel(janela, text="Menu Principal")
texto.pack(padx=50, pady=50)

registrar = customtkinter.CTkButton(janela, text="Registrar-se")
registrar.pack(padx=30, pady=10)


logar = customtkinter.CTkButton(janela, text="Logar-se")
logar.pack(padx=30, pady=10)

janela.mainloop()