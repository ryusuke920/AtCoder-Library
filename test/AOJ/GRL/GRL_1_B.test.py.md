---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Graph import BellmanFord\n\
    from Search import BreadthFirstSearch_graph\n\ndef main() -> None:\n    V, E,\
    \ r = map(int, input().split())\n    s, t, d = [0] * E, [0] * E, [0] * E\n\n \
    \   g = [[] for _ in range(V)]\n    for i in range(E):\n        s[i], t[i], d[i]\
    \ = map(int, input().split())\n        g[s[i]].append(t[i])\n\n    dist = BreadthFirstSearch_graph.bfs(V,\
    \ g, r)\n    judge = [False] * V\n\n    for i in range(V):\n        if dist[i]\
    \ != float('inf'):\n            judge[i] = True\n    \n    g = []\n    for i in\
    \ range(E):\n        if judge[s[i]]:\n            g.append((s[i], t[i], d[i]))\n\
    \n    ans = BellmanFord.bellman_ford(V, g, r)\n    if ans == -1:\n        print('NEGATIVE\
    \ CYCLE')\n    else:\n        for i in range(V):\n            if ans[i] == float('inf'):\n\
    \                print('INF')\n            else:\n                print(ans[i])\n\
    \n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: test/AOJ/GRL/GRL_1_B.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/AOJ/GRL/GRL_1_B.test.py
layout: document
redirect_from:
- /verify/test/AOJ/GRL/GRL_1_B.test.py
- /verify/test/AOJ/GRL/GRL_1_B.test.py.html
title: test/AOJ/GRL/GRL_1_B.test.py
---
