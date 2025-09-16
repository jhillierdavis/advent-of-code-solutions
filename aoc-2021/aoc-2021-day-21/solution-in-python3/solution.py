# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from collections import defaultdict


def switch_player(current_player):
    return 1 if current_player == 0 else 0


def get_new_position(player_position, round_die_score):
    new_position = player_position + round_die_score
    new_position = new_position % 10
    if 0 == new_position:
        new_position = 10    
    return new_position


def solve_part1(starting_positions):
    ans = 0
    player_positions = list(starting_positions)
    player_scores = [0,0]
    current_player = 0
    round_score = 0
    for i in range(1, 10000):
        round_score += i

        if i % 3 == 0:
            new_position = get_new_position(player_positions[current_player], round_score)
                
            player_positions[current_player] = new_position                
            player_scores[current_player] += new_position            
            logger.debug(f"Player {current_player + 1} round_score={round_score} postion={player_positions[current_player]} score={player_scores[current_player]}")            

            if player_scores[current_player] >= 1000:
                logger.debug(f"Winner! i={i} current_player={1+current_player} score={player_scores[current_player]}")
                losing_player = switch_player(current_player)
                ans = player_scores[losing_player] * i 
                break

            current_player = switch_player(current_player)
            round_score = 0

    return ans

def get_quantum_die_score_distribution():
    score_distribution = defaultdict(int)
    
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                current_sum = i+j+k
                #logger.debug(f"{i}+{j}+{k}={current_sum}")
                score_distribution[current_sum] = 1 + score_distribution[current_sum] 
                current_sum = 0
                
    #logger.debug(f"score_distribution={score_distribution} rolls={sum(score_distribution.values())}")
    return score_distribution


def calculate_wins(memoization, score_distribution, current_player, player_positions, player_scores, player_wins, paths):
    next_player = switch_player(current_player)

    for k, v in score_distribution.items():
        current_positions = list(player_positions)
        current_scores = list(player_scores)

        new_position = get_new_position(current_positions[current_player], k)
        current_positions[current_player] = new_position                
        current_scores[current_player] += new_position            

        current_key = current_player, current_positions[0], current_positions[1], current_scores[0], current_scores[1]
        current_universe_paths = v * paths
        if current_scores[current_player] >= 21:
            player_wins[current_player] += current_universe_paths
            memoization[current_key] = player_wins
        else:
            if (current_key) in memoization:
                cached_wins = memoization[current_key]
                player_wins[current_player] += cached_wins[current_player]
            else:
                calculate_wins(memoization, score_distribution, next_player, current_positions, current_scores, player_wins, current_universe_paths)
    


def solve_part2(starting_positions):
    score_distribution = get_quantum_die_score_distribution() # {3:1,4:3,5:6,6:7,7:6,8:3,9:1}
    player_wins = [0,0]

    memoization = dict()
    calculate_wins(memoization, score_distribution, 0, starting_positions, [0, 0], player_wins, 1)
    
    logger.debug(f"player_wins={player_wins}")
    return max(player_wins)
