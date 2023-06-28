# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_D&lang=ja

import sys
sys.path.append("../../../")

from Math import Dice
from random import randint


def main() -> None:

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = True
    for i in range(n - 1):
        for j in range(i + 1, n):

            up_1, front_1, right_1, left_1, back_1, down_1 = a[i]
            up_2, front_2, right_2, left_2, back_2, down_2 = a[j]

            # サイコロの目が 1~6 ではない場合に置き換える
            replace_dice1, replace_dice2 = {}, {}
            replace_dice1[f"{up_1}-1"], replace_dice2[f"{up_2}-1"] = 1, 1
            replace_dice1[f"{front_1}-2"], replace_dice2[f"{front_2}-2"] = 2, 2
            replace_dice1[f"{right_1}-3"], replace_dice2[f"{right_2}-3"] = 3, 3
            replace_dice1[f"{left_1}-4"], replace_dice2[f"{left_2}-4"] = 4, 4
            replace_dice1[f"{back_1}-5"], replace_dice2[f"{back_2}-5"] = 5, 5
            replace_dice1[f"{down_1}-6"], replace_dice2[f"{down_2}-6"] = 6, 6

            # 置き換えた場合に復元する用の辞書
            restoration_dice1, restoration_dice2 = {}, {}
            restoration_dice1[1], restoration_dice2[1] = up_1, up_2
            restoration_dice1[2], restoration_dice2[2] = front_1, front_2
            restoration_dice1[3], restoration_dice2[3] = right_1, right_2
            restoration_dice1[4], restoration_dice2[4] = left_1, left_2
            restoration_dice1[5], restoration_dice2[5] = back_1, back_2
            restoration_dice1[6], restoration_dice2[6] = down_1, down_2

            dice1 = Dice.Dice(0, replace_dice1[f"{up_1}-1"], 2, replace_dice1[f"{front_1}-2"], 0, 0)
            dice2 = Dice.Dice(0, replace_dice2[f"{up_2}-1"], 2, replace_dice2[f"{front_2}-2"], 0, 0)

            for _ in range(1000):
                p = randint(0, 3)
                if p == 0:
                    dice1.RotateN()
                if p == 1:
                    dice1.RotateS()
                if p == 2:
                    dice1.RotateW()
                if p == 3:
                    dice1.RotateE()
                
                check = 0
                for k in range(6):
                    if restoration_dice1[dice1.status()[k]] == restoration_dice2[dice2.status()[k]]:
                        check += 1

                if check == 6:
                    ans = False
                    break

    print("Yes") if ans else print("No")


if __name__ == "__main__":
    main()