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
  code: "from collections import defaultdict\n\ndef BoyerMoore(s: str, t: str) ->\
    \ bool:\n    '''\u6587\u5B57\u5217 s \u306E\u4E2D\u306B t \u304C\u5B58\u5728\u3059\
    \u308B\u304B\u3092\u5224\u5225\u3059\u308B'''\n    skip_table = defaultdict(lambda\
    \ : -1)\n    for i, j in enumerate(t[::-1]):\n        if skip_table[j] == -1:\n\
    \            skip_table[j] = i\n    \n    l_s = len(s)\n    l_t = len(t)\n\n \
    \   if l_s < l_t:\n        return False\n    else:\n        i = l_t - 1\n    \
    \    cnt = 0\n        while i < l_s:\n            if s[i] == t[-1 - cnt]:\n  \
    \              cnt += 1\n                i -= 1\n            else:\n         \
    \       i += l_t if skip_table[s[i]] == -1 else skip_table[s[i]]\n           \
    \     cnt = 0\n\n            if cnt == l_t:\n                print(f'[{i + 1},\
    \ {i + l_t}] \u306E\u533A\u9593\u306B {t} \u304C\u898B\u3064\u304B\u308A\u307E\
    \u3057\u305F\u3002')\n                return True\n        \n        return False\n\
    \ns = 'abcdefghijklmnopqrstuvwxyz'\nt = 'def'\nprint(BoyerMoore(s, t))"
  dependsOn: []
  isVerificationFile: false
  path: String/BoyerMoore.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/BoyerMoore.py
layout: document
redirect_from:
- /library/String/BoyerMoore.py
- /library/String/BoyerMoore.py.html
title: String/BoyerMoore.py
---
