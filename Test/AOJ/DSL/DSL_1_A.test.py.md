---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Tree/UnionFindTree.py
    title: Tree/UnionFindTree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Tree import UnionFindTree\n\
    \ndef main():\n    n, q = map(int, input().split())\n\n    uf = UnionFindTree.UnionFind(n)\n\
    \n    for _ in range(q):\n        com, x, y = map(int, input().split())\n    \
    \    if com == 0:\n            uf.merge(x, y)\n        elif com == 1:\n      \
    \      print(int(uf.same(x, y)))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - Tree/UnionFindTree.py
  isVerificationFile: true
  path: Test/AOJ/DSL/DSL_1_A.test.py
  requiredBy: []
  timestamp: '2022-08-11 00:02:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/DSL/DSL_1_A.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/DSL/DSL_1_A.test.py
- /verify/Test/AOJ/DSL/DSL_1_A.test.py.html
title: Test/AOJ/DSL/DSL_1_A.test.py
---
