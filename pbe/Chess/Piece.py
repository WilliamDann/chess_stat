class Color:
    White = 0b0000
    Black = 0b1000

class PieceType:
    Pawn   = 0b001
    Night  = 0b010
    Bishop = 0b011
    Rook   = 0b100
    Queen  = 0b101
    King   = 0b110
    
def piece(piece_type: PieceType, color: Color) -> bin:
    return bin(piece_type) + bin(color)