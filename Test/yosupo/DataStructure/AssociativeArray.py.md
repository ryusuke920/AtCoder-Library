---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    \nfrom collections import defaultdict\nimport sys\ninput = sys.stdin.readline\n\
    \ndef main() -> None:\n    d = defaultdict(int)\n\n    Q = int(input())\n    for\
    \ _ in range(Q):\n        query = list(map(int, input().split()))\n        if\
    \ query[0] == 0:\n            d[query[1]] = query[2]\n        elif query[0] ==\
    \ 1:\n            print(d[query[1]])\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Test/yosupo/DataStructure/AssociativeArray.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Test/yosupo/DataStructure/AssociativeArray.py
layout: document
redirect_from:
- /library/Test/yosupo/DataStructure/AssociativeArray.py
- /library/Test/yosupo/DataStructure/AssociativeArray.py.html
title: Test/yosupo/DataStructure/AssociativeArray.py
---
