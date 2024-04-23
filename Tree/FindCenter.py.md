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
  code: "# \u6728\u306E\u4E2D\u5FC3\u3092\u6C42\u3081\u308B O(N)\n# 1-indexed\u3067\
    \u8868\u3055\u308C\u305F\u6728\u306E\u4E2D\u5FC3\u3068\u306A\u308A\u3046\u308B\
    \u9802\u70B9\u306E\u96C6\u5408\u3092\u6539\u884C\u533A\u5207\u308A\u3067\u51FA\
    \u529B\u3057\u307E\u3059\u3002\nfrom collections import deque\nfrom collections\
    \ import defaultdict\n\ndef bfs(s: int) -> tuple:\n    \"\u5E45\u512A\u5148\u63A2\
    \u7D22\u3092\u884C\u3044\u3001\u9802\u70B9 s \u304B\u3089\u306E\u8DDD\u96E2\u3092\
    \u6C42\u3081\u308B\"\n    dist = [10000] * N\n    dist[s] = 0\n    q = deque([s])\n\
    \n    vertexmemo = defaultdict(list)\n    vertexmemo[0].append(s)\n    while q:\n\
    \        v = q.popleft()\n        for nxt in g[v]:\n            if dist[nxt] ==\
    \ 10000:\n                dist[nxt] = dist[v] + 1\n                vertexmemo[dist[nxt]].append(nxt)\n\
    \                q.append(nxt)\n    \n    return dist, vertexmemo\n\nN = int(input())\n\
    \ng = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    a, b = map(int, input().split())\n\
    \    a -= 1\n    b -= 1\n    g[a].append(b)\n    g[b].append(a)\n\ndist, vmap\
    \ = bfs(0)\n\n#\u76F4\u5F84\u3092\u4E0E\u3048\u308B\u30D1\u30B9\u306E\u7AEF\u70B9\
    \u304B\u3089\u306E\u8DDD\u96E2\u306E\u30EA\u30B9\u30C8\u3068\u8DDD\u96E2d\u306B\
    \u3042\u308B\u9802\u70B9\u306E\u30EA\u30B9\u30C8\u3092\u5F97\u308B\u3002\nDlist,\
    \ FromA = bfs(vmap[max(dist)][0])\nDiameter = max(Dlist)\n\n#\u76F4\u5F84\u3092\
    \u4E0E\u3048\u308B\u30D1\u30B9\u306E\u3082\u3046\u7247\u65B9\u306E\u7AEF\u70B9\
    \u304B\u3089BFS\u3092\u884C\u3044\u3001\u8DDD\u96E2 d (0 <= d <= Diameter)\u306E\
    \u9802\u70B9\u306E\u30EA\u30B9\u30C8\u3092\u5F97\u308B\u3002\nFromB = bfs(FromA[Diameter][0])[1]\n\
    \n#\u7247\u65B9\u306E\u7AEF\u70B9\u304B\u3089ceil(Diameter/2), floor(Diameter/2)\u306E\
    \u8DDD\u96E2\u306B\u3042\u308B\u9802\u70B9\u3092\u5217\u6319\u3002\npre_center\
    \ = FromA[Diameter//2] if Diameter%2 == 0 else FromA[Diameter//2]+FromA[(Diameter+1)//2]\n\
    center = list()\n\n#\u4ED6\u65B9\u306E\u7AEF\u70B9\u304B\u3089ceil(Diameter/2),\
    \ floor(Diameter/2)\u306E\u8DDD\u96E2\u306B\u3042\u308B\u9802\u70B9\u3092\u5217\
    \u6319\u3002\u5171\u901A\u3059\u308B\u9802\u70B9(\u4E2D\u5FC3)\u3092\u5F97\u308B\
    \u3002\nfor i in FromB[Diameter//2] if Diameter%2 == 0 else FromB[Diameter//2]+FromB[(Diameter+1)//2]:\n\
    \    if i in pre_center:\n        center.append(i+1)\n\nfor i in sorted(center):\n\
    \    print(i)"
  dependsOn: []
  isVerificationFile: false
  path: Tree/FindCenter.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/FindCenter.py
layout: document
redirect_from:
- /library/Tree/FindCenter.py
- /library/Tree/FindCenter.py.html
title: Tree/FindCenter.py
---
