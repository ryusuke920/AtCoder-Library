---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Tree/RangeMinimamQuery.py
    title: Tree/RangeMinimamQuery.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \nimport sys\ninput = sys.stdin.readline\n\nsys.path.append(\"../../../\")\n\n\
    from Tree import RangeMinimamQuery\n\ndef main():\n    N, Q = map(int,input().split())\n\
    \    a = list(map(int,input().split()))\n    seg = RangeMinimamQuery.SegTree(a,\
    \ float('inf'))\n\n    for _ in range(Q):\n        l, r = map(int, input().split())\n\
    \        print(seg.query(l, r))\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Tree/RangeMinimamQuery.py
  isVerificationFile: true
  path: Test/yosupo/DataStructure/StaticRMQ.test.py
  requiredBy: []
  timestamp: '2022-08-11 00:02:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/yosupo/DataStructure/StaticRMQ.test.py
layout: document
redirect_from:
- /verify/Test/yosupo/DataStructure/StaticRMQ.test.py
- /verify/Test/yosupo/DataStructure/StaticRMQ.test.py.html
title: Test/yosupo/DataStructure/StaticRMQ.test.py
---
