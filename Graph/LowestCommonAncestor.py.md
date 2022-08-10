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
  code: "import sys\nsys.setrecursionlimit(10 ** 6)\n\nn = int(input())\ng = [[] for\
    \ _ in range(n)]\nfor i in range(n):\n    a = list(map(int, input().split()))[1:]\n\
    \    for j in a:\n        g[i].append(j)\n        g[j].append(i)\n\nLogN = 1\n\
    while 1 << LogN < n: \n    LogN += 1\n\ndepth = [0] * n\nroot = [[0] * n for _\
    \ in range(LogN)]\n\ndef dfs(now: int, prev: int):\n    root[0][now] = prev\n\
    \    for nxt in g[now]:\n        if nxt == prev: continue\n        depth[nxt]\
    \ = depth[now] + 1\n        dfs(nxt, now)\ndfs(0, -1)\n\nfor i in range(LogN -\
    \ 1):\n    for j in range(n):\n        root[i + 1][j] = root[i][root[i][j]]\n\n\
    def LCA(u, v):\n    # depth[u] < depth[v]\n    if depth[u] > depth[v]:\n     \
    \   u, v = v, u\n\n    dist = depth[v] - depth[u]\n    for i in range(LogN):\n\
    \        if dist >> i & 1:\n            v = root[i][v]\n\n    if u == v:\n   \
    \     return u\n\n    for i in reversed(range(LogN)):\n        if root[i][u] !=\
    \ root[i][v]:\n            u = root[i][u]\n            v = root[i][v]\n    return\
    \ root[0][u]\n\nq = int(input())\nfor _ in range(q):\n    u, v = map(int, input().split())\n\
    \    print(LCA(u, v))"
  dependsOn: []
  isVerificationFile: false
  path: Graph/LowestCommonAncestor.py
  requiredBy: []
  timestamp: '2022-02-06 19:12:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/LowestCommonAncestor.py
layout: document
redirect_from:
- /library/Graph/LowestCommonAncestor.py
- /library/Graph/LowestCommonAncestor.py.html
title: Graph/LowestCommonAncestor.py
---
