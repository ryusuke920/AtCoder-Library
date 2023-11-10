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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def CC(A: list) -> list:\n    \"\u5EA7\u6A19\u5727\u7E2E\"\n    B = {j: i\
    \ + 1 for i, j in enumerate(sorted(set(A)))}\n    return B\n\nx = [2, 5, 1, 21,\
    \ 312, 23, 21]\nans = CC(x)\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: String/CoordinateCompression.py
  requiredBy: []
  timestamp: '2022-05-22 23:05:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/CoordinateCompression.py
layout: document
redirect_from:
- /library/String/CoordinateCompression.py
- /library/String/CoordinateCompression.py.html
title: String/CoordinateCompression.py
---
