import random

random_play = random.randint(1,3)


def computer_play():
        
    if random_play == 1:
        return("Tesoura")
    elif random_play == 2:
         return("Pedra")
    else:
        return("Papel")

jogada_computador =  computer_play()



def game_round():
    print("Escolha entre Papel, pedra e tesoura: ")
    player_choice = input()
    if player_choice == "Pedra" and jogada_computador == "Papel":
        return("Você perdeu!")
    elif player_choice == "Tesoura" and jogada_computador == "Pedra":
        return("Você perdeu!")
    elif player_choice == "Papel" and jogada_computador == "Tesoura":
        return("Você perdeu!")
    elif player_choice == "Pedra" and jogada_computador == "Tesoura":
        return("Você venceu")
    elif player_choice == "Tesoura" and jogada_computador == "Papel":
        return("Você Venceu!")
    elif player_choice == "Papel" and jogada_computador == "Pedra":
        return("Você Venceu!")
    else:
        return("Empate!")



i = 0
while i < 3:
    print(game_round())
    i += 1
