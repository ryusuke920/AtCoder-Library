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
  code: "from collections import deque\n\ndef bfs(sy: int, sx: int) -> list:\n   \
    \ INF = float('inf')\n    dist = [[INF] * w for _ in range(h)]\n    dist[sy][sx]\
    \ = 0\n    \n    for i in range(h):\n        for j in range(w):\n            if\
    \ grid[i][j] == '#':\n                dist[i][j] = -1\n    \n    d = ((0, 1),\
    \ (0, -1), (1, 0), (-1, 0))\n    q = deque()\n    q.append((sy, sx))\n\n    while\
    \ q:\n        vy, vx = q.popleft()\n        for dy, dx in d:\n            y =\
    \ vy + dy\n            x = vx + dx\n            if not (0 <= x < w and 0 <= y\
    \ < h):continue\n            if grid[y][x] == '#': continue\n            if dist[y][x]\
    \ != INF: continue\n            dist[y][x] = dist[vy][vx] + 1\n            q.append((y,\
    \ x))\n    \n    return dist\n\ndef main() -> None:\n    global h, w, grid\n\n\
    \    h, w = map(int, input().split())\n    grid = [list(input()) for _ in range(h)]\n\
    \n    dist = bfs(0, 0)\n    print(*dist, sep='\\n')\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Search/BreadthFirstSearch_grid.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Search/BreadthFirstSearch_grid.py
layout: document
redirect_from:
- /library/Search/BreadthFirstSearch_grid.py
- /library/Search/BreadthFirstSearch_grid.py.html
title: Search/BreadthFirstSearch_grid.py
---
