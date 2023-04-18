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
  code: "from itertools import product\n\ndef BitSearch(x, l): # \u30EA\u30B9\u30C8\
    \u30FB\u6570\n    num = 0\n    for i in product([0, 1], repeat = l):\n       \
    \ for j in range(l):\n            if i[j] == 1: # 1 <-> bit\u304C\u7ACB\u3063\u3066\
    \u3044\u308B\u6642\n                # O(1)"
  dependsOn: []
  isVerificationFile: false
  path: Search/BitSearch.py
  requiredBy: []
  timestamp: '2022-02-06 18:58:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Search/BitSearch.py
layout: document
redirect_from:
- /library/Search/BitSearch.py
- /library/Search/BitSearch.py.html
title: Search/BitSearch.py
---
