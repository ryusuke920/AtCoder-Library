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
  code: "# \u3053\u306E\u30BB\u30B0\u6728\u306FPython\u3060\u3068TLE\u3059\u308B\u306E\
    \u3067PyPy\u3092\u63A8\u5968\u3057\u307E\u3059\n\n\"\"\"\n\u301Csegfunc\u306E\u4F7F\
    \u3044\u65B9\u306B\u3064\u3044\u3066\u301C\nupdate(k, x): k\u756A\u76EE\u306E\u8981\
    \u7D20\u3092x\u306B\u66F4\u65B0\u3059\u308B\nquery(l, r): [l, r)\uFF08l <= k <\
    \ r \u306E\u533A\u9593\uFF09\u304B\u3089\u5024k\u3092\u53D6\u5F97\u3059\u308B\n\
    \"\"\"\ndef segfunc(x: int, y: int) -> int:\n    \"\u3053\u3053\u3067\u6C42\u3081\
    \u305F\u3044\u51E6\u7406\u3092\u884C\u3046, max(x, y) \u3084 x ^ y \u306A\u3069\
    \"\n    return x ^ y\n\n\"\"\"\n\u301C\u5358\u4F4D\u5143\u306E\u4E00\u89A7\u306B\
    \u3064\u3044\u3066\u301C\n\u6700\u5C0F\u5024\uFF1Afloat(\"inf\")\n\u6700\u5927\
    \u5024\uFF1A-float(\"inf\")\nXOR\uFF1A0\n\u533A\u9593\u548C\uFF1A0\n\u533A\u9593\
    \u7A4D\uFF1A1\n\u6700\u5927\u516C\u7D04\u6570\uFF1A0\n\"\"\"\nide_ele = 0 # \u521D\
    \u671F\u5024\uFF08\u5358\u4F4D\u5143\uFF09\u306E\u8A2D\u5B9A\n\nclass SegTree:\n\
    \    def __init__(self, segfunc, init_val, ide_ele):\n        self.segfunc = segfunc\n\
    \        self.ide_ele = ide_ele\n        self.num = 2 ** n.bit_length()\n    \
    \    self.seg = [self.ide_ele] * 2 * self.num\n        for i in range(n):\n  \
    \          self.seg[i+self.num - 1] = init_val[i]\n        for i in range(self.num\
    \ - 2, -1, -1):\n            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2\
    \ * i + 2])\n\n    def update(self, k, x):\n        k += self.num - 1\n      \
    \  self.seg[k] = self.segfunc(self.seg[k], x)\n        while k:\n            k\
    \ = (k - 1) // 2\n            self.seg[k] = self.segfunc(self.seg[k * 2 + 1],\
    \ self.seg[k * 2 + 2])\n\n    def query(self, l, r):\n        \" l \u306F0index,\
    \ r \u306F1index\"\n        if r <= l:\n            return self.ide_ele\n    \
    \    l += self.num - 1\n        r += self.num - 2\n        res = self.ide_ele\n\
    \        while r - l > 1:\n            if l & 1 == 0:\n                res = self.segfunc(res,\
    \ self.seg[l])\n            if r & 1 == 1:\n                res = self.segfunc(res,\
    \ self.seg[r])\n                r -= 1\n            l = l // 2\n            r\
    \ = (r - 1) // 2\n        if l == r:\n            res = self.segfunc(res, self.seg[l])\n\
    \        else:\n            res = self.segfunc(res, self.segfunc(self.seg[l],\
    \ self.seg[r]))\n        return res\n\nn, q = map(int,input().split()) # \u914D\
    \u5217\u306E\u9577\u3055\u30FB\u30AF\u30A8\u30EA\u6570\na = list(map(int,input().split()))\
    \ # \u914D\u5217\nseg = SegTree(segfunc, a, ide_ele) # \u30AA\u30D6\u30B8\u30A7\
    \u30AF\u30C8\u306E\u4F5C\u6210"
  dependsOn: []
  isVerificationFile: false
  path: Tree/SegTree.py
  requiredBy: []
  timestamp: '2022-02-06 18:58:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/SegTree.py
layout: document
redirect_from:
- /library/Tree/SegTree.py
- /library/Tree/SegTree.py.html
title: Tree/SegTree.py
---
