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
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import Dice\n\ndef main()\
    \ -> None:\n    up, front, right, left, back, down = map(int, input().split())\n\
    \    d = {}\n    d[1] = up\n    d[2] = front\n    d[3] = right\n    d[4] = left\n\
    \    d[5] = back\n    d[6] = down\n\n    # E: \u53F3\u306B\u56DE\u8EE2, N: \u5965\
    \u306B\u56DE\u8EE2, S: \u624B\u524D\u306B\u56DE\u8EE2, W: \u5DE6\u306B\u56DE\u8EE2\
    \n    # u,d,f,b,l,r\u3092\u305D\u308C\u305E\u308C 0,1,2,3,4,5\u3068\u3057\u3066\
    state1,state2\u306B\u6307\u5B9A\n    dice = Dice.Dice(0, 1, 2, 2, 0, 0)\n\n  \
    \  direction = input()\n    for i in direction:\n        if i == \"E\":\n    \
    \        dice.RotateE()\n        if i == \"N\":\n            dice.RotateN()\n\
    \        if i == \"S\":\n            dice.RotateS()\n        if i == \"W\":\n\
    \            dice.RotateW()\n\n    state = dice.status()\n\n    print(d[state[0]])\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Math/Dice.py
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_11_A.test.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_11_A.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_11_A.test.py
- /verify/Test/AOJ/ITP1/ITP1_11_A.test.py.html
title: Test/AOJ/ITP1/ITP1_11_A.test.py
---
