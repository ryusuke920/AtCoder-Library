---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\ndef LIS(n: int, a: list) -> int:\n    INF\
    \ = 10 ** 18\n    dp = [INF] * n\n    for i in a:\n        x = bisect_left(dp,\
    \ i)\n        dp[x] = i\n\n    return bisect_left(dp, INF)\n\nn = int(input())\n\
    a = list(map(int, input().split()))\n\ncnt = LIS(n, a)\nprint(cnt)"
  dependsOn: []
  isVerificationFile: false
  path: DP/LongestIncreasingSubsequence.py
  requiredBy: []
  timestamp: '2022-05-22 23:05:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DP/LongestIncreasingSubsequence.py
layout: document
redirect_from:
- /library/DP/LongestIncreasingSubsequence.py
- /library/DP/LongestIncreasingSubsequence.py.html
title: DP/LongestIncreasingSubsequence.py
---
