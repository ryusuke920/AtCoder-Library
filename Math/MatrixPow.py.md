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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def matrix_multi(a: list, b: list, mod=998244353) -> list:\n    len_a, len_b,\
    \ len_b_zero = len(a), len(b), len(b[0])\n    c = [[0] * len(b[0]) for _ in range(len_a)]\n\
    \    for i in range(len_a):\n        for j in range(len_b_zero):\n           \
    \ for k in range(len_b):\n                c[i][j] += a[i][k] * b[k][j]\n     \
    \           c[i][j] %= mod\n\n    return c\n\n\ndef matrix_pow(a: list, n: int)\
    \ -> list:\n    len_a = len(a)\n    cnt = [[0] * len_a for _ in range(len_a)]\n\
    \n    for i in range(len_a):\n        cnt[i][i] = 1\n\n    while n > 0:\n    \
    \    if n & 1:\n            cnt = matrix_multi(a, cnt)\n\n        a = matrix_multi(a,\
    \ a)\n        n >>= 1\n\n    return cnt\n\n\ndef main() -> None:\n    n = int(input())\n\
    \n    fibonacci = [[1, 1], [1, 0]]\n    fibonacci = matrix_pow(fibonacci, n)\n\
    \n    ans = fibonacci[1][0]\n    # print(*fibonacci, sep=\"\\n\")\n    print(ans)\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Math/MatrixPow.py
  requiredBy: []
  timestamp: '2023-11-10 19:18:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/MatrixPow.py
layout: document
redirect_from:
- /library/Math/MatrixPow.py
- /library/Math/MatrixPow.py.html
title: Math/MatrixPow.py
---
