---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/1737.test.py
    title: Test/yukicoder/1737.test.py
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/847.test.py
    title: Test/yukicoder/847.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def factorization(n: int) -> int:\n    arr, tmp = [], n\n    for i in range(2,\
    \ int(-(-n ** 0.5 // 1)) + 1):\n        if tmp % i == 0:\n            cnt = 0\n\
    \            while tmp % i == 0:\n                cnt += 1\n                tmp\
    \ //= i\n            arr.append([i, cnt])\n\n    if tmp != 1:\n        arr.append([tmp,\
    \ 1])\n\n    return arr\n\n\ndef main() -> None:\n    print(factorization(2592))\n\
    \n\nif __name__ == \"__main\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/Factorization.py
  requiredBy: []
  timestamp: '2022-08-11 00:02:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/yukicoder/1737.test.py
  - Test/yukicoder/847.test.py
documentation_of: MathLibrary/Factorization.py
layout: document
redirect_from:
- /library/MathLibrary/Factorization.py
- /library/MathLibrary/Factorization.py.html
title: MathLibrary/Factorization.py
---
