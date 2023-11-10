---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Math/Divisor.py
    title: Math/Divisor.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import Divisor\n\ndef\
    \ main() -> None:\n    a, b, c = map(int, input().split())\n\n    ans = 0\n  \
    \  for i in Divisor.divisors(c):\n        if a <= i <= b:\n            ans +=\
    \ 1\n    \n    print(ans)\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Math/Divisor.py
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_3_D.test.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_3_D.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_3_D.test.py
- /verify/Test/AOJ/ITP1/ITP1_3_D.test.py.html
title: Test/AOJ/ITP1/ITP1_3_D.test.py
---
