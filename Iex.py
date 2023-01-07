handle_player_move()

handle_computer_move()


game_is_over() # returns True if it's the end of game False other wise


whos_move = 0   # number of player ( 0 or 1 )
while not game_is_over():
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_player_move(player2)
     whos_move = (whos_move + 1) % 2


whos_move = 0   # number of player ( 0 or 1 )
while not game_is_over():
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_computer_move(player2)
     whos_move = (whos_move + 1) % 2


whos_move = 0   # number of player ( 0 or 1 )
while game_still_going:
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_computer_move(player2)
     whos_move = (whos_move + 1) % 2
     check_if_game_over()
     if statement:  # your ending statement here
         game_is_still_going = False


import random
random.randint(1,9) # choose integer x such that: 1 <= x <= 9



handle_player_move()

handle_computer_move()


game_is_over() # returns True if it's the end of game False other wise


whos_move = 0   # number of player ( 0 or 1 )
while not game_is_over():
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_player_move(player2)
     whos_move = (whos_move + 1) % 2


whos_move = 0   # number of player ( 0 or 1 )
while not game_is_over():
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_computer_move(player2)
     whos_move = (whos_move + 1) % 2


whos_move = 0   # number of player ( 0 or 1 )
while game_still_going:
     if whos_move == 0:
         handle_player_move(player1)
     if whos_move == 1:
         handle_computer_move(player2)
     whos_move = (whos_move + 1) % 2
     check_if_game_over()
     if statement:  # your ending statement here
         game_is_still_going = False


import random
random.randint(1,9) # choose integer x such that: 1 <= x <= 9







