from PIL import Image

class Histoboard:
    def __init__(self, n=8):
        self.n       = n
        self.squares = [0]*(n*n)

    def __getitem__(self, i):
        return self.squares[i]
    def __setitem__(self, i, val):
        self.squares[i] = val
    
    def __len__(self):
        return len(self.squares)

    def __str__(self):
        board_matrix = [self[i:i+8] for i in range(0, 64, 8)]
        return str(board_matrix)

    def draw(self, size=500, r=0, g=0, b=255) -> Image:
        w, h   = 8, 8
        img    = Image.new("RGB", (w,h))
        pixels = img.load()

        max_num = sum(self) / len(self)
        
        for i in range(w):
            for j in range(h):
                board_square = (j * 8) + i
                color_value  = (self[board_square] / max_num) * 255 / 2

                pixels[i,j]  = (
                    int(color_value*(r/255)),
                    int(color_value*(g/255)),
                    int(color_value*(b/255))
                )

        img = img.resize((size*w,size*h), Image.NEAREST)
        return img
