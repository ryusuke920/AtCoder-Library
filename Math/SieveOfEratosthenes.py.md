---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/Volume11/1172.test.py
    title: Test/AOJ/Volume11/1172.test.py
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/0007.test.py
    title: Test/yukicoder/0007.test.py
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/0713.test.py
    title: Test/yukicoder/0713.test.py
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
  code: "def primes(n: int) -> list:\n    \"\u7D20\u6570\u306E\u5217\u6319\u3092\u884C\
    \u3046\"\n\n    is_prime = [True] * (n + 1)\n    is_prime[0] = False\n    is_prime[1]\
    \ = False\n\n    for i in range(2, int(n ** 0.5) + 1):\n        if not is_prime[i]:\n\
    \            continue\n        for j in range(i * 2, n + 1, i):\n            is_prime[j]\
    \ = False\n\n    return [i for i, j in enumerate(is_prime) if j]\n\n\ndef main()\
    \ -> None:\n    x = primes(100)\n    print(len(x), x)\n\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Math/SieveOfEratosthenes.py
  requiredBy: []
  timestamp: '2023-06-29 01:19:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/Volume11/1172.test.py
  - Test/yukicoder/0713.test.py
  - Test/yukicoder/0007.test.py
documentation_of: Math/SieveOfEratosthenes.py
layout: document
redirect_from:
- /library/Math/SieveOfEratosthenes.py
- /library/Math/SieveOfEratosthenes.py.html
title: Math/SieveOfEratosthenes.py
---
