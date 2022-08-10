---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc259/submissions/33150317
    - https://atcoder.jp/contests/abc259/tasks/abc259_d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def SharedPoint(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) ->\
    \ int:\n    \"\"\"2\u3064\u306E\u5186\u306E\u5171\u6709\u70B9\u306E\u500B\u6570\
    \u3092\u6C42\u3081\u308B\"\"\"\n    # (x1, y1) \u3092\u4E2D\u5FC3\u3068\u3057\u305F\
    \u534A\u5F84 r1 \u306E\u5186\n    # (x - x1) ** 2 + (y - y1) ** 2 = r1 ** 2\n\
    \    d = (x1 - x2) ** 2 + (y1 - y2) ** 2\n    \n    # r1 > r2\n    if r1 < r2:\n\
    \        r1, r2 = r2, r1\n    \n    if d == (r1 + r2) ** 2 or d == (r1 - r2) **\
    \ 2:\n        return 1\n    elif (r1 - r2) ** 2 < d < (r1 + r2) ** 2:\n      \
    \  return 2\n    else:\n        return 0\n\n'''\n\u985E\u984C\nABC259-D - Circumferences:\
    \ https://atcoder.jp/contests/abc259/tasks/abc259_d\nAC\u30B3\u30FC\u30C9: https://atcoder.jp/contests/abc259/submissions/33150317\n\
    '''\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/SharedPoint.py
  requiredBy: []
  timestamp: '2022-07-10 23:21:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometry/SharedPoint.py
layout: document
redirect_from:
- /library/Geometry/SharedPoint.py
- /library/Geometry/SharedPoint.py.html
title: Geometry/SharedPoint.py
---
