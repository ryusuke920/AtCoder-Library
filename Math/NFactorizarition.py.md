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
  code: "# 2ms\u306E\u5834\u5408\u306F10^6\u307E\u3067\u884C\u3051\u308B\ndef primes_list(n):\n\
    \    \"\"\"\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\u3067n\u4EE5\
    \u4E0B\u306E\u7D20\u6570\u3092\u5168\u5217\u6319\u3059\u308B\"\"\"\n    if n ==\
    \ 0:\n        return []\n    is_prime = [True] * (n + 1)\n    is_prime[0] = False\n\
    \    is_prime[1] = False\n    for i in range(2, int(n ** 0.5) + 1):\n        if\
    \ not is_prime[i]: continue\n        for j in range(i * 2, n + 1, i):\n      \
    \      is_prime[j] = False\n    return [i for i in range(n + 1) if is_prime[i]]\n\
    \ndef nCkFactorization(k: int) -> list:\n    \"\"\"1,2, ... ,n \u3092\u5168\u3066\
    \u7D20\u56E0\u6570\u5206\u89E3\u3059\u308B\"\"\"\n\n    divisors = [[] for _ in\
    \ range(k + 1)]\n    a = [i for i in range(k + 1)]\n    num = primes_list(k)\n\
    \n    for p in num:\n        for i in range(p, k + 1, p):\n            while a[i]\
    \ % p == 0:\n                divisors[i].append(p)\n                a[i] //= p\n\
    \n    return divisors\n\nnum = nCkFactorization(100)\n#print(*num, sep=\"\\n\"\
    )\nfor i in range(len(num)):\n    print(i, num[i])"
  dependsOn: []
  isVerificationFile: false
  path: Math/NFactorizarition.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/NFactorizarition.py
layout: document
redirect_from:
- /library/Math/NFactorizarition.py
- /library/Math/NFactorizarition.py.html
title: Math/NFactorizarition.py
---
