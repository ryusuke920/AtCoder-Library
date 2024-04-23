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
  code: "def XorToN(N: int) -> int:\n    \"0 \u301C N \u307E\u3067\u306E XOR \u306E\
    \u5024\u3092\u8FD4\u3059\u95A2\u6570\"\n    \n    if N % 4 == 0:\n        return\
    \ N\n    \n    if N % 4 == 1:\n        return 1\n    \n    if N % 4 == 2:\n  \
    \      return N + 1\n    \n    if N % 4 == 3:\n        return 0\n\nprint(XorToN(196))"
  dependsOn: []
  isVerificationFile: false
  path: Math/XorToN.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/XorToN.py
layout: document
redirect_from:
- /library/Math/XorToN.py
- /library/Math/XorToN.py.html
title: Math/XorToN.py
---
