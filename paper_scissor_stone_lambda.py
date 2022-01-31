#paper_scissor_stone_lambda.py
import json
import random






moves = ['paper', 'scissors','stone']



victor = {  
    'stone':'paper',
    'paper':'scissors',
    'scissors':'stone'
}


def winner(player_1_move, player_2_move):
    """
        >>> winner('stone','paper')
        'paper'
        >>> winner('paper','stone')
        'paper'
        >>> winner('stone','scissors')
        'stone'
    """
    if player_1_move == victor[player_2_move]:
        return player_1_move
    elif player_2_move == victor[player_1_move]:
        return player_2_move
    else:
        return None


def get_json_move(event):
    body = event['body']
    move = json.loads(body)['move']
    
    return move
    

def clean_input(move):
    """
        >>>clean_input(' Stone ')
        stone
        >>>clean_input(' STONE ')
        stone
        >>>clean_input('FOO')
        'FOO' is not a valid move        
    """    
    move = move.strip().lower()

    if move not in moves:
        raise ValueError(f"'{move}' is not a valid move")
    
    return move


def get_move(event):
    return clean_input(get_json_move(event))


def play_round(player_move):
    opponent_move = random.choice(moves)
    winning_move = winner(player_move, opponent_move)
    
    if winning_move == player_move:
        return f'{player_move} beats {opponent_move}: YOU WIN!'
    elif winning_move == opponent_move:
        return f'{opponent_move} beats {player_move}: YOU LOSE!'
    else:
        return f'both played {player_move}: REMATCH!'


def play(event):
    player_move = get_move(event)
    return play_round(player_move)


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(play(event))
    }


