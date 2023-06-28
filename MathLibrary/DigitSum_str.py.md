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
  code: "def DigitSum(num: str) -> int:\n    '''str \u578B\u306E\u6841\u548C\u3092\
    \u6C42\u3081\u308B'''\n    return sum([int(num[i]) for i in range(len(num))])\n\
    \nprint(DigitSum('1234567890'))"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/DigitSum_str.py
  requiredBy: []
  timestamp: '2022-05-30 00:19:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/DigitSum_str.py
layout: document
redirect_from:
- /library/MathLibrary/DigitSum_str.py
- /library/MathLibrary/DigitSum_str.py.html
title: MathLibrary/DigitSum_str.py
---
