---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/yosupo/DataStructure/StaticRMQ.test.py
    title: Test/yosupo/DataStructure/StaticRMQ.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\n\u301Csegfunc\u306E\u4F7F\u3044\u65B9\u306B\u3064\u3044\u3066\u301C\
    \nupdate(k, x): k\u756A\u76EE\u306E\u8981\u7D20\u3092x\u306B\u66F4\u65B0\u3059\
    \u308B\nquery(l, r): [l, r)\uFF08l <= k < r \u306E\u533A\u9593\uFF09\u304B\u3089\
    \u5024k\u3092\u53D6\u5F97\u3059\u308B\n\"\"\"\n\nclass SegTree:\n    def __init__(self,\
    \ init_val, ide_ele) -> None:\n        self.ide_ele = ide_ele\n        self.n\
    \ = len(init_val)\n        self.num = 2 ** self.n.bit_length()\n        self.seg\
    \ = [self.ide_ele] * 2 * self.num\n        for i in range(self.n):\n         \
    \   self.seg[i + self.num - 1] = init_val[i]\n        for i in range(self.num\
    \ - 2, -1, -1):\n            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2\
    \ * i + 2])\n\n\n    def segfunc(self, x: int, y: int) -> int:\n        return\
    \ min(x, y)\n\n\n    def update(self, k: int, x: int) -> None:\n        k += self.num\
    \ - 1\n        self.seg[k] = self.segfunc(self.seg[k], x)\n        while k:\n\
    \            k = (k - 1) // 2\n            self.seg[k] = self.segfunc(self.seg[k\
    \ * 2 + 1], self.seg[k * 2 + 2])\n\n\n    def query(self, l: int, r: int):\n \
    \       if r <= l:\n            return self.ide_ele\n        l += self.num - 1\n\
    \        r += self.num - 2\n        res = self.ide_ele\n        while r - l >\
    \ 1:\n            if l & 1 == 0:\n                res = self.segfunc(res, self.seg[l])\n\
    \            if r & 1 == 1:\n                res = self.segfunc(res, self.seg[r])\n\
    \                r -= 1\n            l = l // 2\n            r = (r - 1) // 2\n\
    \        if l == r:\n            res = self.segfunc(res, self.seg[l])\n      \
    \  else:\n            res = self.segfunc(res, self.segfunc(self.seg[l], self.seg[r]))\n\
    \    \n        return res"
  dependsOn: []
  isVerificationFile: false
  path: Tree/RangeMinimamQuery.py
  requiredBy: []
  timestamp: '2022-08-09 15:54:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/yosupo/DataStructure/StaticRMQ.test.py
documentation_of: Tree/RangeMinimamQuery.py
layout: document
redirect_from:
- /library/Tree/RangeMinimamQuery.py
- /library/Tree/RangeMinimamQuery.py.html
title: Tree/RangeMinimamQuery.py
---
