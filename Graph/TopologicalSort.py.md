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
  code: "from collections import defaultdict\nfrom heapq import heappop, heappush\n\
    \nn, m = map(int,input().split())\n\ng = [[] for _ in range(n)]\nd = defaultdict(int)\
    \ # d[i] := \u9802\u70B9i\u306B\u5165\u3063\u3066\u304F\u308B\u8FBA\u306E\u500B\
    \u6570\n\nfor _ in range(m):\n    a, b = map(int,input().split())\n    g[a - 1].append(b\
    \ - 1)\n    d[b - 1] += 1\n\nq = []\n# \u30B9\u30BF\u30FC\u30C8\u5730\u70B9\u3092\
    \u6C7A\u3081\u308B\nfor i in range(n):\n    if d[i] == 0:\n        heappush(q,\
    \ i)\n\nans = []\nl = 0 # \u7B54\u3048\u306E\u9577\u3055\nwhile l < n:\n    if\
    \ len(q) == 0:\n        exit(print(-1))\n\n    v = heappop(q)\n    ans.append(v\
    \ + 1)\n    l += 1\n    for i in g[v]:\n        d[i] -= 1\n        if d[i] ==\
    \ 0:\n            heappush(q, i)\n\nprint(*ans)"
  dependsOn: []
  isVerificationFile: false
  path: Graph/TopologicalSort.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/TopologicalSort.py
layout: document
redirect_from:
- /library/Graph/TopologicalSort.py
- /library/Graph/TopologicalSort.py.html
title: Graph/TopologicalSort.py
---
