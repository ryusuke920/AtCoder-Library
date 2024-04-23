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
  code: "from heapq import heappush, heappop\n\ndef dijkstra(s: int, g: list, INF=10**18)\
    \ -> list:\n    n = len(g)\n    dist = [INF] * n\n    dist[s] = 0\n    q = [(0,\
    \ s)]\n    while q:\n        pre = heappop(q)[1]\n        for nxt, cost in g[pre]:\n\
    \            if dist[nxt] < dist[pre] + cost: continue\n            dist[nxt]\
    \ = dist[pre] + cost\n            heappush(q, (dist[nxt], nxt))\n\n    return\
    \ dist\n\n\ndef main():\n    n, m = map(int,input().split())\n    g = [[] for\
    \ _ in range(n)]\n    for _ in range(m):\n        x, y, cost = map(int,input().split())\n\
    \        x -= 1\n        y -= 1\n        g[x].append((y, cost))\n        g[y].append((x,\
    \ cost))\n\n    d = dijkstra(0, g)\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Dijkstra.py
layout: document
redirect_from:
- /library/Graph/Dijkstra.py
- /library/Graph/Dijkstra.py.html
title: Graph/Dijkstra.py
---
