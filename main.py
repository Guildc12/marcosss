def tratamento():
    txt = open("marcos.txt", "r")
    tratar = txt.read()
    txt.close()
    abc = tratar.split("\n")
    final = list()
    add = list()
    for a in abc:
        if "!" in a:
            add.append(a[1:])
        elif "#" in a:
            add.append(a[1:])
        elif "$" in a:
            add.append(a[1:])
            final.append(add)
            add = list()
    return final


def registrar(banco):
    dataw = open("marcos.txt", "a")
    controle = True
    while True:
        produto = input("Qual é o produto? ---> ")
        qnt = input("Quantidade? ---> ")
        idd = input("Id do produto? --- >")

        for elementos in banco:
            if elementos[0] == produto:
                controle = False
            elif elementos[2] == idd:
                controle = False

        if controle == True and not "!" in produto and not "#" in produto and not "$" in produto and not "!" in qnt and not "#" in qnt and not "$" in qnt and not "!" in idd and not "#" in idd and not "$" in idd and not "\\" in produto and not "\\" in idd and not "//" in qnt:
            if qnt.isnumeric():
                dataw.write(f'!{produto}\n'
                            f'#{qnt}\n'
                            f'${idd}\n\n')
                dataw.close()
                break
            else:
                print("A quantia deve ser um valor numerico!")
                continue
        else:
            print("Produto já registrado ou inválido.")
            continue


def mudar(banco):
    ver = input("Qual produto que você quer mudar? nome // id---> ")
    for a in banco:
        if a[0] == ver or a[2] == ver:
            qnt = input(f"Nova quantia ({a[0]}) ---> ")
            a[1] = qnt
            break
    dta = open("marcos.txt", "w")
    for ele in banco:
        dta.write(f'!{ele[0]}\n#{ele[1]}\n${ele[2]}\n\n')
    dta.close()


def visualizar(banco):
    vis = input("Qual produto que você quer analisar? nome // id---> ")
    for a in banco:
        if a[0] == vis or a[2] == vis:
            print(f"O produto {a[0]} tem {a[1]} exemplares e seu id é: {a[2]}!")
            break


def deletar(banco):
    vis = input("Qual produto que você quer eliminar? nome // id---> ")
    for b, a in enumerate(banco):
        if a[0] == vis or a[2] == vis:
            print("Deletando")
            del banco[b]
            print("Deletado!")
            break

    data_delete = open("marcos.txt", "w")
    for ele in banco:
        data_delete.write(f'!{ele[0]}\n#{ele[1]}\n${ele[2]}\n\n')
    data_delete.close()


while True:
    print("-="*30)
    dt = tratamento()
    for quantia in dt:
        num = int(quantia[1])
        if num <= 3:
            print(f"O produto {quantia[0]} tem apenas {num} exemplares!")

    querer = input("Registrar (1) // Visualizar (2) // Mudar (3) // Deletar (4) // Sair (5)\n---> ")

    if querer == "1":
        registrar(dt)
    if querer == "2":
        visualizar(dt)
    if querer == "3":
        mudar(dt)
    if querer == "4":
        deletar(dt)
    if querer == "5":
        break
