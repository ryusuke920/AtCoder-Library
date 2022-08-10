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
  code: "def primes(n: int) -> list:\n    \"\u7D20\u6570\u306E\u5217\u6319\u3092\u884C\
    \u3046\"\n\n    is_prime = [True] * (n + 1)\n    is_prime[0] = False\n    is_prime[1]\
    \ = False\n\n    for i in range(2, int(n ** 0.5) + 1):\n        if not is_prime[i]:\n\
    \            continue\n        for j in range(i * 2, n + 1, i):\n            is_prime[j]\
    \ = False\n\n    return [i for i, j in enumerate(is_prime) if j]\n\nx = primes(100)\
    \ # \u7D20\u6570\u306E\u5168\u5217\u6319\nprint(len(x), x)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/SieveOfEratosthenes.py
  requiredBy: []
  timestamp: '2022-05-30 00:24:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/SieveOfEratosthenes.py
layout: document
redirect_from:
- /library/MathLibrary/SieveOfEratosthenes.py
- /library/MathLibrary/SieveOfEratosthenes.py.html
title: MathLibrary/SieveOfEratosthenes.py
---
