from math   import floor
from .Piece import PieceType, Color

FEN_TO_PIECE = {
    'P' : PieceType.Pawn   + Color.White,
    'N' : PieceType.Night  + Color.White,
    'B' : PieceType.Bishop + Color.White,
    'R' : PieceType.Rook   + Color.White,
    'Q' : PieceType.Queen  + Color.White,
    'K' : PieceType.King   + Color.White,

    'p' : PieceType.Pawn   + Color.Black,
    'n' : PieceType.Night  + Color.Black,
    'b' : PieceType.Bishop + Color.Black,
    'r' : PieceType.Rook   + Color.Black,
    'q' : PieceType.Queen  + Color.Black,
    'k' : PieceType.King   + Color.Black,
    '-' : -1
}
PIECE_TO_FEN = {v: k for k, v in FEN_TO_PIECE.items()}

class Board:
    def __init__(self):
        self.board = [-1]*144

    def __getitem__(self, index):
        return self.board[index]
    def __setitem__(self, index: int, value):
        self.board[index] = value
    def __delitem__(self, index: int):
        self.board[index].__delitem__(self, index)  
    def __str__(self):
        s = ""
        
        for i in range(len(self.board)):
            if self.board[i] == 0:
                s += '_ '
            else:
                if self.board[i] not in PIECE_TO_FEN:
                    s += str(self.board[i]) + ' '
                else:
                    s += PIECE_TO_FEN[self.board[i]] + ' '

            if (i+1) % 12 == 0 and i != 0:
                s += '\n'

        return s

    def getBoardCoord(self, sq: int):
        return sq + 26 + (floor(sq/8)*4)

    def loadFEN(self, fen: str):
        rows = fen.split('/')
        i    = 0

        for row in rows:
            for char in row:
                if char.isnumeric():
                    for j in range(int(char)):
                        self[self.getBoardCoord(i+j)] = 0
                    i += int(char)
                    continue
                
                if char not in FEN_TO_PIECE:
                    raise Exception('Invalid FEN')

                self[self.getBoardCoord(i)] = FEN_TO_PIECE[char]
                i += 1