team_name = 'IDK' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 11:
        return "c"
    elif "b" in their_history[0:11]:
        return "b"
    
    else:
        return "c"
    
    

    
