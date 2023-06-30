---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    ERROR: 1e-5
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja\n\
    # verification-helper: ERROR 1e-5\n\ndef main():\n    n = int(input())\n    x\
    \ = list(map(int, input().split()))\n    y = list(map(int, input().split()))\n\
    \n    ans = [0] * 4\n    for i in range(n):\n        ans[0] += abs(x[i] - y[i])\n\
    \        ans[1] += abs(x[i] - y[i]) ** 2\n        ans[2] += abs(x[i] - y[i]) **\
    \ 3\n        ans[3] = max(ans[3], abs(x[i] - y[i]))\n    \n    print(ans[0])\n\
    \    print(ans[1]**0.5)\n    print(ans[2]**(1/3))\n    print(ans[3])\n\n\nif __name__\
    \ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ITP1/ALDS1_10_D.test.py
  requiredBy: []
  timestamp: '2023-06-30 14:54:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ALDS1_10_D.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ALDS1_10_D.test.py
- /verify/Test/AOJ/ITP1/ALDS1_10_D.test.py.html
title: Test/AOJ/ITP1/ALDS1_10_D.test.py
---
