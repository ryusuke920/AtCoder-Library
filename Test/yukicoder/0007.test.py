# verification-helper: PROBLEM https://yukicoder.me/problems/no/7

import sys
sys.path.append("../../")

from Math import SieveOfEratosthenes

def main() -> None:

    n = int(input())
    primes_list = SieveOfEratosthenes.primes(n)

    # dp[i] := 残りが i の時にあなたが勝つか
    dp = [False] * (n + 1)
    dp[0] = True
    dp[1] = True
    for i in range(2, n + 1):
        check = False
        for j in primes_list:
            if 0 <= i - j <= n:
                if dp[i - j] == False:
                    check = True
        
        dp[i] = check
    
    print("Win") if dp[n] else print("Lose")


if __name__ == "__main__":
    main()