---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/1639.test.py
    title: Test/yukicoder/1639.test.py
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/1639.test.py
    title: test/yukicoder/1639.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Kruskal:\n    def __init__(self, n: int, g: list) -> None:\n      \
    \  self.n = n\n        self.g = g.sort(key=lambda x: x[2])\n        self.p = [-1]\
    \ * n\n\n\n    def leader(self, a: int) -> int:\n        while self.p[a] >= 0:\n\
    \            a = self.p[a]\n\n        return a\n\n\n    def merge(self, a: int,\
    \ b: int) -> int:\n        x = self.leader(a)\n        y = self.leader(b)\n\n\
    \        if x == y:\n            return x\n\n        if self.p[x] > self.p[y]:\n\
    \            x, y = y, x\n\n        self.p[x] += self.p[y]\n        self.p[y]\
    \ = x\n\n        return x\n\n\n    def same(self, a: int, b: int) -> bool:\n \
    \       return self.leader(a) == self.leader(b)\n\n\n    def size(self, a: int)\
    \ -> int:\n        return -self.p[self.leader(a)]\n\n\n    def cost(self, g: list)\
    \ -> list:\n        tree = []\n        for u, v, cost in g:\n            if self.same(u,\
    \ v):\n                continue\n            self.merge(u, v)\n            tree.append(cost)\n\
    \n        return tree\n\n\ndef main() -> None:\n    n, m = map(int, input().split())\n\
    \    g = [list(map(int, input().split())) for _ in range(m)]\n\n    kruskal =\
    \ Kruskal(n, g)\n    print(sum(kruskal.tree(g)))\n\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Kruskal.py
  requiredBy: []
  timestamp: '2022-08-10 23:47:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/yukicoder/1639.test.py
  - test/yukicoder/1639.test.py
documentation_of: Graph/Kruskal.py
layout: document
redirect_from:
- /library/Graph/Kruskal.py
- /library/Graph/Kruskal.py.html
title: Graph/Kruskal.py
---
