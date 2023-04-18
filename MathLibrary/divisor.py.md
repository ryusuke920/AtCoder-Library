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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def divisors(n):\n    divisor = []\n    for i in range(1, int(n ** 0.5) +\
    \ 1):\n        if n % i == 0:\n            divisor.append(i)\n            if i\
    \ != n // i:\n                divisor.append(n // i)\n\n    divisor.sort()\n \
    \   return divisor\n\nx = divisors(10 ** 12)\ny = divisors(136)\nprint(len(x))\n\
    print(y)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/divisor.py
  requiredBy: []
  timestamp: '2021-12-06 01:43:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/divisor.py
layout: document
redirect_from:
- /library/MathLibrary/divisor.py
- /library/MathLibrary/divisor.py.html
title: MathLibrary/divisor.py
---
