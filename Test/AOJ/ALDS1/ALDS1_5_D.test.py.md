---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Tree import BinaryIndexedTree\n\
    import copy\n\n\ndef main():\n    n = int(input())\n    a = list(map(int, input().split()))\n\
    \n    x = copy.copy(a)\n    print(BinaryIndexedTree.BIT(x))\n\n\nif __name__ ==\
    \ \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ALDS1/ALDS1_5_D.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ALDS1/ALDS1_5_D.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ALDS1/ALDS1_5_D.test.py
- /verify/Test/AOJ/ALDS1/ALDS1_5_D.test.py.html
title: Test/AOJ/ALDS1/ALDS1_5_D.test.py
---
