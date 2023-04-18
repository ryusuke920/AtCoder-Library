---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc217/submissions/32096323
    - https://atcoder.jp/contests/abc217/tasks/abc217_d
    - https://atcoder.jp/contests/abc260/submissions/33353118
    - https://atcoder.jp/contests/abc260/tasks/abc260_d
    - https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
    - https://qiita.com/tatyam/items/492c70ac4c955c055602
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# 99.99% tatyam \u3055\u3093\u304C\u516C\u958B\u3055\u308C\u3066\u3044\u308B\
    \ SortedSet \u3092\u4F7F\u7528\u3057\u3066\u3044\u307E\u3059\n# \u4E00\u90E8\u81EA\
    \u5206\u7528\u306B\u5909\u63DB\u3057\u3066\u3044\u307E\u3059\n\n# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py\n\
    \n# https://qiita.com/tatyam/items/492c70ac4c955c055602\n\n'''\n\u4F7F\u7528\u4F8B\
    \n\nABC217-D - CuttingWoods https://atcoder.jp/contests/abc217/tasks/abc217_d\n\
    https://atcoder.jp/contests/abc217/submissions/32096323\n\nABC260-D - Draw Your\
    \ Cards https://atcoder.jp/contests/abc260/tasks/abc260_d\nhttps://atcoder.jp/contests/abc260/submissions/33353118\n\
    '''\n\nfrom math import ceil, sqrt\nfrom bisect import bisect_left, bisect_right\n\
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List\nT = TypeVar('T')\n\
    \nclass SortedSet(Generic[T]):\n    BUCKET_RATIO = 50\n    REBUILD_RATIO = 170\n\
    \n    def _build(self, a=None) -> None:\n        \"Evenly divide `a` into buckets.\"\
    \n        if a is None:\n            a = list(self)\n        size = self.size\
    \ = len(a)\n        bucket_size = int(ceil(sqrt(size / self.BUCKET_RATIO)))\n\
    \        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size]\
    \ for i in range(bucket_size)]\n    \n\n    def __init__(self, a: Iterable[T]\
    \ = []) -> None:\n        \"Make a new SortedSet from iterable. / O(N) if sorted\
    \ and unique / O(N log N)\"\n        a = list(a)\n        if not all(a[i] < a[i\
    \ + 1] for i in range(len(a) - 1)):\n            a = sorted(set(a))\n        self._build(a)\n\
    \n\n    def __iter__(self) -> Iterator[T]:\n        for i in self.a:\n       \
    \     for j in i:\n                yield j\n\n\n    def __reversed__(self) ->\
    \ Iterator[T]:\n        for i in reversed(self.a):\n            for j in reversed(i):\n\
    \                yield j\n\n\n    def __len__(self) -> int:\n        return self.size\n\
    \n\n    def __repr__(self) -> str:\n        return \"SortedSet\" + str(self.a)\n\
    \n\n    def __str__(self) -> str:\n        s = str(list(self))\n        return\
    \ \"{\" + s[1 : len(s) - 1] + \"}\"\n\n\n    def _find_bucket(self, x: T) -> List[T]:\n\
    \        \"Find the bucket which should contain x. self must not be empty.\"\n\
    \        for a in self.a:\n            if x <= a[-1]:\n                return\
    \ a\n    \n        return a\n\n\n    def __contains__(self, x: T) -> bool:\n \
    \       if self.size == 0:\n            return False\n\n        a = self._find_bucket(x)\n\
    \        i = bisect_left(a, x)\n\n        return i != len(a) and a[i] == x\n\n\
    \n    def add(self, x: T) -> bool:\n        \"Add an element and return True if\
    \ added. / O(\u221AN)\"\n        if self.size == 0:\n            self.a = [[x]]\n\
    \            self.size = 1\n            return True\n\n        a = self._find_bucket(x)\n\
    \        i = bisect_left(a, x)\n\n        if i != len(a) and a[i] == x: \n   \
    \         return False\n\n        a.insert(i, x)\n        self.size += 1\n   \
    \     if len(a) > len(self.a) * self.REBUILD_RATIO:\n            self._build()\n\
    \n        return True\n\n\n    def discard(self, x: T) -> bool:\n        \"Remove\
    \ an element and return True if removed. / O(\u221AN)\"\n        if self.size\
    \ == 0:\n            return False\n\n        a = self._find_bucket(x)\n      \
    \  i = bisect_left(a, x)\n\n        if i == len(a) or a[i] != x:\n           \
    \ return False\n\n        a.pop(i)\n        self.size -= 1\n\n        if len(a)\
    \ == 0:\n            self._build()\n\n        return True\n\n \n    def lt(self,\
    \ x: T) -> Union[T, None]:\n        \"Find the largest element < x, or None if\
    \ it doesn't exist.\"\n        for a in reversed(self.a):\n            if a[0]\
    \ < x:\n                return a[bisect_left(a, x) - 1]\n\n\n    def le(self,\
    \ x: T) -> Union[T, None]:\n        \"Find the largest element <= x, or None if\
    \ it doesn't exist.\"\n        for a in reversed(self.a):\n            if a[0]\
    \ <= x:\n                return a[bisect_right(a, x) - 1]\n\n\n    def gt(self,\
    \ x: T) -> Union[T, None]:\n        \"Find the smallest element > x, or None if\
    \ it doesn't exist.\"\n        for a in self.a:\n            if a[-1] > x:\n \
    \               return a[bisect_right(a, x)]\n\n\n    def ge(self, x: T) -> Union[T,\
    \ None]:\n        \"Find the smallest element >= x, or None if it doesn't exist.\"\
    \n        for a in self.a:\n            if a[-1] >= x:\n                return\
    \ a[bisect_left(a, x)]\n\n\n    def __getitem__(self, x: int) -> T:\n        \"\
    Return the x-th element, or IndexError if it doesn't exist.\"\n        if x <\
    \ 0:\n            x += self.size\n\n        if x < 0:\n            raise IndexError\n\
    \n        for a in self.a:\n            if x < len(a):\n                return\
    \ a[x]\n            x -= len(a)\n\n        raise IndexError\n\n\n    def index(self,\
    \ x: T) -> int:\n        \"Count the number of elements < x.\"\n        ans =\
    \ 0\n        for a in self.a:\n            if a[-1] >= x:\n                return\
    \ ans + bisect_left(a, x)\n            ans += len(a)\n\n        return ans\n\n\
    \n    def index_right(self, x: T) -> int:\n        \"Count the number of elements\
    \ <= x.\"\n        ans = 0\n        for a in self.a:\n            if a[-1] > x:\n\
    \                return ans + bisect_right(a, x)\n            ans += len(a)\n\n\
    \        return ans"
  dependsOn: []
  isVerificationFile: false
  path: MathLibrary/SortedSet.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MathLibrary/SortedSet.py
layout: document
redirect_from:
- /library/MathLibrary/SortedSet.py
- /library/MathLibrary/SortedSet.py.html
title: MathLibrary/SortedSet.py
---
