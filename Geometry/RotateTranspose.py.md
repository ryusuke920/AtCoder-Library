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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def TransposeRotate(l: list) -> list:\n    \"\"\"\u8EE2\u7F6E\u884C\u5217\
    \u3092\u6C42\u3081\u308B\"\"\"\n    h, w = len(l), len(l[0])\n    ans = [[None]\
    \ * h for _ in range(w)]\n    for i in range(w):\n        for j in range(h):\n\
    \            ans[i][j] = l[j][i]\n\n    return ans\n\nsample = [[0, 1, 2, 3],\
    \ [4, 5, 6, 7], [8, 9, 10, 11]]\nprint(*TransposeRotate(sample), sep=\"\\n\")"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/RotateTranspose.py
  requiredBy: []
  timestamp: '2022-07-10 23:02:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometry/RotateTranspose.py
layout: document
redirect_from:
- /library/Geometry/RotateTranspose.py
- /library/Geometry/RotateTranspose.py.html
title: Geometry/RotateTranspose.py
---
