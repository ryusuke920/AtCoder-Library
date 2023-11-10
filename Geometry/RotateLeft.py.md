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
  code: "def LeftRotate(l: list) -> list:\n    \"\"\"\u5DE6\u306B90\xB0\u56DE\u8EE2\
    \u3055\u305B\u308B\"\"\"\n    h, w = len(l), len(l[0])\n    ans = [[None] * h\
    \ for _ in range(w)]\n    for i in range(h):\n        for j in range(w):\n   \
    \         ans[w - j - 1][i] = l[i][j]\n\n    return ans\n\nsample = [[0, 1, 2,\
    \ 3], [4, 5, 6, 7], [8, 9, 10, 11]]\nprint(*LeftRotate(sample), sep=\"\\n\")"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/RotateLeft.py
  requiredBy: []
  timestamp: '2022-07-10 23:02:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometry/RotateLeft.py
layout: document
redirect_from:
- /library/Geometry/RotateLeft.py
- /library/Geometry/RotateLeft.py.html
title: Geometry/RotateLeft.py
---
