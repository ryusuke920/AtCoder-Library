---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja\n\
    \nfrom statistics import stdev\n\ndef main():\n    while True:\n        n = int(input())\n\
    \        if n == 0:\n            exit()\n        print(stdev(list(map(int, input().split()))))\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ITP1/ALDS1_10_C.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ALDS1_10_C.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ALDS1_10_C.test.py
- /verify/Test/AOJ/ITP1/ALDS1_10_C.test.py.html
title: Test/AOJ/ITP1/ALDS1_10_C.test.py
---
