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
  code: "# warshall_floyd\u6CD5\ndef warshall_floyd() -> list:\n    for k in range(n):\n\
    \        for i in range(n):\n            for j in range(n):\n                dist[i][j]\
    \ = min(dist[i][j], dist[i][k] + dist[k][j])\n\n    return dist\n\nINF = 10 **\
    \ 20\nn, m = map(int,input().split()) # \u9802\u70B9\u6570\u30FB\u8FBA\u306E\u6570\
    \n\ndist = [[INF] * n for _ in range(n)] # \u96A3\u63A5\u884C\u5217\u306E\u521D\
    \u671F\u5316\n\n# \u81EA\u5206\u81EA\u8EAB\u3078\u306E\u30B3\u30B9\u30C8\u306F\
    \ 0\nfor i in range(n):\n    dist[i][i] = 0\n\n# \u4E0E\u3048\u3089\u308C\u305F\
    \u8DDD\u96E2\u306E\u521D\u671F\u5316\nfor i in range(m):\n    x, y, r = map(int,input().split())\n\
    \    dist[x - 1][y - 1] = r\n    dist[y - 1][x - 1] = r\n\n# s\u304B\u3089t\u3078\
    \u306E\u6700\u77ED\u8DDD\u96E2\u3092\u6C42\u3081\u308B\nans = warshall_floyd()"
  dependsOn: []
  isVerificationFile: false
  path: Graph/warshall_floyd.py
  requiredBy: []
  timestamp: '2022-03-23 20:17:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/warshall_floyd.py
layout: document
redirect_from:
- /library/Graph/warshall_floyd.py
- /library/Graph/warshall_floyd.py.html
title: Graph/warshall_floyd.py
---
