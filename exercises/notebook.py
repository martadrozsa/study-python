def createNote(notes):
    newNote = input("Digite a sua nota. > ")
    notes.append(newNote)


def listNotes(notes):
    print("######################")
    for notePosition, note in enumerate(notes):
        print(f"({notePosition}) - {note}")
    print("######################")


def deleteNote(notes):
    notePositionText = input("Qual a posição da nota que você deseja deletar? > ")
    notePosition = int(notePositionText)
    notes.pop(notePosition)


def updateNote(notes):
    notePositionText = input("Qual a posição da nota que você deseja alterar? > ")
    notePosition = int(notePositionText)

    newNote = input("Digite a sua nota. > ")
    notes[notePosition] = newNote


# base de notas
notes = ["Nota numero 1", "Nota numero 2", "Nota numero 3",
         "Nota numero 4"]

# mostrar boas vindas
print("\n\nBem vindo ao Notebook da Marta e do Vitor!")

while (True):
    # mostrar opcoes de comandos
    print("\nVocê pode [criar], [listar], [deletar] e [alterar] as notas. Você também pode [sair].\n")

    # ler acao do usuario
    userCmd = input("o que voce deseja fazer? > ")

    if userCmd == "criar":
        createNote(notes)

    elif userCmd == "listar":
        listNotes(notes)

    elif userCmd == "deletar":
        deleteNote(notes)

    elif userCmd == "alterar":
        updateNote(notes)

    # checar se eh comando de saida (se sim, sair)
    elif userCmd == "sair":
        break

    # checar se acao e valida (se nao for valida exibir erro)
    else:
        print("Esse comando não é válido! ", userCmd)

    # exibir mensagem de sucesso do comando
    print("Comando executado com sucesso! ", userCmd)

# TODO
# adicionar mensagemde agradecimento/saida

# corrigir bug no qual printa comando invalido e ainda assim comando executado com sucesso.
