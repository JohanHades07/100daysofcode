def determine_winner(player1, player2):
    if player1 ==player2:
        return "Empate!"
    elif (player1 == "rock" and player2 == "scissors" ) or \
          (player1 == "scissors" and player2 == "paper") or \
          (player1 == "paper" and player2 =="rock"):
        return "jugador 1 gana!"
    else:
        return "jugador 2 gana!"    
    
print("EPIC ROCK PAPER AND SCOSSORS")

# primer jugador
player1_move = input("jugador 1, elige el movimiento(rock, paper, scissors):").lower()

# segundo jugador
player2_move = input("jugador 2, elije tu movimiento (rock, paper, scissors):").lower()

# determinar el ganador
result = determine_winner(player1_move, player2_move)
print(result)






