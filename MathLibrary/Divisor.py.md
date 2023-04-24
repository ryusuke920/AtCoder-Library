---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/ITP1/ITP1_3_D.test.py
    title: Test/AOJ/ITP1/ITP1_3_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def divisors(n: int) -> list:\n    divisor = []\n    for i in range(1, int(n**0.5)\
    \ + 1):\n        if n % i == 0:\n            divisor.append(i)\n            if\
    \ i != n // i:\n                divisor.append(n // i)\n\n    divisor.sort()\n\
    \    return divisor"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/Divisor.py
  requiredBy: []
  timestamp: '2023-04-24 10:12:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/ITP1/ITP1_3_D.test.py
documentation_of: MathLibrary/Divisor.py
layout: document
redirect_from:
- /library/MathLibrary/Divisor.py
- /library/MathLibrary/Divisor.py.html
title: MathLibrary/Divisor.py
---
