import sys

class Dice:
    """サイコロの全ての状態 (up, down, front, back, left, right の順) (u + d = f + b = l + r = 7 が成り立つ)"""
    state = [
            [1, 6, 2, 5, 4, 3], [1, 6, 3, 4, 2, 5], [1, 6, 4, 3, 5, 2], [1, 6, 5, 2, 3, 4],
            [2, 5, 1, 6, 3, 4], [2, 5, 3, 4, 6, 1], [2, 5, 4, 3, 1, 6], [2, 5, 6, 1, 4, 3],
            [3, 4, 1, 6, 5, 2], [3, 4, 2, 5, 1, 6], [3, 4, 5, 2, 6, 1], [3, 4, 6, 1, 2, 5],
            [4, 3, 1, 6, 2, 5], [4, 3, 2, 5, 6, 1], [4, 3, 5, 2, 1, 6], [4, 3, 6, 1, 5, 2],
            [5, 2, 1, 6, 4, 3], [5, 2, 3, 4, 1, 6], [5, 2, 4, 3, 6, 1], [5, 2, 6, 1, 3, 4],
            [6, 1, 2, 5, 3, 4], [6, 1, 3, 4, 5, 2], [6, 1, 4, 3, 2, 5], [6, 1, 5, 2, 4, 3]
        ]

    def __init__(self, state1: int, value1: int, state2: int, value2: int, now_x: int, now_y: int) -> None:
        """state1 の面が value1, state2 の面が value2"""
        """u, d, f, b, l, r -> 0, 1, 2, 3, 4, 5"""
        self.now_x = now_x
        self.now_y = now_y
        for i in range(24):
            if Dice.state[i][state1] == value1 and Dice.state[i][state2] == value2:
                self.u, self.d, self.f, self.b, self.l, self.r = Dice.state[i]
                break
        else:
            print("Error", file=sys.stderr)
            exit()


    #上から見てy軸の+方向に回転 (後面が下面になる)
    def RotateN(self) -> None:
        self.d, self.f, self.u, self.b = self.b, self.d, self.f, self.u
        self.now_y += 1


    #上から見てy軸の-方向に回転 (前面が下面になる)
    def RotateS(self) -> None:
        self.d, self.f, self.u ,self.b = self.f, self.u, self.b, self.d
        self.now_y -= 1


    #上から見てx軸の+方向に回転 (右面が下面になる)
    def RotateE(self) -> None:
        self.d, self.l, self.u, self.r = self.r, self.d, self.l, self.u
        self.now_x += 1


    # 上から見てx軸の-方向に回転 (左面が下面になる)
    def RotateW(self) -> None:
        self.d, self.l, self.u, self.r = self.l, self.u, self.r, self.d
        self.now_x -= 1


    # 前から見て左回転 (反時計回り)
    def RotateL(self) -> None:
        self.f, self.l, self.b, self.r = self.r, self.f, self.l, self.b


    # 前から見て右回転 (時計回り)
    def RotateR(self) -> None:
        self.f, self.l, self.b, self.r = self.l, self.b, self.r, self.f
    

    def status(self) -> None:
        # 上、下、前、後、右、左、(x, y)　の順で返す
        return self.u, self.d, self.f, self.b, self.r, self.l, self.now_x, self.now_y