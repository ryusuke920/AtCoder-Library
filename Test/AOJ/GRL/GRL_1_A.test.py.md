---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Graph import Dijkstra\n\n\
    \ndef main():\n    V, E, r = map(int, input().split())\n    g = [[] for _ in range(V)]\n\
    \    INF = 10**18\n    for _ in range(E):\n        s, t, d = map(int, input().split())\n\
    \        g[s].append((t, d))\n\n    dist = Dijkstra.dijkstra(r, g)\n    for i\
    \ in range(V):\n        print(dist[i]) if dist[i] != INF else print(\"INF\")\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/GRL/GRL_1_A.test.py
  requiredBy: []
  timestamp: '2023-04-24 15:04:25+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: Test/AOJ/GRL/GRL_1_A.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/GRL/GRL_1_A.test.py
- /verify/Test/AOJ/GRL/GRL_1_A.test.py.html
title: Test/AOJ/GRL/GRL_1_A.test.py
---
