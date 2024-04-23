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
  code: "# \u8A08\u7B97\u91CF\uFF1AO(|V||E|)\ndef bellman_ford(n: int, g: list, s:\
    \ int) -> list:\n    INF = float('inf')\n    dist = [INF] * n\n    dist[s] = 0\n\
    \n    for i in range(n):\n        update = False # \u7D4C\u8DEF\u66F4\u65B0\u3092\
    \u884C\u3063\u305F\u304B\n        for a, b, cost in g:\n            if dist[b]\
    \ > dist[a] + cost:\n                dist[b] = dist[a] + cost\n              \
    \  update = True\n\n        # \u66F4\u65B0\u304C\u884C\u308F\u308C\u306A\u3051\
    \u308C\u3070\u305D\u308C\u304C\u6700\u77ED\u7D4C\u8DEF\u3068\u306A\u308B\n   \
    \     if not update:\n            break\n\n        if i == n - 1:\n          \
    \  return -1\n\n    return dist\n\n\ndef main() -> None:\n    n, m = map(int,\
    \ input().split())\n    g = []\n    for _ in range(m):\n        u, v, cost = map(int,\
    \ input().split())\n        u -= 1\n        v -= 1\n        g.append((u, v, cost))\n\
    \        g.append((v, u, cost))\n\n    ans = bellman_ford(0)\n\n    if ans ==\
    \ -1:\n        print('Yes')\n    else:\n        print(ans)\n\n\nif __name__ ==\
    \ \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Graph/BellmanFord.py
  requiredBy: []
  timestamp: '2022-07-19 12:08:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/BellmanFord.py
layout: document
redirect_from:
- /library/Graph/BellmanFord.py
- /library/Graph/BellmanFord.py.html
title: Graph/BellmanFord.py
---
