---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/0002.test.py
    title: Test/yukicoder/0002.test.py
  - icon: ':heavy_check_mark:'
    path: Test/yukicoder/0847.test.py
    title: Test/yukicoder/0847.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def factorization(n: int) -> int:\n    arr, tmp = [], n\n    for i in range(2,\
    \ int(-(-n ** 0.5 // 1)) + 1):\n        if tmp % i == 0:\n            cnt = 0\n\
    \            while tmp % i == 0:\n                cnt += 1\n                tmp\
    \ //= i\n            arr.append([i, cnt])\n\n    if tmp != 1:\n        arr.append([tmp,\
    \ 1])\n\n    return arr\n\n\ndef main() -> None:\n    print(factorization(2592))\n\
    \n\nif __name__ == \"__main\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/factorization.py
  requiredBy: []
  timestamp: '2022-08-10 23:10:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/yukicoder/0847.test.py
  - Test/yukicoder/0002.test.py
documentation_of: MathLibrary/factorization.py
layout: document
redirect_from:
- /library/MathLibrary/factorization.py
- /library/MathLibrary/factorization.py.html
title: MathLibrary/factorization.py
---
