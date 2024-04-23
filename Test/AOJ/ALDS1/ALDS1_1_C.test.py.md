---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Math/PrimaryCheck.py
    title: Math/PrimaryCheck.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import PrimaryCheck\n\
    \ndef main() -> None:\n    ans = 0\n\n    n = int(input())\n    for _ in range(n):\n\
    \        ans += int(PrimaryCheck.PrimaryCheck(int(input())))\n    \n    print(ans)\n\
    \n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - Math/PrimaryCheck.py
  isVerificationFile: true
  path: Test/AOJ/ALDS1/ALDS1_1_C.test.py
  requiredBy: []
  timestamp: '2023-06-29 17:50:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ALDS1/ALDS1_1_C.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ALDS1/ALDS1_1_C.test.py
- /verify/Test/AOJ/ALDS1/ALDS1_1_C.test.py.html
title: Test/AOJ/ALDS1/ALDS1_1_C.test.py
---
