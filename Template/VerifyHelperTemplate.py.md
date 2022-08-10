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
  code: "import sys\ninput = sys.stdin.readline\n\nfrom pathlib import Path\n\np =\
    \ Path(__file__).parts\nsys.path.append('/'.join(p[:p.index('AtCoder-Library')\
    \ + 1]))\n\nfrom Tree import UnionFindTree\n\ndef main():\n    pass\n\n\nif __name__\
    \ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Template/VerifyHelperTemplate.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Template/VerifyHelperTemplate.py
layout: document
redirect_from:
- /library/Template/VerifyHelperTemplate.py
- /library/Template/VerifyHelperTemplate.py.html
title: Template/VerifyHelperTemplate.py
---
