---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Combination:\n    def __init__(self, N: int, MOD: int) -> None:\n \
    \       self.N = N + 100\n        self.MOD = MOD\n        self.fac = [0]*(self.N\
    \ + 1)\n        self.fac_inv = [0]*(self.N + 1)\n        self.fac[0] = 1\n   \
    \     self.fac_inv[0] = 1\n\n        for i in range(1, self.N + 1):\n        \
    \    self.fac[i] = self.fac[i - 1] * i\n            self.fac[i] %= self.MOD\n\
    \        \n        for i in range(1, self.N + 1):\n            self.fac_inv[i]\
    \ = pow(self.fac[i], self.MOD - 2, self.MOD)\n    \n    def nCr(self, N: int,\
    \ R: int) -> int:\n        return self.fac[N]*self.fac_inv[R]*self.fac_inv[N -\
    \ R] % self.MOD\n\n    def nPr(self, N: int, R: int) -> int:\n        return self.nCr(N,\
    \ R)*self.fac[R] % self.MOD\n\n\ndef main() -> None:\n    N = 10**5\n    mod =\
    \ 998244353\n    Com = Combination(N, mod)\n\n\nif __name__ == \"__main__\":\n\
    \    main()"
  dependsOn: []
  isVerificationFile: false
  path: Math/Combination.py
  requiredBy: []
  timestamp: '2024-08-21 21:59:55+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/Combination.py
layout: document
redirect_from:
- /library/Math/Combination.py
- /library/Math/Combination.py.html
title: Math/Combination.py
---
