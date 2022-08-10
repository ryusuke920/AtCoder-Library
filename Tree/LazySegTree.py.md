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
  code: "\"\"\"\n\u301Csegfunc\u306E\u4F7F\u3044\u65B9\u306B\u3064\u3044\u3066\u301C\
    \nupdate(k, x): k\u756A\u76EE\u306E\u8981\u7D20\u3092x\u306B\u66F4\u65B0\u3059\
    \u308B\nquery(l, r): [l, r)\uFF08l <= k < r \u306E\u533A\u9593\uFF09\u304B\u3089\
    \u5024k\u3092\u53D6\u5F97\u3059\u308B\n\"\"\"\ndef segfunc(x: int, y: int) ->\
    \ int:\n    \"\u3053\u3053\u3067\u6C42\u3081\u305F\u3044\u51E6\u7406\u3092\u884C\
    \u3046, max(x, y) \u3084 x ^ y \u306A\u3069\"\n    return x ^ y\n\n\"\"\"\n\u301C\
    \u5358\u4F4D\u5143\u306E\u4E00\u89A7\u306B\u3064\u3044\u3066\u301C\n\u6700\u5C0F\
    \u5024\uFF1Afloat(\"inf\")\n\u6700\u5927\u5024\uFF1A-float(\"inf\")\nXOR\uFF1A\
    0\n\u533A\u9593\u548C\uFF1A0\n\u533A\u9593\u7A4D\uFF1A1\n\u6700\u5927\u516C\u7D04\
    \u6570\uFF1A0\n\"\"\"\nide_ele = 0 # \u521D\u671F\u5024\uFF08\u5358\u4F4D\u5143\
    \uFF09\u306E\u8A2D\u5B9A\n\nclass LazySegmentTree:\n    def __init__(self, init_val,\
    \ segfunc, ide_ele):\n        n = len(init_val)\n        self.segfunc = segfunc\n\
    \        self.ide_ele = ide_ele\n        self.num = 1 << (n - 1).bit_length()\n\
    \        self.data = [ide_ele] * 2 * self.num\n        self.lazy = [None] * 2\
    \ * self.num\n        for i in range(n):\n            self.data[self.num + i]\
    \ = init_val[i]\n        for i in range(self.num - 1, 0, -1):\n            self.data[i]\
    \ = self.segfunc(self.data[2 * i], self.data[2 * i + 1])\n\n    def gindex(self,\
    \ l, r):\n        l += self.num\n        r += self.num\n        lm = l >> (l &\
    \ -l).bit_length()\n        rm = r >> (r & -r).bit_length()\n        while l <\
    \ r:\n            if l <= lm:\n                yield l\n            if r <= rm:\n\
    \                yield r\n            r >>= 1\n            l >>= 1\n        while\
    \ l:\n            yield l\n            l >>= 1\n\n    def propagates(self, *ids):\n\
    \        for i in reversed(ids):\n            v = self.lazy[i]\n            if\
    \ v is None:\n                continue\n            self.lazy[2 * i] = v\n   \
    \         self.lazy[2 * i + 1] = v\n            self.data[2 * i] = v\n       \
    \     self.data[2 * i + 1] = v\n            self.lazy[i] = None\n\n    def update(self,\
    \ l, r, x):\n        *ids, = self.gindex(l, r)\n        self.propagates(*ids)\n\
    \        l += self.num\n        r += self.num\n        while l < r:\n        \
    \    if l & 1:\n                self.lazy[l] = x\n                self.data[l]\
    \ = x\n                l += 1\n            if r & 1:\n                self.lazy[r\
    \ - 1] = x\n                self.data[r - 1] = x\n            r >>= 1\n      \
    \      l >>= 1\n        for i in ids:\n            self.data[i] = self.segfunc(self.data[2\
    \ * i], self.data[2 * i + 1])\n\n    def query(self, l, r):\n        *ids, = self.gindex(l,\
    \ r)\n        self.propagates(*ids)\n        res = self.ide_ele\n        l +=\
    \ self.num\n        r += self.num\n        while l < r:\n            if l & 1:\n\
    \                res = self.segfunc(res, self.data[l])\n                l += 1\n\
    \            if r & 1:\n                res = self.segfunc(res, self.data[r -\
    \ 1])\n            l >>= 1\n            r >>= 1\n        return res\n\n# \u308F\
    \u304B\u3089\u306A\u304F\u306A\u3063\u305F\u3089\u5178\u578B90\u554F\u306E29\u3092\
    \u53C2\u8003\u306B\u3059\u308B\u3053\u3068"
  dependsOn: []
  isVerificationFile: false
  path: Tree/LazySegTree.py
  requiredBy: []
  timestamp: '2022-02-06 18:58:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/LazySegTree.py
layout: document
redirect_from:
- /library/Tree/LazySegTree.py
- /library/Tree/LazySegTree.py.html
title: Tree/LazySegTree.py
---
