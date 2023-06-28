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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def ReverseRotate(l: list) -> list:\n    \"\"\"180\xB0\u56DE\u8EE2\u3055\u305B\
    \u308B\"\"\"\n    h, w = len(l), len(l[0])\n    ans = [[None] * w for _ in range(h)]\n\
    \    for i in range(h):\n        for j in range(w):\n            ans[h - i - 1][w\
    \ - j - 1] = l[i][j]\n\n    return ans\n\nsample = [[0, 1, 2, 3], [4, 5, 6, 7],\
    \ [8, 9, 10, 11]]\nprint(*ReverseRotate(sample), sep=\"\\n\")"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/RotateReverse.py
  requiredBy: []
  timestamp: '2022-07-10 23:02:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometry/RotateReverse.py
layout: document
redirect_from:
- /library/Geometry/RotateReverse.py
- /library/Geometry/RotateReverse.py.html
title: Geometry/RotateReverse.py
---
