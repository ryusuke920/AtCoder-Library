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
  code: "# \u6700\u5C0F\u5168\u57DF\u6728\uFF08\u30D7\u30EA\u30E0\u6CD5\uFF09\nfrom\
    \ heapq import heappop, heappush, heapify\n\nn, m = map(int,input().split())\n\
    \ng = [[] for _ in range(n)]\nfor _ in range(m):\n    u, v, cost = map(int,input().split())\n\
    \    g[u].append((cost, v))\n    g[v].append((cost, u))\n\nvisited = [False] *\
    \ n\nconnection = 0\nq = []\nq.append((0, 0))\nheapify(q)\n\nans = 0\nwhile q:\n\
    \    cost, v = heappop(q)\n    if visited[v]: continue\n\n    visited[v] = True\n\
    \    connection += 1\n    ans += cost\n\n    for nxt in g[v]:\n        heappush(q,\
    \ nxt)\n    \n    if connection == n:\n        break\n\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Prim.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Prim.py
layout: document
redirect_from:
- /library/Graph/Prim.py
- /library/Graph/Prim.py.html
title: Graph/Prim.py
---
