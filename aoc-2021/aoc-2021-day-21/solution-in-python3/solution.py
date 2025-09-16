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


def solve_part1(starting_positions):
    #logger.debug("TODO: Implement Part 1")
    #lines = fileutils.get_file_lines_from(filename)

    ans = 0
    player_positions = list(starting_positions)
    player_scores = [0,0]
    current_player = 0
    round_score = 0
    for i in range(1, 10000):
        round_score += i

        if i % 3 == 0:
            new_position = player_positions[current_player] + round_score
            new_position = new_position % 10
            if 0 == new_position:
                new_position = 10
                
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


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    #lines = fileutils.get_file_lines_from(filename)

    # Exploration
    score_distribution = defaultdict(int)
    
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                current_sum = i+j+k
                logger.debug(f"{i}+{j}+{k}={current_sum}")
                score_distribution[current_sum] = 1 + score_distribution[current_sum] 
                current_sum = 0
                
    logger.debug(f"score_distribution={score_distribution} rolls={sum(score_distribution.values())}")
    return "TODO"
