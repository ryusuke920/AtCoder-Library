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
  code: "# \u914D\u5217\u306E\u7D2F\u7A4D\u548C\u3092\u6C42\u3081\u308B\ndef CumulativeSum(num_array):\n\
    \    for i in range(len(num_array) - 1):\n        num_array[i + 1] += num_array[i]\n\
    \    return num_array\n\n\na = [1, 4, -1, 9, 34, 21, -12, 31]\nans = CumulativeSum(a)\n\
    print(ans)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/CumulativeSum.py
  requiredBy: []
  timestamp: '2021-02-08 02:18:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/CumulativeSum.py
layout: document
redirect_from:
- /library/MathLibrary/CumulativeSum.py
- /library/MathLibrary/CumulativeSum.py.html
title: MathLibrary/CumulativeSum.py
---