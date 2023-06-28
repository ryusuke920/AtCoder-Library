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
  code: "def manhattan_distance(li: list, k: int) -> int: # \u8FD4\u308A\u5024\u6CE8\
    \u610F\n    \"\u30DE\u30F3\u30CF\u30C3\u30BF\u30F3\u8DDD\u96E2\u3067\u884C\u3051\
    \u308B\u5834\u6240\u3092\u5168\u63A2\u7D22\u3059\u308B\uFF08t\u306F\u30DE\u30F3\
    \u30CF\u30C3\u30BF\u30F3\u8DDD\u96E2\u306E\u534A\u5F84\uFF09\"\n    tmp = 0 #\
    \ \u3053\u3053\u306F\u4F8B\n    for i in range(k - 1, h - (k - 1)):\n        for\
    \ j in range(k - 1, w - (k - 1)):\n            cnt = 0 # \u3053\u3053\u306F\u4F8B\
    \n            for t in range(2):\n                if t == 0: # ((i,j)\u30DE\u30B9\
    \u3092\u542B\u3080 k \u500B)\n                    for l in reversed(range(k)):\n\
    \                        for x in range(j - l, j + l + 1):\n                 \
    \           y = i - (k - (l + 1))\n                            if li[y][x] ==\
    \ \"1\": cnt += 1 # \u3053\u3053\u306F\u4F8B\n                elif t == 1: # ((i,j)\u30DE\
    \u30B9\u3092\u542B\u307E\u306A\u3044 k-1 \u500B)\n                    for l in\
    \ reversed(range(k - 1)):\n                        for x in range(j - l, j + l\
    \ + 1):\n                            y = i + (k - (l + 1))\n                 \
    \           if li[y][x] == \"1\": cnt += 1 # \u3053\u3053\u306F\u4F8B\n      \
    \      tmp = max(tmp, cnt) # \u3053\u3053\u306F\u4F8B\n    return tmp # \u3053\
    \u3053\u306F\u4F8B\n\n\"\"\"\n5 6 2\n010111\n100100\n010010\n100101\n011010\n\n\
    \u4E0A\u56F3\u306E 5*6 \u306E\u30B0\u30EA\u30C3\u30C9\u3067 k=2 \u306E\u6642\u306E\
    \ 1 \u306E\u542B\u307E\u308C\u308B\u6700\u5927\u306E\u500B\u6570\u3092\u51FA\u529B\
    \u3059\u308B\n\"\"\"\nh, w, k = map(int,input().split()) # \u7E26\u3001\u6A2A\u3001\
    \u30DE\u30F3\u30CF\u30C3\u30BF\u30F3\u8DDD\u96E2\u306E\u534A\u5F84\ngrid = [list(input().rstrip())\
    \ for _ in range(h)]\nans = manhattan_distance(grid, k)\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: Math/ManhattanDistanceSearch.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/ManhattanDistanceSearch.py
layout: document
redirect_from:
- /library/Math/ManhattanDistanceSearch.py
- /library/Math/ManhattanDistanceSearch.py.html
title: Math/ManhattanDistanceSearch.py
---
