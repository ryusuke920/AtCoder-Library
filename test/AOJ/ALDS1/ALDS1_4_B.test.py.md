---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\ndef main():\n    n = int(input())\n\
    \    s = set(list(map(int, input().split())))\n    q = int(input())\n    t = set(list(map(int,\
    \ input().split())))\n    \n    print(len(s & t))\n\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: test/AOJ/ALDS1/ALDS1_4_B.test.py
  requiredBy: []
  timestamp: '2022-08-09 16:25:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/AOJ/ALDS1/ALDS1_4_B.test.py
layout: document
redirect_from:
- /verify/test/AOJ/ALDS1/ALDS1_4_B.test.py
- /verify/test/AOJ/ALDS1/ALDS1_4_B.test.py.html
title: test/AOJ/ALDS1/ALDS1_4_B.test.py
---
