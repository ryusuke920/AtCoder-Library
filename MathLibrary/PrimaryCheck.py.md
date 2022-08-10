---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/ALDS1/ALDS1_1_C.test.py
    title: Test/AOJ/ALDS1/ALDS1_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def PrimaryCheck(x: int) -> bool:\n    if x == 1:\n        return False\n\
    \n    for i in range(2, int(x ** 0.5) + 1):\n        if x % i == 0:\n        \
    \    return False\n\n    return True"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/PrimaryCheck.py
  requiredBy: []
  timestamp: '2022-08-09 16:25:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/ALDS1/ALDS1_1_C.test.py
documentation_of: MathLibrary/PrimaryCheck.py
layout: document
redirect_from:
- /library/MathLibrary/PrimaryCheck.py
- /library/MathLibrary/PrimaryCheck.py.html
title: MathLibrary/PrimaryCheck.py
---
