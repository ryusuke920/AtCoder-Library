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
  code: "import sys\ndebug = lambda *x : print(*x, file = sys.stderr)\n\n\"\"\"\n\u3053\
    \u308C\u3092\u4F7F\u7528\u3059\u308B\u3068\u3001\u6A19\u6E96\u30A8\u30E9\u30FC\
    \u51FA\u529B\u306B\u306A\u308B\u306E\u3067\u3001print\u3057\u3066\u3082\u30B8\u30E3\
    \u30C3\u30B8\u306B\u53CD\u6620\u3055\u308C\u306A\u3044\n\"\"\"\n\na = [1, 2, 3,\
    \ 4, 5]\nword = \"ryusuke\"\ndebug(a, word)\n\n\nA, B, C = map(int, input().split())\n\
    if A ** 2 + B ** 2 < C ** 2:\n    print(\"Yes\")\nelse:\n    print(\"No\")"
  dependsOn: []
  isVerificationFile: false
  path: Other/debug.py
  requiredBy: []
  timestamp: '2022-08-11 01:40:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Other/debug.py
layout: document
redirect_from:
- /library/Other/debug.py
- /library/Other/debug.py.html
title: Other/debug.py
---
