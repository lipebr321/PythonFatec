agenda = {}

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado.")

def alterar():
    nome = input("Nome do contato para alterar: ")
    if nome in agenda:
        telefone = input("Novo telefone: ")
        agenda[nome] = telefone
        print("Contato alterado.")
    else:
        print("Contato não encontrado.")

def consultar():
    nome = input("Nome do contato para consultar: ")
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def excluir():
    nome = input("Nome do contato para excluir: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato excluído.")
    else:
        print("Contato não encontrado.")

def listar():
    if agenda:
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    else:
        print("Agenda vazia.")


while True:
    opcao = input("\n1. Adicionar 2. Alterar 3. Consultar 4. Excluir 5. Listar 6. Sair\nEscolha: ")
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        alterar()
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        listar()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

