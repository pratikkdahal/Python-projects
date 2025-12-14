import random  #random libraries access garna


def get_choices():
  
  player_choice = input("Enter a choice(rock,paper,scissors):")
  options = ["rock","paper","scissors"]  #option vanne list banako
  computer_choice = random.choice(options)  #random.choice() is a function in the random module that returns a random element from a non-empty sequence (list, tuple, string)

  choices = {"player":player_choice , "computer":computer_choice} #yo choices vanne chai dictionary ho
  return choices

def check_win(player, computer):
  
  #print( "You chose " + player + ", Computer chose " + computer)
  #using f string---- f strings is used to concatenate variables and the strings together

  print(f"You chose {player}, Computer chose {computer}")
  
  if player == computer:
    return "Oops! It's a tie"
  
  elif player=="rock":
   
   if computer=="scissors":
    return "Yayyy, Rock smashes Scissors, You win!"
   else:
    return "Paper covers Rock, You lose!"
  
  
  elif player=="paper":
   
   if computer=="scissors":
    return "Oops, Scissors cuts Paper, You lose!"
   else:
    return "Paper covers Rock, You win!"
   
choices = get_choices()
result = check_win(choices["player"],choices["computer"])

print(result)
  

  

