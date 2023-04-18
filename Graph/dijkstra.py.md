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
  code: "from heapq import heappush, heappop\n\ndef dijkstra(s: int) -> list:\n  \
    \  INF = 10 ** 18\n    dist = [INF] * n\n    dist[s] = 0\n    q = [(0, s)]\n \
    \   while q:\n        pre = heappop(q)[1]\n        for nxt, cost in g[pre]:\n\
    \            if dist[nxt] < dist[pre] + cost: continue\n            dist[nxt]\
    \ = dist[pre] + cost\n            heappush(q, (dist[nxt], nxt))\n\n    return\
    \ dist\n\nn, m = map(int,input().split())\n\ng = [[] for _ in range(n)]\nfor _\
    \ in range(m):\n    x, y, cost = map(int,input().split())\n    x -= 1\n    y -=\
    \ 1\n    g[x].append((y, cost))\n    g[y].append((x, cost))\n\nd = dijkstra(0)"
  dependsOn: []
  isVerificationFile: false
  path: Graph/dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/dijkstra.py
layout: document
redirect_from:
- /library/Graph/dijkstra.py
- /library/Graph/dijkstra.py.html
title: Graph/dijkstra.py
---
