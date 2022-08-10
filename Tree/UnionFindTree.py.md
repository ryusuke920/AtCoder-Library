---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/DSL/DSL_1_A.test.py
    title: Test/AOJ/DSL/DSL_1_A.test.py
  - icon: ':heavy_check_mark:'
    path: test/AOJ/DSL/DSL_1_A.test.py
    title: test/AOJ/DSL/DSL_1_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n):\n        self.n = n\n      \
    \  self.p = [-1] * n\n\n\n    def leader(self, a):\n        while self.p[a] >=\
    \ 0:\n            a = self.p[a]\n        return a\n\n\n    def merge(self, a,\
    \ b):\n        x = self.leader(a)\n        y = self.leader(b)\n\n        if x\
    \ == y:\n            return x\n\n        if self.p[x] > self.p[y]:\n         \
    \   x, y = y, x\n\n        self.p[x] += self.p[y]\n        self.p[y] = x\n\n \
    \       return x\n\n    def same(self, a, b):\n        return self.leader(a) ==\
    \ self.leader(b)\n\n    def size(self, a):\n        return -self.p[self.leader(a)]\n\
    \ndef main() -> None:\n    n, m = map(int, input().split())\n\n    uf = UnionFind(n)\n\
    \n    for _ in range(m):\n        a, b = map(int,input().split())\n        uf.merge(a\
    \ - 1, b - 1)\n\n    ans = 0\n    for i in range(n):\n        ans = max(ans, uf.size(i))\n\
    \n    print(ans)\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Tree/UnionFindTree.py
  requiredBy: []
  timestamp: '2022-07-15 00:14:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/DSL/DSL_1_A.test.py
  - test/AOJ/DSL/DSL_1_A.test.py
documentation_of: Tree/UnionFindTree.py
layout: document
redirect_from:
- /library/Tree/UnionFindTree.py
- /library/Tree/UnionFindTree.py.html
title: Tree/UnionFindTree.py
---
