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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def RLE(S: str) -> list:\n    tmp, cnt, ans = S[0], 1, []\n    for i in range(1,\
    \ len(S)):\n        if tmp == S[i]:\n            cnt += 1\n        else:\n   \
    \         ans.append((tmp, cnt))\n            tmp = S[i]\n            cnt = 1\n\
    \n    ans.append((tmp, cnt))\n\n    return ans\n\ns = \"RRRLLRLRRLLLLRLRLRR\"\n\
    print(*RLE(s), sep=\"\\n\")"
  dependsOn: []
  isVerificationFile: false
  path: String/RunLengthEncoding.py
  requiredBy: []
  timestamp: '2022-05-30 00:14:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/RunLengthEncoding.py
layout: document
redirect_from:
- /library/String/RunLengthEncoding.py
- /library/String/RunLengthEncoding.py.html
title: String/RunLengthEncoding.py
---
