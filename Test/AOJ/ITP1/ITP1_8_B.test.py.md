---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Math/DigitSum_int.py
    title: Math/DigitSum_int.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import DigitSum_int\n\
    \ndef main() -> None:\n    while True:\n        n = int(input())\n        if n\
    \ == 0:\n            exit()\n        \n        print(DigitSum_int.DigitSum(n))\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Math/DigitSum_int.py
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_8_B.test.py
  requiredBy: []
  timestamp: '2023-06-30 09:44:00+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_8_B.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_8_B.test.py
- /verify/Test/AOJ/ITP1/ITP1_8_B.test.py.html
title: Test/AOJ/ITP1/ITP1_8_B.test.py
---
