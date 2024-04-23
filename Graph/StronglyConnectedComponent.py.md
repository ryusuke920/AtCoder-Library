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
  code: "import sys\ninput = sys.stdin.readline\n\n\"SCC\uFF08Strongly Connected Component\uFF09\
    \ := \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3\"\nclass SCC:\n    def __init__(self,\
    \ n):\n        self.n = n\n        self.graph = [[] for _ in range(n)]\n     \
    \   self.rev_graph = [[] for _ in range(n)]\n        self.labels = [-1] * n\n\
    \        self.lb_cnt = 0\n\n    def add_edge(self, v, nxt_v):\n        self.graph[v].append(nxt_v)\n\
    \        self.rev_graph[nxt_v].append(v)\n\n    def build(self):\n        self.post_order\
    \ = []\n        self.used = [False] * self.n\n        for v in range(self.n):\n\
    \            if not self.used[v]:\n                self._dfs(v)\n        for v\
    \ in reversed(self.post_order):\n            if self.labels[v] == -1:\n      \
    \          self._rev_dfs(v)\n                self.lb_cnt += 1\n\n    def _dfs(self,\
    \ v):\n        stack = [v, 0]\n        while stack:\n            v, idx = stack[-2:]\n\
    \            if not idx and self.used[v]:\n                stack.pop()\n     \
    \           stack.pop()\n            else:\n                self.used[v] = True\n\
    \                if idx < len(self.graph[v]):\n                    stack[-1] +=\
    \ 1\n                    stack.append(self.graph[v][idx])\n                  \
    \  stack.append(0)\n                else:\n                    stack.pop()\n \
    \                   self.post_order.append(stack.pop())\n\n    def _rev_dfs(self,\
    \ v):\n        stack = [v]\n        self.labels[v] = self.lb_cnt\n        while\
    \ stack:\n            v = stack.pop()\n            for nxt_v in self.rev_graph[v]:\n\
    \                if self.labels[nxt_v] != -1:\n                    continue\n\
    \                stack.append(nxt_v)\n                self.labels[nxt_v] = self.lb_cnt\n\
    \n    def construct(self):\n        self.dag = [[] for i in range(self.lb_cnt)]\n\
    \        self.groups = [[] for i in range(self.lb_cnt)]\n        for v, lb in\
    \ enumerate(self.labels):\n            for nxt_v in self.graph[v]:\n         \
    \       nxt_lb = self.labels[nxt_v]\n                if lb == nxt_lb:\n      \
    \              continue\n                self.dag[lb].append(nxt_lb)\n       \
    \     self.groups[lb].append(v)\n        return self.dag, self.groups\n\n\nn,\
    \ m = map(int, input().split()) # \u30CE\u30FC\u30C9\u6570\u30FB\u30A8\u30C3\u30B8\
    \u6570\ngraph = [list(map(int,input().split())) for _ in range(m)] # \u30A8\u30C3\
    \u30B8\u306E\u53D7\u3051\u53D6\u308A\nscc = SCC(n) # Class\u3092\u4F7F\u3048\u308B\
    \u3088\u3046\u306B\u3059\u308B\n\nfor u, v in graph:\n    scc.add_edge(u - 1,\
    \ v - 1) # \u6709\u5411\u30B0\u30E9\u30D5\u306B\u3059\u308B\uFF080index\uFF09\n\
    scc.build()\n_,elems = scc.construct() # \u9589\u8DEF\u305A\u3064\u306E\u914D\u5217\
    \u3067\u5E30\u3063\u3066\u304F\u308B\n\nprint(elems)"
  dependsOn: []
  isVerificationFile: false
  path: Graph/StronglyConnectedComponent.py
  requiredBy: []
  timestamp: '2022-02-06 19:12:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/StronglyConnectedComponent.py
layout: document
redirect_from:
- /library/Graph/StronglyConnectedComponent.py
- /library/Graph/StronglyConnectedComponent.py.html
title: Graph/StronglyConnectedComponent.py
---
