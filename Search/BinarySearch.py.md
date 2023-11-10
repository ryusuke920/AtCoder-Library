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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def check(arg):\n    if 1:\n        return True\n    else:\n       return\
    \ False\n\ndef binary_search(left: int, right: int) -> int:\n    while right -\
    \ left > 1:\n        mid = (left + right) // 2\n        if check(mid):\n     \
    \       left = mid\n        else:\n            right = mid\n\n    return left"
  dependsOn: []
  isVerificationFile: false
  path: Search/BinarySearch.py
  requiredBy: []
  timestamp: '2022-08-09 16:25:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Search/BinarySearch.py
layout: document
redirect_from:
- /library/Search/BinarySearch.py
- /library/Search/BinarySearch.py.html
title: Search/BinarySearch.py
---
