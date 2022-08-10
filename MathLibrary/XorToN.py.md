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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def XorToN(N: int) -> int:\n    \"0 \u301C N \u307E\u3067\u306E XOR \u306E\
    \u5024\u3092\u8FD4\u3059\u95A2\u6570\"\n    \n    if N % 4 == 0:\n        return\
    \ N\n    \n    if N % 4 == 1:\n        return 1\n    \n    if N % 4 == 2:\n  \
    \      return N + 1\n    \n    if N % 4 == 3:\n        return 0\n\nprint(XorToN(196))"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/XorToN.py
  requiredBy: []
  timestamp: '2022-05-30 00:16:39+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/XorToN.py
layout: document
redirect_from:
- /library/MathLibrary/XorToN.py
- /library/MathLibrary/XorToN.py.html
title: MathLibrary/XorToN.py
---
