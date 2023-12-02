---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/ITP1/ITP1_11_A.test.py
    title: Test/AOJ/ITP1/ITP1_11_A.test.py
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/ITP1/ITP1_11_B.test.py
    title: Test/AOJ/ITP1/ITP1_11_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\nclass Dice:\n    \"\"\"\u30B5\u30A4\u30B3\u30ED\u306E\u5168\
    \u3066\u306E\u72B6\u614B (up, down, front, back, left, right \u306E\u9806) (u\
    \ + d = f + b = l + r = 7 \u304C\u6210\u308A\u7ACB\u3064)\"\"\"\n    state = [\n\
    \            [1, 6, 2, 5, 4, 3], [1, 6, 3, 4, 2, 5], [1, 6, 4, 3, 5, 2], [1, 6,\
    \ 5, 2, 3, 4],\n            [2, 5, 1, 6, 3, 4], [2, 5, 3, 4, 6, 1], [2, 5, 4,\
    \ 3, 1, 6], [2, 5, 6, 1, 4, 3],\n            [3, 4, 1, 6, 5, 2], [3, 4, 2, 5,\
    \ 1, 6], [3, 4, 5, 2, 6, 1], [3, 4, 6, 1, 2, 5],\n            [4, 3, 1, 6, 2,\
    \ 5], [4, 3, 2, 5, 6, 1], [4, 3, 5, 2, 1, 6], [4, 3, 6, 1, 5, 2],\n          \
    \  [5, 2, 1, 6, 4, 3], [5, 2, 3, 4, 1, 6], [5, 2, 4, 3, 6, 1], [5, 2, 6, 1, 3,\
    \ 4],\n            [6, 1, 2, 5, 3, 4], [6, 1, 3, 4, 5, 2], [6, 1, 4, 3, 2, 5],\
    \ [6, 1, 5, 2, 4, 3]\n        ]\n\n    def __init__(self, state1: int, value1:\
    \ int, state2: int, value2: int, now_x: int, now_y: int) -> None:\n        \"\"\
    \"state1 \u306E\u9762\u304C value1, state2 \u306E\u9762\u304C value2\"\"\"\n \
    \       \"\"\"u, d, f, b, l, r -> 0, 1, 2, 3, 4, 5\"\"\"\n        self.now_x =\
    \ now_x\n        self.now_y = now_y\n        for i in range(24):\n           \
    \ if Dice.state[i][state1] == value1 and Dice.state[i][state2] == value2:\n  \
    \              self.u, self.d, self.f, self.b, self.l, self.r = Dice.state[i]\n\
    \                break\n        else:\n            print(\"Error\", file=sys.stderr)\n\
    \            exit()\n\n\n    #\u4E0A\u304B\u3089\u898B\u3066y\u8EF8\u306E+\u65B9\
    \u5411\u306B\u56DE\u8EE2 (\u5F8C\u9762\u304C\u4E0B\u9762\u306B\u306A\u308B)\n\
    \    def RotateN(self) -> None:\n        self.d, self.f, self.u, self.b = self.b,\
    \ self.d, self.f, self.u\n        self.now_y += 1\n\n\n    #\u4E0A\u304B\u3089\
    \u898B\u3066y\u8EF8\u306E-\u65B9\u5411\u306B\u56DE\u8EE2 (\u524D\u9762\u304C\u4E0B\
    \u9762\u306B\u306A\u308B)\n    def RotateS(self) -> None:\n        self.d, self.f,\
    \ self.u ,self.b = self.f, self.u, self.b, self.d\n        self.now_y -= 1\n\n\
    \n    #\u4E0A\u304B\u3089\u898B\u3066x\u8EF8\u306E+\u65B9\u5411\u306B\u56DE\u8EE2\
    \ (\u53F3\u9762\u304C\u4E0B\u9762\u306B\u306A\u308B)\n    def RotateE(self) ->\
    \ None:\n        self.d, self.l, self.u, self.r = self.r, self.d, self.l, self.u\n\
    \        self.now_x += 1\n\n\n    # \u4E0A\u304B\u3089\u898B\u3066x\u8EF8\u306E\
    -\u65B9\u5411\u306B\u56DE\u8EE2 (\u5DE6\u9762\u304C\u4E0B\u9762\u306B\u306A\u308B\
    )\n    def RotateW(self) -> None:\n        self.d, self.l, self.u, self.r = self.l,\
    \ self.u, self.r, self.d\n        self.now_x -= 1\n\n\n    # \u524D\u304B\u3089\
    \u898B\u3066\u5DE6\u56DE\u8EE2 (\u53CD\u6642\u8A08\u56DE\u308A)\n    def RotateL(self)\
    \ -> None:\n        self.f, self.l, self.b, self.r = self.r, self.f, self.l, self.b\n\
    \n\n    # \u524D\u304B\u3089\u898B\u3066\u53F3\u56DE\u8EE2 (\u6642\u8A08\u56DE\
    \u308A)\n    def RotateR(self) -> None:\n        self.f, self.l, self.b, self.r\
    \ = self.l, self.b, self.r, self.f\n    \n\n    def status(self) -> None:\n  \
    \      # \u4E0A\u3001\u4E0B\u3001\u524D\u3001\u5F8C\u3001\u53F3\u3001\u5DE6\u3001\
    (x, y)\u3000\u306E\u9806\u3067\u8FD4\u3059\n        return self.u, self.d, self.f,\
    \ self.b, self.r, self.l, self.now_x, self.now_y"
  dependsOn: []
  isVerificationFile: false
  path: Math/Dice.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/ITP1/ITP1_11_A.test.py
  - Test/AOJ/ITP1/ITP1_11_B.test.py
documentation_of: Math/Dice.py
layout: document
redirect_from:
- /library/Math/Dice.py
- /library/Math/Dice.py.html
title: Math/Dice.py
---
