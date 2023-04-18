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
  code: "def extgcd(a: int, b: int) -> int:\n    \"ax + by = gcd(a,b) = d \u3068\u306A\
    \u308B (x, y, d) \u3092\u8FD4\u3059\"\n    if b == 0:\n        return (1, 0, a)\n\
    \n    q, r = a // b, a % b\n    x, y, d = extgcd(b, r)\n    s, t = y, x - q *\
    \ y\n\n    return s, t, d # (qb + r)s + bt = d\u3068\u306A\u308B s, t, d\n\nans\
    \ = extgcd(30, 50)\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/ExtGCD.py
  requiredBy: []
  timestamp: '2022-02-06 18:58:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/ExtGCD.py
layout: document
redirect_from:
- /library/MathLibrary/ExtGCD.py
- /library/MathLibrary/ExtGCD.py.html
title: MathLibrary/ExtGCD.py
---
