# the winning play needs to win two out of three rounds
# the players can choose between scissor, paper or rock
# results: 0 = tie; 1 = player_one wins; 2 = player_two wins


round_one = -1
round_two = -1
round_three = -1

#victory_player_one =
#victory_player_two =

for turn in range(3):
    player_one = input("Rock paper scissor: ")
    player_two = input("Rock paper scissor: ")

    result = -1
    if player_one == "rock" and player_two == "rock":
        print("Tie!")
        result = 0

    elif player_one == "scissor" and player_two == "scissor":
        print("Tie!")
        result = 0

    elif player_one == "paper" and player_two == "paper":
        print("Tie!")
        result = 0

    elif player_one == "scissor" and player_two == "paper":
        print("Player one get a point!")
        result = 1

    elif player_one == "scissor" and player_two == "rock":
        print("Player two get a point!")
        result = 2

    elif player_one == "paper" and player_two == "scissor":
        print("Player two get a point!")
        result = 2

    elif player_one == "paper" and player_two == "rock":
        print("Player one get a point!")
        result = 1

    elif player_one == "rock" and player_two == "scissor":
        print("Player one get a point!")
        result = 1

    elif player_one == "rock" and player_two == "paper":
        print("Player two get a point!")
        result = 2

    if turn == 0:
        round_one = result
    elif turn == 1:
        round_two = result
    elif turn == 2:
        round_three = result

# criar variáveis de vitória para cada player
# incrementar o contador de vitórias para cada player baseado no valor dos rounds
# descobrir qual player é o vitorioso comparando os contadores de vitória


if round_one == 0:
    print("Player one and two get a point!")
elif round_two == 1:
    print("Player one get a point!")
elif round_three == 2:
    print("Player two get a point!")