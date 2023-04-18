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
  code: "def DigitSum(num: int) -> int:\n    '''int \u578B\u306E\u6841\u548C\u3092\
    \u6C42\u3081\u308B'''\n    digit_sum = 0\n\n    while num > 0:\n        digit_sum\
    \ += num % 10\n        num //= 10\n\n    return digit_sum\n\nprint(DigitSum(1234567890))"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/DigitSum_int.py
  requiredBy: []
  timestamp: '2022-05-30 00:19:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/DigitSum_int.py
layout: document
redirect_from:
- /library/MathLibrary/DigitSum_int.py
- /library/MathLibrary/DigitSum_int.py.html
title: MathLibrary/DigitSum_int.py
---
