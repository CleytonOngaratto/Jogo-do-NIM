import random

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")
    
    option = int(input())
    
    if option == 1:
        play_game(1)
    elif option == 2:
        play_game(3)
    else:
        print("Opção inválida. Tente novamente.")
        main()
        
def play_game(rounds):
    player_score = 0
    computer_score = 0
    
    for i in range(1, rounds+1):
        print(f"**** Rodada {i} ****\n")
        
        number_of_pieces = int(input("Quantas peças? "))
        max_remove = int(input("Limite de peças por jogada? "))
        
        if number_of_pieces % (max_remove + 1) == 0:
            print("Você começa!\n")
            current_player = "player"
        else:
            print("Computador começa!\n")
            current_player = "computer"
        
        while number_of_pieces > 0:
            if current_player == "player":
                print("Sua vez!\n")
                player_choice = get_player_choice(number_of_pieces, max_remove)
                number_of_pieces -= player_choice
                print(f"Agora restam {number_of_pieces} peças no tabuleiro.\n")
                
                if number_of_pieces == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    player_score += 1
                else:
                    current_player = "computer"
            else:
                print("Vez do computador!\n")
                computer_choice = get_computer_choice(number_of_pieces, max_remove)
                number_of_pieces -= computer_choice
                print(f"O computador tirou {computer_choice} peça(s).\n")
                print(f"Agora restam {number_of_pieces} peças no tabuleiro.\n")
                
                if number_of_pieces == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    computer_score += 1
                else:
                    current_player = "player"
                    
        print(f"**** Placar: Você {player_score} X {computer_score} Computador ****\n")
        
    if player_score > computer_score:
        print("**** Você ganhou o campeonato! ****")
    elif player_score < computer_score:
        print("**** O computador ganhou o campeonato! ****")
    else:
        print("**** O campeonato terminou empatado! ****")
        
def get_player_choice(number_of_pieces, max_remove):
    player_choice = int(input("Quantas peças você vai tirar? "))
    
    if player_choice > max_remove or player_choice < 1 or player_choice > number_of_pieces:
        print("Oops! Jogada inválida! Tente de novo.\n")
        player_choice = get_player_choice(number_of_pieces, max_remove)
        
    return player_choice
    
def get_computer_choice(number_of_pieces, max_remove):
    computer_choice = random.randint(1, max_remove)
    
    while computer_choice > number_of_pieces or computer_choice > max_remove:
        computer_choice = random.randint(1, max_remove)
        
    return computer_choice

if __name__ == "__main__":
    main()
