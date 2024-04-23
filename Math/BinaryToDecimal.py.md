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
  code: "# \uFF12\u9032\u6570 -> 10\u9032\u6570\u3078\u306E\u5909\u63DB\ndef BinaryToDecimal(num):\n\
    \    num = str(num)[::-1]\n    decimal_number = 0\n    for i in range(len(num)):\n\
    \        decimal_number += int(num[i]) * (2 ** i)\n    return decimal_number\n\
    \nn = 101001001111101011\nans = BinaryToDecimal(n)\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: Math/BinaryToDecimal.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/BinaryToDecimal.py
layout: document
redirect_from:
- /library/Math/BinaryToDecimal.py
- /library/Math/BinaryToDecimal.py.html
title: Math/BinaryToDecimal.py
---
