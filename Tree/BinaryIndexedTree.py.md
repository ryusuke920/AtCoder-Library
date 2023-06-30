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
  code: "\"\"\"\nBIT\u3092\u884C\u3063\u305F\u5F8C\u306E\u6570\u5217\u306F\u6607\u9806\
    \u306B\u306A\u308B\u306E\u3067\u6CE8\u610F\uFF01\n\"\"\"\nimport copy\n\ndef BIT(A:\
    \ list) -> int:\n    \"\u8EE2\u5012\u6570\u3092\u6C42\u3081\u308B\"\n    cnt =\
    \ 0\n    n = len(A)\n    if n > 1:\n        A1 = A[: n >> 1]\n        A2 = A[n\
    \ >> 1 :]\n        cnt += BIT(A1)\n        cnt += BIT(A2)\n        i1, i2 = 0,\
    \ 0\n        for i in range(n):\n            if i2 == len(A2):\n             \
    \   A[i] = A1[i1]\n                i1 += 1\n            elif i1 == len(A1):\n\
    \                A[i] = A2[i2]\n                i2 += 1\n            elif A1[i1]\
    \ <= A2[i2]:\n                A[i] = A1[i1]\n                i1 += 1\n       \
    \     else:\n                A[i] = A2[i2]\n                i2 += 1\n        \
    \        cnt += n // 2 - i1\n\n    return cnt\n\n\ndef main() -> None:\n    a\
    \ = [2, 15, 23, 32, 7, 19]\n    x = copy.copy(a)\n    ans = BIT(x)\n    print(ans)\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Tree/BinaryIndexedTree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/BinaryIndexedTree.py
layout: document
redirect_from:
- /library/Tree/BinaryIndexedTree.py
- /library/Tree/BinaryIndexedTree.py.html
title: Tree/BinaryIndexedTree.py
---
