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
  code: "import sys\nsys.setrecursionlimit(10 ** 6)\n\nn = int(input())\ng = [[] for\
    \ _ in range(n)]\n\nfor _ in range(n - 1):\n    a, b = map(int,input().split())\n\
    \    a -= 1\n    b -= 1\n    g[a].append(b)\n    g[b].append(a)\n\nfor i in range(n):\n\
    \    g[i].sort()\n\nans = [] # \u9802\u70B9\u96C6\u5408\ndepth = [] # \u6DF1\u3055\
    \u306E\u96C6\u5408\ndef dfs(now: int, prev: int, cnt: int):\n    ans.append(now\
    \ + 1)\n    depth.append(cnt)\n    for nxt in g[now]:\n        if nxt == prev:\
    \ continue\n        dfs(nxt, now, cnt + 1)\n        ans.append(now + 1)\n    \
    \    depth.append(cnt)\n\ndfs(0, -1, 0)\nprint(*ans)\nprint(*depth)"
  dependsOn: []
  isVerificationFile: false
  path: Graph/EulerTour.py
  requiredBy: []
  timestamp: '2022-02-06 18:58:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/EulerTour.py
layout: document
redirect_from:
- /library/Graph/EulerTour.py
- /library/Graph/EulerTour.py.html
title: Graph/EulerTour.py
---
