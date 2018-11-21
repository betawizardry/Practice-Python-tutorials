#scissory paper rock game. two players, two inputs.
#scissors beats paper, rock beats scissors, paper beats rock
#take inputs and deliver result, which player wins.
#if same selection, ask for inpus again.
#after result delivered, ask 'would you like to play again?

winner = 'none'
replay = 'y'

while replay == 'y':
    player1 = input('Player 1: scissors, paper or rock?: ')
    player2 = input('Player 2: scissors, paper or rock?: ')
    
    while player1 == player2:
        replaydraw = input('The round is a draw. Would you like to play again?: y/n ')
        if replaydraw == 'y':
            pass
        else:
            break
        player1 = input('Player 1: scissors, paper or rock?: ')
        player2 = input('Player 2: scissors, paper or rock?: ')
    
    if player1 == 'rock':
        if player2 == 'scissors':
            winner = 'Player 1'
        elif player2 == 'paper':
            winner = 'Player 2'
        else:
            pass
        
    if player1 == 'paper':
        if player2 == 'scissors':
            winner = 'Player 2'
        elif player2 == 'rock':
            winner = 'Player 1'
        else:
            pass
        
    if player1 == 'scissors':
        if player2 == 'rock':
            winner = 'Player 2'
        elif player2 == 'paper':
            winner = 'Player 1'
        else:
            pass
    print('The winner is',winner)
    replay = input('would you like to play again?: y/n ')
    
