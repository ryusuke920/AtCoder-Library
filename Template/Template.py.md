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
  code: "import sys\ninput = sys.stdin.readline\nsys.setrecursionlimit(10 ** 6)\n\
    printd = lambda *x : print(*x, file = sys.stderr)\n\nfrom math import ceil, floor,\
    \ sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees\nfrom collections\
    \ import defaultdict, deque, Counter\nfrom itertools import product, permutations,\
    \ combinations, combinations_with_replacement\nfrom heapq import heapify, heappop,\
    \ heappush\nfrom bisect import bisect, bisect_left, bisect_right\n\n\ndef min_int(a:\
    \ int, b: int) -> int:\n    \"2\u6570\u306E\u6700\u5C0F\u5024\"\n    return a\
    \ if a <= b else b\n\n\ndef min_list(a: list) -> int:\n    \"\u30EA\u30B9\u30C8\
    \u306E\u6700\u5C0F\u5024\"\n    global INF\n    cnt = INF\n    for i in range(len(a)):\n\
    \        if a[i] < cnt:\n            cnt = a[i]\n\n    return cnt\n\n\ndef min_list(a:\
    \ list) -> int:\n    \"\u30EA\u30B9\u30C8\u306E\u6700\u5927\u5024\"\n    global\
    \ INF\n    cnt = -INF\n    for i in range(len(a)):\n        if a[i] > cnt:\n \
    \           cnt = a[i]\n\n    return cnt\n\n\ndef max_int(a: int, b: int) -> int:\n\
    \    \"2\u6570\u306E\u6700\u5927\u5024\"\n    return a if a >= b else b\n\n\n\
    def OutOfRange(h: int, w: int, vy: int, vx: int) -> bool:\n    \"BFS\u306A\u3069\
    \u306E\u914D\u5217\u5916\u53C2\u7167\"\n    d = ((1, 0), (-1, 0), (0, 1), (0,\
    \ -1))\n    for dy, dx in d:\n        y = vy + dy\n        x = vx + dx\n     \
    \   if not (0 <= x < w and 0 <= y < h):\n            return False\n        else:\n\
    \            return True\n\n\ndef main() -> None:\n    INF = 10 ** 18\n\n\nif\
    \ __name__ == '__main__':\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Template/Template.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Template/Template.py
layout: document
redirect_from:
- /library/Template/Template.py
- /library/Template/Template.py.html
title: Template/Template.py
---
