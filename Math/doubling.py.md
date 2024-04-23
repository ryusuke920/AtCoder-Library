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
  code: "class Doubling():\n    def __init__(self, n, k_max, f) -> None:\n       \
    \ \"\"\"\u8981\u7D20\u6570n\u306E\u30C0\u30D6\u30EA\u30F3\u30B0\u30C6\u30FC\u30D6\
    \u30EB\u3092\u4F5C\u6210\u3057\u307E\u3059\u3002\"\"\"\n\n        k_bits = k_max.bit_length()\n\
    \n        # dub[i][j] = \u5024j\u30922**i\u56DE\u64CD\u4F5C\u3057\u305F\u7D50\u679C\
    \n        dub = [[0] * n for _ in range(k_bits)]\n\n        # 1\u56DE(2**0\u56DE\
    )\u64CD\u4F5C\u3057\u305F\u7D50\u679C\u3092\u4F5C\u6210\n        for j in range(n):\n\
    \            dub[0][j] = f(j)\n\n        # 2**i\u56DE\u64CD\u4F5C\u3057\u305F\u7D50\
    \u679C\u3092\u9806\u306B\u4F5C\u6210\n        # 2**(i-1)\u56DE\u64CD\u4F5C\u3092\
    2\u56DE\u3059\u308C\u30702**i\u56DE\u64CD\u4F5C\u3057\u305F\u3053\u3068\u306B\u306A\
    \u308B\n        for i in range(1, k_bits):\n            for j in range(n):\n \
    \               dub[i][j] = dub[i - 1][dub[i - 1][j]]\n\n        self.doubling_table\
    \ = dub\n\n    def get(self, x, k):\n        \"\"\"x\u3092k\u56DE\u64CD\u4F5C\u3057\
    \u305F\u5024\u3092\u53D6\u5F97\u3057\u307E\u3059\u3002\"\"\"\n        # k\u3092\
    \u30D3\u30C3\u30C8\u3054\u3068\u306B\u5206\u89E3\u3057\u3066\u30012**a + 2**b\
    \ + 2**c + ... \u306E\u5F62\u3067\u8003\u3048\u308B\u3002\n        # x\u30922**a\u56DE\
    \u64CD\u4F5C\u3057\u305F\u7D50\u679C\u30922**b\u56DE\u64CD\u4F5C\u3057\u305F\u7D50\
    \u679C\u30922**c\u56DE\u64CD\u4F5C\u2026 \u306E\u3088\u3046\u306B\u9806\u306B\u9069\
    \u7528\u3059\u308B\n        now = x\n        for i in range(k.bit_length()):\n\
    \            if k>>i & 1:\n                now = self.doubling_table[i][now]\n\
    \n        return now\n\ndef calc():\n    \"\u95A2\u6570\u3092\u5B9A\u7FA9\u3059\
    \u308B\"\n    return\n\nn, k = map(int,input().split())\n# n\u306E\u6700\u5927\
    \u5024, k\u56DE, \u95A2\u6570\ndub = Doubling(10 ** 5, k, calc)\n\n# n\u3092k\u56DE\
    \u7E70\u308A\u8FD4\u3057\u305F\u5148\nprint(dub.get(n, k))"
  dependsOn: []
  isVerificationFile: false
  path: Math/doubling.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/doubling.py
layout: document
redirect_from:
- /library/Math/doubling.py
- /library/Math/doubling.py.html
title: Math/doubling.py
---
