senha = "123"
usr = "Lucas"
for i in range(3):
    usuario = input("Digite seu usuario: ")
    usenha = input("Digite sua senha: ")
    if usuario == usr and usenha == senha:
       print("logado com sucesso")
       break
    else:
        print(f"Acesso negado, voce tem {2 - i} tentativas")

