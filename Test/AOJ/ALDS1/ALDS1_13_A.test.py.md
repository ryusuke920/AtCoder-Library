---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A\n\
    \nfrom itertools import permutations\n\nk = int(input())\nrc = [list(map(int,\
    \ input().split())) for _ in range(k)]\n\nfor p in permutations(range(8)):\n \
    \   flag = True\n    for i, j in rc:\n        if p[i] != j:\n            flag\
    \ = False\n\n    if not flag:\n        continue\n\n    for k in range(8):\n  \
    \      for l in range(8):\n            if k == l:\n                continue\n\
    \            if abs(p[k] - p[l]) == abs(k - l):\n                flag = False\n\
    \n    if flag:\n        for i in p:\n            ans = [\".\"] * 8\n         \
    \   ans[i] = \"Q\"\n            print(\"\".join(ans))"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ALDS1/ALDS1_13_A.test.py
  requiredBy: []
  timestamp: '2022-08-11 00:02:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ALDS1/ALDS1_13_A.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ALDS1/ALDS1_13_A.test.py
- /verify/Test/AOJ/ALDS1/ALDS1_13_A.test.py.html
title: Test/AOJ/ALDS1/ALDS1_13_A.test.py
---
