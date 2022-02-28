## William Dann
##    Creates a heatmap of where pieces are found from pgn game data
##

## TODO implement Histoboard here instead of the old
##      by-hand method

import io
import sys    
import json
import chess
import chess.pgn
import chess.svg

from PIL import Image

GENERATE_NEW_DATA = '--generate' in sys.argv or '-g' in sys.argv

def generate_data(filepath):
    data = init_data()
    with open(filepath, 'r') as data_file:
        single_pgn = ""

        for line in data_file.readlines():
            if '[Event' in line and len(single_pgn) != 0:
                handle_pgn(single_pgn, data)
                single_pgn = ""
            
            single_pgn += line

        handle_pgn(single_pgn, data)

        for piece_type in chess.PIECE_TYPES:
            draw_board(data, piece_type, True).save('data/' + str(piece_type) + '_white_map.png')
            draw_board(data, piece_type, False).save('data/' + str(piece_type) + '_black_map.png')

        with open('data/dump.json', 'w') as f:
            f.write(json.dumps(data))

def load_data(filepath):
    data_temp = {}
    with open(filepath, 'r') as data_file:
        data_temp = json.loads(data_file.read())

    data = {True: {}, False:{} }
    for key in data_temp['true'].keys():
        data[True][int(key)] = data_temp['true'][key]
    for key in data_temp['false'].keys():
        data[False][int(key)] = data_temp['false'][key]

    return data


def draw_board(data, piece, color):
    w, h   = 8, 8
    img    = Image.new("RGB", (w,h))
    pixels = img.load()

    max_num = sum(data[color][piece]) / len(data[color][piece])
    
    for i in range(w):
        for j in range(h):
            board_square = (j * 8) + i

            if data[color][piece][board_square] == 0:
                color_value = 0
            else:
                color_value = (data[color][piece][board_square] / max_num) * 255 / 2
                # color_value = max(color_value, 255)

            pixels[i,j] = (0,0,int(color_value))

    img = img.resize((500*w,500*h), Image.NEAREST)
    return img

def init_data():
    data = { True: {}, False: {}}

    for piece in chess.PIECE_TYPES:
        data[True][piece]  = [0]*64
        data[False][piece] = [0]*64

    return data

def handle_pgn(pgn_data, data):
    game_data = chess.pgn.read_game(io.StringIO(pgn_data))

    board = chess.Board()
    for move in game_data.mainline_moves():
        piece = board.piece_at(move.from_square)
        
        data[piece.color][piece.piece_type][move.from_square] += 1    
        board.push(move)


if __name__ == "__main__":
    generate_data(sys.argv[1])
    