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
  code: "def primes_list(n):\n    \"\"\"\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\
    \u306E\u7BE9\u3067n\u4EE5\u4E0B\u306E\u7D20\u6570\u3092\u5168\u5217\u6319\u3059\
    \u308B\"\"\"\n    if n == 0:\n        return []\n    is_prime = [True] * (n +\
    \ 1)\n    is_prime[0] = False\n    is_prime[1] = False\n    for i in range(2,\
    \ int(n ** 0.5) + 1):\n        if not is_prime[i]: continue\n        for j in\
    \ range(i * 2, n + 1, i):\n            is_prime[j] = False\n    return [i for\
    \ i in range(n + 1) if is_prime[i]]\n\ndef nCkFactorization(n: int, k: int) ->\
    \ list:\n    \"\"\"nCk\u306E 1,2,...,k, n,n-1,...,n-k+1\u3092\u5168\u3066\u7D20\
    \u56E0\u6570\u5206\u89E3\u3059\u308B\"\"\"\n\n    # \u5206\u5B50\n    divisors_1\
    \ = [[] for _ in range(k)]\n    a = [n - i for i in range(k)]\n    num = primes_list(int(n\
    \ ** 0.5) + 1)\n\n    for p in num:\n        for i in reversed(range(n - k + 1\
    \ + p - (n - k + 1) % p if (n - k + 1) % p != 0 else n - k + 1, n + 1, p)):\n\
    \            while a[n - i] % p == 0:\n                divisors_1[n - i].append(p)\n\
    \                a[n - i] //= p\n\n    for i in range(len(a)):\n        if a[i]\
    \ != 1:\n            divisors_1[i].append(a[i])\n\n    # \u5206\u6BCD\n    divisors_2\
    \ = [[] for _ in range(k + 1)]\n    a = [i for i in range(k + 1)]\n    num = primes_list(k)\
    \ # \u7D20\u6570\u306E\u5168\u5217\u6319\n    \n    for p in num:\n        for\
    \ i in range(p, k + 1, p):\n            while a[i] % p == 0:\n               \
    \ divisors_2[i].append(p)\n                a[i] //= p\n    \n    return divisors_1,\
    \ divisors_2\n\nx, y = nCkFactorization(100, 30)\nprint(\"\u5206\u5B50\")\nprint(*x,\
    \ sep=\"\\n\")\nprint(\"\u5206\u6BCD\")\nprint(*y, sep=\"\\n\")"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/nCkFactorization.py
  requiredBy: []
  timestamp: '2021-11-14 03:32:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/nCkFactorization.py
layout: document
redirect_from:
- /library/MathLibrary/nCkFactorization.py
- /library/MathLibrary/nCkFactorization.py.html
title: MathLibrary/nCkFactorization.py
---
