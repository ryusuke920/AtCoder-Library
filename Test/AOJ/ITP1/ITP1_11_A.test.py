# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja

import sys
sys.path.append("../../../")

from Math import Dice

def main() -> None:
    up, front, right, left, back, down = map(int, input().split())
    d = {}
    d[1] = up
    d[2] = front
    d[3] = right
    d[4] = left
    d[5] = back
    d[6] = down

    # E: 右に回転, N: 奥に回転, S: 手前に回転, W: 左に回転
    # u,d,f,b,l,rをそれぞれ 0,1,2,3,4,5としてstate1,state2に指定
    dice = Dice.Dice(0, 1, 2, 2, 0, 0)

    direction = input()
    for i in direction:
        if i == "E":
            dice.RotateE()
        if i == "N":
            dice.RotateN()
        if i == "S":
            dice.RotateS()
        if i == "W":
            dice.RotateW()

    state = dice.status()

    print(d[state[0]])


if __name__ == "__main__":
    main()