---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/DSL/DSL_1_A.test.py
    title: Test/AOJ/DSL/DSL_1_A.test.py
  - icon: ':heavy_check_mark:'
    path: Test/yosupo/DataStructure/Unionfind.test.py
    title: Test/yosupo/DataStructure/Unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n: int) -> None:\n        self.n\
    \ = n\n        self.p = [-1] * n\n\n\n    def leader(self, a: int) -> int:\n \
    \       while self.p[a] >= 0:\n            a = self.p[a]\n        return a\n\n\
    \n    def merge(self, a: int, b: int) -> int:\n        x = self.leader(a)\n  \
    \      y = self.leader(b)\n\n        if x == y:\n            return x\n\n    \
    \    if self.p[x] > self.p[y]:\n            x, y = y, x\n\n        self.p[x] +=\
    \ self.p[y]\n        self.p[y] = x\n\n        return x\n\n    def same(self, a:\
    \ int, b: int) -> bool:\n        return self.leader(a) == self.leader(b)\n\n \
    \   def groups(self) -> list:\n        member = [[] for _ in range(self.n)]\n\
    \        for i in range(self.n):\n            member[self.leader(i)].append(i)\n\
    \        return member\n\n    def size(self, a: int) -> int:\n        return -self.p[self.leader(a)]\n\
    \n\ndef main() -> None:\n    N, M = map(int, input().split())\n\n    UF = UnionFind(N)\n\
    \n    for _ in range(m):\n        A, B = map(lambda x: int(x) - 1,input().split())\n\
    \        UF.merge(A, B)\n\n    ans = 0\n    for i in range(N):\n        ans =\
    \ max(ans, UF.size(i))\n\n    print(ans)\n\n\nif __name__ == \"__main__\":\n \
    \   main()"
  dependsOn: []
  isVerificationFile: false
  path: Tree/UnionFindTree.py
  requiredBy: []
  timestamp: '2024-04-23 12:17:37+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/yosupo/DataStructure/Unionfind.test.py
  - Test/AOJ/DSL/DSL_1_A.test.py
documentation_of: Tree/UnionFindTree.py
layout: document
redirect_from:
- /library/Tree/UnionFindTree.py
- /library/Tree/UnionFindTree.py.html
title: Tree/UnionFindTree.py
---
