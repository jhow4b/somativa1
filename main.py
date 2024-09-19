def jogar():
    print("Selecione uma opção:")
    print("1- Atacar")
    print("2- Bolsa de itens")
    print("3- Fugir")
    escolha = int(input("Qual a sua escolha meu camarada? "))
    match escolha:
        case 1:
            result = "Atacou"
        case 2:
            result = "Abriu sua bolsa de itens"
        case 3:
            result = "Fugiu"
        case _:
            result = "Opção invalida"
    print(result)

jogar()