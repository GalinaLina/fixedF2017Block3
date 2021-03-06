####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Vindict-c' # Only 10 chars displayed.
strategy_name = 'Benevolent Vindictive'
strategy_description = 'Benevolent Vindictive'
    
def move(my_history, their_history, my_score, their_score):
    #collude on the first turn
    if len(their_history)==0:
      return 'c'
    #betray if opponent has ever betrayed previously
    elif 'b' in their_history[-1]:
      return 'b'
    #collude if opponent has never betrayed
    else:
      return 'c'