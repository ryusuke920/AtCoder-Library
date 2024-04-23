---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Math/Dice.py
    title: Math/Dice.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_B&lang=ja\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import Dice\n\ndef main()\
    \ -> None:\n    up, front, right, left, back, down = map(int, input().split())\n\
    \    d = {}\n    d[1] = up\n    d[2] = front\n    d[3] = right\n    d[4] = left\n\
    \    d[5] = back\n    d[6] = down\n\n    rev_d = {}\n    rev_d[up] = 1\n    rev_d[front]\
    \ = 2\n    rev_d[right] = 3\n    rev_d[left] = 4\n    rev_d[back] = 5\n    rev_d[down]\
    \ = 6\n\n    q = int(input())\n    for _ in range(q):\n        up, front = map(int,\
    \ input().split())\n        dice = Dice.Dice(0, rev_d[up], 2, rev_d[front], 0,\
    \ 0)\n        print(d[dice.status()[4]])\n\n\nif __name__ == \"__main__\":\n \
    \   main()"
  dependsOn:
  - Math/Dice.py
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_11_B.test.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_11_B.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_11_B.test.py
- /verify/Test/AOJ/ITP1/ITP1_11_B.test.py.html
title: Test/AOJ/ITP1/ITP1_11_B.test.py
---
