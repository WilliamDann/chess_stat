from typing      import List
from Chess.Board import Board
from math        import pi

def slider(board: Board, start: int, step: int) -> List[int]:
    mv = []

    for sq in range(start, 144, step):
        if board[sq] == -1:
            break
        mv.append(sq)

    for sq in range(start, 0, -step):
        if board[sq] == -1:
            break
        mv.append(sq)

    return mv

def knight_psuedo(board: Board, start: int) -> List[int]:
    mv = [
        start - 24 + 1,
        start - 12 + 2,

        start + 12 + 2,
        start + 24 + 1,

        start - 24 - 1,
        start - 12 - 2,

        start + 12 - 2,
        start + 24 - 1
    ]

    return list(filter(lambda sq: board[sq] != -1, mv))

def rook_psuedo(board: Board, sq: int):
    return slider(board, sq, 1)+slider(board, sq, 12)
def bishop_psuedo(board: Board, sq: int):
    return slider(board, sq, 13)+slider(board, sq, 11)
def queen_psuedo(board: Board, sq: int):
    return rook_psuedo(board, sq)+bishop_psuedo(board, sq)