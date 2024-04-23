---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM  https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A&lang=ja\n\
    \n\ndef main() -> None:\n    a, b = map(int, input().split())\n    if a < b:\n\
    \        print(\"a < b\")\n    elif a > b:\n        print(\"a > b\")\n    else:\n\
    \        print(\"a == b\")\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_2_A.test.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_2_A.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_2_A.test.py
- /verify/Test/AOJ/ITP1/ITP1_2_A.test.py.html
title: Test/AOJ/ITP1/ITP1_2_A.test.py
---
