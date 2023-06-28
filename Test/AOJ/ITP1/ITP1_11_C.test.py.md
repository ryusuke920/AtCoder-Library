---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_C&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_C&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_C&lang=ja\n\
    \nimport sys\nsys.path.append(\"../../../\")\n\nfrom Math import Dice\nfrom random\
    \ import randint\n\ndef main() -> None:\n\n    up_1, front_1, right_1, left_1,\
    \ back_1, down_1 = map(int, input().split())\n    up_2, front_2, right_2, left_2,\
    \ back_2, down_2 = map(int, input().split())\n\n    # \u30B5\u30A4\u30B3\u30ED\
    \u306E\u76EE\u304C 1~6 \u3067\u306F\u306A\u3044\u5834\u5408\u306B\u7F6E\u304D\u63DB\
    \u3048\u308B\n    replace_dice1, replace_dice2 = {}, {}\n    replace_dice1[f\"\
    {up_1}-1\"], replace_dice2[f\"{up_2}-1\"] = 1, 1\n    replace_dice1[f\"{front_1}-2\"\
    ], replace_dice2[f\"{front_2}-2\"] = 2, 2\n    replace_dice1[f\"{right_1}-3\"\
    ], replace_dice2[f\"{right_2}-3\"] = 3, 3\n    replace_dice1[f\"{left_1}-4\"],\
    \ replace_dice2[f\"{left_2}-4\"] = 4, 4\n    replace_dice1[f\"{back_1}-5\"], replace_dice2[f\"\
    {back_2}-5\"] = 5, 5\n    replace_dice1[f\"{down_1}-6\"], replace_dice2[f\"{down_2}-6\"\
    ] = 6, 6\n\n    # \u7F6E\u304D\u63DB\u3048\u305F\u5834\u5408\u306B\u5FA9\u5143\
    \u3059\u308B\u7528\u306E\u8F9E\u66F8\n    restoration_dice1, restoration_dice2\
    \ = {}, {}\n    restoration_dice1[1], restoration_dice2[1] = up_1, up_2\n    restoration_dice1[2],\
    \ restoration_dice2[2] = front_1, front_2\n    restoration_dice1[3], restoration_dice2[3]\
    \ = right_1, right_2\n    restoration_dice1[4], restoration_dice2[4] = left_1,\
    \ left_2\n    restoration_dice1[5], restoration_dice2[5] = back_1, back_2\n  \
    \  restoration_dice1[6], restoration_dice2[6] = down_1, down_2\n\n    # u,d,f,b,l,r\
    \ \u3092\u305D\u308C\u305E\u308C 0,1,2,3,4,5 \u3068\u3057\u3066 state1,state2\
    \ \u306B\u6307\u5B9A\n    # value1,value2 \u306F\u305D\u308C\u305E\u308C state1,\
    \ state2 \u306B\u5BFE\u5FDC\u3059\u308B\u9762\u306E\u76EE\n\n    dice1 = Dice.Dice(0,\
    \ replace_dice1[f\"{up_1}-1\"], 2, replace_dice1[f\"{front_1}-2\"], 0, 0)\n  \
    \  dice2 = Dice.Dice(0, replace_dice2[f\"{up_2}-1\"], 2, replace_dice2[f\"{front_2}-2\"\
    ], 0, 0)\n\n    check = False\n    for _ in range(1000):\n        p = randint(0,\
    \ 3)\n        if p == 0:\n            dice1.RotateN()\n        if p == 1:\n  \
    \          dice1.RotateS()\n        if p == 2:\n            dice1.RotateW()\n\
    \        if p == 3:\n            dice1.RotateE()\n\n        is_ok = True\n   \
    \     for i in range(6):\n            if restoration_dice1[dice1.status()[i]]\
    \ != restoration_dice2[dice2.status()[i]]:\n                is_ok = False\n  \
    \      \n        if is_ok:\n            check = True\n\n    print(\"Yes\") if\
    \ check else print(\"No\")\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: true
  path: Test/AOJ/ITP1/ITP1_11_C.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: Test/AOJ/ITP1/ITP1_11_C.test.py
layout: document
redirect_from:
- /verify/Test/AOJ/ITP1/ITP1_11_C.test.py
- /verify/Test/AOJ/ITP1/ITP1_11_C.test.py.html
title: Test/AOJ/ITP1/ITP1_11_C.test.py
---
