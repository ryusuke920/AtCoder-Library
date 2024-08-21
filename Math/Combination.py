class Combination:
    def __init__(self, N: int, MOD: int) -> None:
        self.N = N + 100
        self.MOD = MOD
        self.fac = [0]*(self.N + 1)
        self.fac_inv = [0]*(self.N + 1)
        self.fac[0] = 1
        self.fac_inv[0] = 1

        for i in range(1, self.N + 1):
            self.fac[i] = self.fac[i - 1] * i
            self.fac[i] %= self.MOD
        
        for i in range(1, self.N + 1):
            self.fac_inv[i] = pow(self.fac[i], self.MOD - 2, self.MOD)
    
    def nCr(self, N: int, R: int) -> int:
        return self.fac[N]*self.fac_inv[R]*self.fac_inv[N - R] % self.MOD

    def nPr(self, N: int, R: int) -> int:
        return self.nCr(N, R)*self.fac[R] % self.MOD


def main() -> None:
    N = 10**5
    mod = 998244353
    Com = Combination(N, mod)


if __name__ == "__main__":
    main()