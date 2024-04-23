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
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Tree import UnionFindTree\n\
    \ndef main():\n    n, q = map(int, input().split())\n\n    uf = UnionFindTree.UnionFind(n)\n\
    \n    for _ in range(q):\n        t, u, v = map(int, input().split())\n      \
    \  if t == 0:\n            uf.merge(u, v)\n        elif t == 1:\n            print(int(uf.same(u,\
    \ v)))\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Tree/UnionFindTree.py
  isVerificationFile: true
  path: Test/yosupo/DataStructure/Unionfind.test.py
  requiredBy: []
  timestamp: '2024-04-23 12:17:37+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/yosupo/DataStructure/Unionfind.test.py
layout: document
redirect_from:
- /verify/Test/yosupo/DataStructure/Unionfind.test.py
- /verify/Test/yosupo/DataStructure/Unionfind.test.py.html
title: Test/yosupo/DataStructure/Unionfind.test.py
---
