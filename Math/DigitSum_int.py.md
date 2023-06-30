---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: Test/AOJ/ITP1/ITP1_8_B.test.py
    title: Test/AOJ/ITP1/ITP1_8_B.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def DigitSum(num: int) -> int:\n    '''int \u578B\u306E\u6841\u548C\u3092\
    \u6C42\u3081\u308B'''\n    digit_sum = 0\n\n    while num > 0:\n        digit_sum\
    \ += num % 10\n        num //= 10\n\n    return digit_sum"
  dependsOn: []
  isVerificationFile: false
  path: Math/DigitSum_int.py
  requiredBy: []
  timestamp: '2023-06-30 09:44:00+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - Test/AOJ/ITP1/ITP1_8_B.test.py
documentation_of: Math/DigitSum_int.py
layout: document
redirect_from:
- /library/Math/DigitSum_int.py
- /library/Math/DigitSum_int.py.html
title: Math/DigitSum_int.py
---
