---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\n\
    def main() -> None:\n    A, B = map(int, input().split())\n    print(A + B)\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: test/yosupo/Sample/A+B.test.py
  requiredBy: []
  timestamp: '2022-08-08 22:10:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yosupo/Sample/A+B.test.py
layout: document
redirect_from:
- /verify/test/yosupo/Sample/A+B.test.py
- /verify/test/yosupo/Sample/A+B.test.py.html
title: test/yosupo/Sample/A+B.test.py
---
