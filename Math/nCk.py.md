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
  code: "def calc_facinv(n: int) -> list:\n    '\u9006\u5143\u30C6\u30FC\u30D6\u30EB\
    \u3092\u4F5C\u6210\u3059\u308B'\n\n    # \u968E\u4E57\u30C6\u30FC\u30D6\u30EB\u306E\
    \u4F5C\u6210\n    fac = [0] * (n + 1)\n    fac[0] = 1\n    for i in range(1, n\
    \ + 1):\n        fac[i] = fac[i - 1] * i\n        fac[i] %= mod\n    \n    # \u9006\
    \u5143\u30C6\u30FC\u30D6\u30EB\u306E\u4F5C\u6210\n    fac_inv = [0] * (n + 1)\n\
    \    fac_inv[0] = 1\n    for i in range(1, n + 1):\n        fac_inv[i] = pow(fac[i],\
    \ mod - 2, mod)\n    \n    return fac, fac_inv\n\ndef combination(n: int, k: int)\
    \ -> int:\n    '''nCk\u3092\u8A08\u7B97\u3059\u308B'''\n\n    return fac[n] *\
    \ fac_inv[k] * fac_inv[n - k] % mod\n\ndef main() -> None:\n\n    n, k = map(int,\
    \ input().split())\n\n    mod = 10 ** 9 + 7\n    fac, fac_inv = calc_facinv(n)\n\
    \n    ans = combination(n, k)\n    print(ans)\n\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: Math/nCk.py
  requiredBy: []
  timestamp: '2023-06-29 00:35:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Math/nCk.py
layout: document
redirect_from:
- /library/Math/nCk.py
- /library/Math/nCk.py.html
title: Math/nCk.py
---
