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
  code: "def FloatToInt(FLOAT):\n    return int(FLOAT.replace(\".\", \"\")), len(FLOAT)\
    \ - FLOAT.index(\".\") - 1 # tuple \u3067return\n\nn = \"314.1592653589\" # \u958B\
    \u59CB\u306Fstr\u3067\u6E21\u3059\nx, y = FloatToInt(n)\nprint(x, y)"
  dependsOn: []
  isVerificationFile: false
  path: Math/FromFloatToInt.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/FromFloatToInt.py
layout: document
redirect_from:
- /library/Math/FromFloatToInt.py
- /library/Math/FromFloatToInt.py.html
title: Math/FromFloatToInt.py
---
