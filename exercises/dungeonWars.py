print("Welcome to the game Dungeon Wars\n")

characters = {
    "knight": {
        "name": "Gerald"
    },
    "mage": {
        "name": "Merlin"
    },
    "archer": {
        "name": "Robin Hood"

    }

}


# def select_two(characters):
#     selection = input("Enter hero: ")
#     if selection != "mage":
#         print("Invalid input")
#     else:
#         hero = characters[selection]
#         return hero

# player_choice = select_two(characters)
# print(player_choice)


def select_hero(characters):
    while True:
        user_hero_choice = input("Enter a hero: ")
        if user_hero_choice == "knight" or user_hero_choice == "mage" or user_hero_choice == "archer":
            print("Hero choosen", user_hero_choice)
            hero = characters[user_hero_choice]
            return hero
        else:
            print("Invalid choice")


# realizar escolha do herói
hero = select_hero(characters)
print(hero)

# [LOOP] sortear o inimigo do turno
# def select_enemy(enemy):
# for x in range(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5)


# current_enemy =

# solicitar ação do jogador
# playerAction = requestUserAction()

# executar ação do jogador

# SE FUGIR
## verificar se pode fugir
## descontar vida
## testar sucesso da fuga
## SE FUGIU, reinicia [LOOP]
## SE NAO FUGIU, segue na execução da ação do inimigo

# SE ATACAR
## calcula dano do ataque
## verifica se dano é válido

## SE DANO NÃO FOR VÁLIDO
### printa dano inválido
### segue na execução da ação do inimigo

## SE DANO FOR VÁLIDO
### desconta dano da vida do inimigo
### verifica se inimigo foi derrotado
### SE INIMIGO DERROTADO, finaliza turno (executando ações de fim de turno)
### SE INIMIGO NÃO DERROTADO, segue na execução da ação do inimigo

# executar ação do inimigo
# testar fim de jogo
# reiniciar a partir de [LOOP] (se for o caso)


# def com input do user para a escolha do personagem

# def para o sorteio do inimigo, cinco opções possíveis para os dez turnos

# def para ação do user que pode ser: fugir ou atacar

# se for FUGIR
# def para devificar se pode fugir, se tem vida
# SE NÂO
# volta para a ação do user em que ele só poderá ATACAR
# SE SIM
# def para descontar a vida do turno que fugir --> precisa ter um contador para atualizar a vida gasta ao fugir e tbm a vida ganha quando recupera (juntar os dois para salvar na variável vida)
# def para fazer o sorteio se pode ou não fugir dentro dos 40% de chance que o user tem de chances para fuguir
# se conseguir fugir volta para o sorteio do inimigo e se não conseguir print("Não pode fugir") e volta para a ação do user em que ele só poderá ATACAR

# se for ATACAR
# def para o ataque em que será calculado o ataque_base e a defesa_base
# retorna com o dano
# def para verificar se dano é válido
# SE DANO > 0
# def para descontar da vida do inimigo
# SE DANO < 0
# print("Ataque sem efeito")
# def para verificar se inimigo foi derrotado
# retorna se inimigo foi derrotado após o dano
# SE SIM
# def para verificar se é o último turno
# SE SIM
# print("Final do jogo? Você venceu!")
# SE NÂO
# def para contabilizar os 50% de vida ganho pelo user
# def para incrementar o turno
# volta para o sorteio do inimigo
# SE NÂO
# def para o ataque do inimigo
# verificar o dano causado pelo inimigo no user
# SE DANO > 0
# def para descontar da vida do user
# def para verificar se user foi derrotado
# SE SIM
# print("Game over!")
# SE NÂO
# volta para ação do user
# SE DANO < 0
# print("Ataque sem efeito")
# volta para ação do user
