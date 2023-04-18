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
  code: "from collections import deque\n\ndef bfs(n: int, g:list, s: int) -> list:\n\
    \    n = len(g)\n    INF = float('inf')\n    dist = [INF] * n\n    dist[s] = 0\n\
    \    \n    q = deque()\n    q.append(s)\n\n    while q:\n        prev = q.popleft()\n\
    \        for nxt in g[prev]:\n            if dist[nxt] != INF: continue\n    \
    \        dist[nxt] = dist[prev] + 1\n            q.append(nxt)\n\n\n    return\
    \ dist\n\ndef main() -> None:\n    n = int(input())\n\n    g = [[] for _ in range(n)]\n\
    \    for _ in range(n - 1):\n        u, v = map(lambda x: int(x) - 1, input().split())\n\
    \        g[u].append(v)\n        g[v].append(u)\n\n    bfs(0, g)\n\n\n\nif __name__\
    \ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Search/BreadthFirstSearch_graph.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Search/BreadthFirstSearch_graph.py
layout: document
redirect_from:
- /library/Search/BreadthFirstSearch_graph.py
- /library/Search/BreadthFirstSearch_graph.py.html
title: Search/BreadthFirstSearch_graph.py
---
