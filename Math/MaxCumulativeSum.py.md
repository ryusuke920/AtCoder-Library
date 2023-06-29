---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: Test/AOJ/Volume5/0516.test.py
    title: Test/AOJ/Volume5/0516.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def MaxCumulativeSum(num_array: list, k: int):\n    max_cumulative_sum =\
    \ []\n    count = 0\n    for i in range(k):\n       count += num_array[i]\n  \
    \  max_cumulative_sum.append([count, 0, 0 + k])\n \n    for i in range(len(num_array)\
    \ - k):\n        count += num_array[i + k]\n        count -= num_array[i]\n  \
    \      max_cumulative_sum.append([count, i + 1, i + 1 + k])\n    \n    max_cumulative_sum.sort(key\
    \ = lambda x: x[0], reverse=True)\n    return max_cumulative_sum[0]\n\n\ndef main()\
    \ -> None:\n    a = [1, 4, -1, 9, 34, 21, -12, 31]\n    ans = MaxCumulativeSum(a,\
    \ 3) # \u914D\u5217\u30FB\u533A\u9593\u5E45\n    print(ans)\n\n\nif __name__ ==\
    \ \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Math/MaxCumulativeSum.py
  requiredBy: []
  timestamp: '2023-06-29 17:50:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - Test/AOJ/Volume5/0516.test.py
documentation_of: Math/MaxCumulativeSum.py
layout: document
redirect_from:
- /library/Math/MaxCumulativeSum.py
- /library/Math/MaxCumulativeSum.py.html
title: Math/MaxCumulativeSum.py
---
