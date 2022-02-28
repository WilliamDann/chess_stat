# William Dann
#   Find all the games where a piece ends up on a strange square
#
#   Output is intended to be piped to a file
#   ex:
#   $ python oddity_search.py input_games.pgn histo_file.json > generated/oddity_search.pgn
# 

## TODO implement threshold instead of just average

import io
import sys
import chess 
import chess.pgn

from common_piece_squares import load_data

def load_games(pgn_file):
    games = []

    with open(pgn_file, 'r') as f:
        games =  ['[Event '+pgn for pgn in f.read().split('[Event ') if pgn]

    if games[0] == '':
        games.pop(0)

    return games

def search(games, histo, threshold=0.5):
    commented  = []
    avgs       = {True: {}, False: {}}
    for k, v in histo[True].items():
        avgs[True][k] = sum(v) / len(v)
    for k, v in histo[False].items():
        avgs[False][k] = sum(v) / len(v)

    for game in games:
        game_data = chess.pgn.read_game(io.StringIO(game))
        board     = chess.Board()

        for move in game_data.mainline():
            piece = board.piece_at(move.move.from_square)
            board.push_uci(str(move.move))

            average   = avgs[piece.color][piece.piece_type]
            histo_val = histo[piece.color][piece.piece_type][move.move.to_square]

            if histo_val < average:
                move.comment = 'oddity'

        commented.append(str(game_data))

    return commented

if __name__ == '__main__':
    if len(sys.argv) < 3 or '--help' in sys.argv:
        print('find all games where a piece ends up in a strange place')
        print('  command: python search.py [input_games_pgn] [histogram_data_file] [threshold=0.5]')
        quit()

    games_data = load_games(sys.argv[1])
    histo_data = load_data(sys.argv[2])

    threshold = 0
    if len(sys.argv) < 5:
        threshold = 0.50
    else:
        threshold = float(sys.argv[3])

    for game in search(games_data, histo_data, threshold):
        print(game)
        print()
        print()