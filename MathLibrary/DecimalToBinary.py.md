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
  code: "# 10\u9032\u6570 -> 2\u9032\u6570\u3078\u306E\u5909\u63DB\ndef DeciamlToBinary(num):\n\
    \    binary_number = \"\"\n    while num > 0:\n        binary_number += str(num\
    \ % 2)\n        num //= 2\n    return int(binary_number[::-1])\n\nn = 1234567890\n\
    ans = DeciamlToBinary(n)\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/DecimalToBinary.py
  requiredBy: []
  timestamp: '2021-02-08 02:18:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/DecimalToBinary.py
layout: document
redirect_from:
- /library/MathLibrary/DecimalToBinary.py
- /library/MathLibrary/DecimalToBinary.py.html
title: MathLibrary/DecimalToBinary.py
---
