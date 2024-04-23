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
  code: "# \u3080\u305A\u3044\nfrom collections import deque\n\ndef SlideMinAlgorithm(a:\
    \ list, k: int) -> list:\n    n = len(a)\n    ans = [-1] * (n - k + 1)\n    q\
    \ = deque()\n    q.append((a[0], 0))\n    for i in range(1, k):\n        if q[0][0]\
    \ < a[i]:\n            q.appendleft((a[i], i))\n    ans[0] = q[0][0]\n\n    for\
    \ i in range(1, n - k + 1):\n        if q[0][1] < i:\n            q.popleft()\n\
    \        while q:\n            if q[-1][0] >= a[i + k - 1]:\n                q.pop()\n\
    \            else:\n                break\n        q.append((a[i + k - 1], i +\
    \ k - 1))\n        ans[i] = q[0][0]\n\n    return ans\n\n\ndef main() -> None:\n\
    \    a = [3, 1, 4, 1, 5, 9, 2, 6, 5]\n    print(SlideMinAlgorithm(a, 4))\n\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: DP/SlideMaxAlgorithm.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DP/SlideMaxAlgorithm.py
layout: document
redirect_from:
- /library/DP/SlideMaxAlgorithm.py
- /library/DP/SlideMaxAlgorithm.py.html
title: DP/SlideMaxAlgorithm.py
---
