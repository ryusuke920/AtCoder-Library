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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def LCS(S, T):\n    L1 = len(S)\n    L2 = len(T)\n    dp = [[0] * (L2 + 1)\
    \ for i in range(L1 + 1)]\n\n    for i in range(L1 - 1, -1, -1):\n        for\
    \ j in range(L2 - 1, -1, -1):\n            r = max(dp[i + 1][j], dp[i][j + 1])\n\
    \            if S[i] == T[j]:\n                r = max(r, dp[i + 1][j + 1] + 1)\n\
    \            dp[i][j] = r\n    # dp[0][0] \u304C\u9577\u3055\u306E\u89E3\n\n \
    \   # \u3053\u3053\u304B\u3089\u306F\u5FA9\u5143\u51E6\u7406\n    res = []\n \
    \   i = 0; j = 0\n    while i < L1 and j < L2:\n        if S[i] == T[j]:\n   \
    \         res.append(S[i])\n            i += 1; j += 1\n        elif dp[i][j]\
    \ == dp[i + 1][j]:\n            i += 1\n        elif dp[i][j] == dp[i][j + 1]:\n\
    \            j += 1\n    return \"\".join(res)\n\nprint(LCS(\"asdcsascsadsd\"\
    , \"assdcascdascasca\"))"
  dependsOn: []
  isVerificationFile: false
  path: DP/LongestCommonSubsequence.py
  requiredBy: []
  timestamp: '2022-05-22 23:05:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DP/LongestCommonSubsequence.py
layout: document
redirect_from:
- /library/DP/LongestCommonSubsequence.py
- /library/DP/LongestCommonSubsequence.py.html
title: DP/LongestCommonSubsequence.py
---
