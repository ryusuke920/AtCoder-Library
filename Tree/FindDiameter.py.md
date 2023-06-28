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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u6728\u306E\u76F4\u5F84\u3092\u6C42\u3081\u308B O(N^3)\n\nfrom collections\
    \ import deque\n\ndef bfs(s: int) -> list:\n    \"\u5E45\u512A\u5148\u63A2\u7D22\
    \u3092\u884C\u3044\u3001\u9802\u70B9 s \u304B\u3089\u306E\u8DDD\u96E2\u3092\u6C42\
    \u3081\u308B\"\n    dist = [10000] * N\n    dist[s] = 0\n    q = deque([s])\n\
    \    while q:\n        v = q.popleft()\n        for nxt in g[v]:\n           \
    \ if dist[nxt] == 10000:\n                dist[nxt] = dist[v] + 1\n          \
    \      q.append(nxt)\n    \n    return dist\n\nN = int(input())\n\ng = [[] for\
    \ _ in range(N)]\nfor _ in range(N - 1):\n    a, b = map(int, input().split())\n\
    \    a -= 1\n    b -= 1\n    g[a].append(b)\n    g[b].append(a)\n\n\ndist = bfs(0)\n\
    \nmax_dist = max(dist)\nfor i in range(N):\n    if dist[i] == max_dist:\n    \
    \    start = i\n        break\n\nprint(max(bfs(start)))"
  dependsOn: []
  isVerificationFile: false
  path: Tree/FindDiameter.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/FindDiameter.py
layout: document
redirect_from:
- /library/Tree/FindDiameter.py
- /library/Tree/FindDiameter.py.html
title: Tree/FindDiameter.py
---
