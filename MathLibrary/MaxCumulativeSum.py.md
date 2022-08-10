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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u914D\u5217\u306E\u7D2F\u7A4D\u548C\u306E\u90E8\u5206\u548C\u306E\u6700\
    \u5927\u5024\u3092\u6C42\u3081\u308B\ndef MaxCumulativeSum(num_array, k): # \u914D\
    \u5217\u30FB\u533A\u9593\u5E45\n    max_cumulative_sum = [] # \u533A\u9593\u5E45\
    \u5206\u306E\u90E8\u5206\u548C\u3092\u683C\u7D0D\u3059\u308B\u914D\u5217\n   \
    \ count = 0\n    for i in range(k):\n       count += num_array[i]\n    max_cumulative_sum.append([count,\
    \ 0, 0 + k]) # \u90E8\u5206\u548C\u30FB\u5DE6\u7AEF\u30FB\u53F3\u7AEF\n    \n\
    \    for i in range(len(num_array) - k):\n        count += num_array[i + k]\n\
    \        count -= num_array[i]\n        max_cumulative_sum.append([count, i +\
    \ 1, i + 1 + k])\n    \n    max_cumulative_sum.sort(key = lambda x: x[0], reverse\
    \ = True) # \u964D\u9806\u306B\u30BD\u30FC\u30C8\n    return max_cumulative_sum[0]\n\
    \n\na = [1, 4, -1, 9, 34, 21, -12, 31]\nans = MaxCumulativeSum(a, 3) # \u914D\u5217\
    \u30FB\u533A\u9593\u5E45\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/MaxCumulativeSum.py
  requiredBy: []
  timestamp: '2021-02-08 02:18:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/MaxCumulativeSum.py
layout: document
redirect_from:
- /library/MathLibrary/MaxCumulativeSum.py
- /library/MathLibrary/MaxCumulativeSum.py.html
title: MathLibrary/MaxCumulativeSum.py
---
