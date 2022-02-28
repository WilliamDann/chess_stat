# William Dann
# Piece Relative Value Score

import chess
import chess.pgn

from sys import argv

def process_games(file):
    while True:
        game = chess.pgn.read_game(file)
        if game is None:
            break

        process_game(game)

def process_game(game: chess.Game):
    pass

if __name__ == '__main__':
    if len(argv) != 2:
        print('usage:')
        print('python piece_relative_value.py [input_games.pgn]')

    process_games(open(argv[1]))
    
