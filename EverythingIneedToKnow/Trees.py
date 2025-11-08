"""
Trees in Python — a hands-on mini-library
-----------------------------------------
Drop this file into a notebook or run it directly. It implements the most
commonly used tree structures and algorithms, with clear examples at the
bottom under `if __name__ == "__main__":`.

Contents
========
1) Binary tree utilities
   - TreeNode (binary)
   - build_tree_from_level_list / serialize_level
   - pretty_print
   - size, height, is_balanced, diameter
   - traversals: preorder/inorder/postorder (recursive & iterative)
   - level_order / zigzag level order
   - root_to_leaf_paths, has_path_sum
   - lowest_common_ancestor (LCA) for binary tree

2) Binary Search Tree (BST)
   - insert, search, delete
   - kth_smallest, validate_bst

3) N-ary Tree (general tree)
   - NaryNode, dfs, bfs

4) Trie (prefix tree)
   - insert, search, starts_with, delete (safe delete)

5) Heap (array-based binary min-heap via heapq)

6) Segment Tree (range sum with point update)

All code uses only the Python standard library.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Deque, Generator, Iterable, List, Optional, Tuple
from collections import deque
import heapq

# =============================================================
# 1) Binary Tree Utilities
# =============================================================

@dataclass
class TreeNode:
    val: Any
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val!r})"


def build_tree_from_level_list(values: List[Optional[Any]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list where None means 'no node'.
    Example: [1,2,3,None,4] =>
        1
       / \
      2   3
       \
        4
    """
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q: Deque[TreeNode] = deque([root])
    for a, b in zip(it, it):  # consume two children at a time
        node = q.popleft()
        if a is not None:
            node.left = TreeNode(a)
            q.append(node.left)
        if b is not None:
            node.right = TreeNode(b)
            q.append(node.right)
    return root


def serialize_level(root: Optional[TreeNode]) -> List[Optional[Any]]:
    """Serialize a tree back to level-order list (trim trailing None)."""
    if not root:
        return []
    q: Deque[Optional[TreeNode]] = deque([root])
    out: List[Optional[Any]] = []
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    # Trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out


def pretty_print(root: Optional[TreeNode]) -> None:
    """Print the tree sideways for quick visualization."""
    def _pp(node: Optional[TreeNode], indent: str, last: bool) -> None:
        if not node:
            return
        connector = "└── " if last else "├── "
        print(indent + connector + str(node.val))
        indent += "    " if last else "│   "
        children = [node.left, node.right]
        for i, child in enumerate(children):
            _pp(child, indent, i == len(children) - 1)
    _pp(root, "", True)


# --- Structural properties ----------------------------------------------------

def size(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


def height(root: Optional[TreeNode]) -> int:
    """Return the number of edges on the longest downward path (empty tree = -1)."""
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """AVL-style balance: for every node, |h(left)-h(right)| <= 1."""
    def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
        if not node:
            return True, -1
        bl, hl = dfs(node.left)
        br, hr = dfs(node.right)
        balanced = bl and br and abs(hl - hr) <= 1
        return balanced, 1 + max(hl, hr)
    return dfs(root)[0]


def diameter(root: Optional[TreeNode]) -> int:
    """Number of edges on the longest path between any two nodes."""
    best = 0
    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return -1
        hl = dfs(node.left)
        hr = dfs(node.right)
        best = max(best, hl + hr + 2)
        return 1 + max(hl, hr)
    dfs(root)
    return best


# --- Traversals ---------------------------------------------------------------

def preorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def inorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def postorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def preorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    stack = [root]
    out: List[Any] = []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out


def inorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    out: List[Any] = []
    stack: List[TreeNode] = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def postorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    stack = [root]
    out: List[Any] = []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return out[::-1]


def level_order(root: Optional[TreeNode]) -> List[List[Any]]:
    if not root:
        return []
    q: Deque[TreeNode] = deque([root])
    levels: List[List[Any]] = []
    while q:
        n = len(q)
        cur: List[Any] = []
        for _ in range(n):
            node = q.popleft()
            cur.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(cur)
    return levels


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[Any]]:
    levels = level_order(root)
    for i in range(len(levels)):
        if i % 2 == 1:
            levels[i].reverse()
    return levels


# --- Paths & sums -------------------------------------------------------------

def root_to_leaf_paths(root: Optional[TreeNode]) -> List[List[Any]]:
    out: List[List[Any]] = []
    def dfs(node: Optional[TreeNode], path: List[Any]) -> None:
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            out.append(path.copy())
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return out


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return target_sum == root.val
    return has_path_sum(root.left, target_sum - root.val) or \
           has_path_sum(root.right, target_sum - root.val)


# --- Lowest Common Ancestor ---------------------------------------------------

def lca_binary_tree(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root or root is p or root is q:
        return root
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    if left and right:
        return root
    return left or right


# =============================================================
# 2) Binary Search Tree (BST)
# =============================================================

class BST:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    @staticmethod
    def from_iterable(vals: Iterable[Any]) -> 'BST':
        bst = BST()
        for v in vals:
            bst.insert(v)
        return bst

    def search(self, key: Any) -> Optional[TreeNode]:
        cur = self.root
        while cur:
            if key == cur.val:
                return cur
            cur = cur.left if key < cur.val else cur.right
        return None

    def insert(self, key: Any) -> None:
        if not self.root:
            self.root = TreeNode(key)
            return
        cur = self.root
        while True:
            if key < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(key)
                    return
            elif key > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(key)
                    return
            else:
                return  # no duplicates

    def _delete(self, node: Optional[TreeNode], key: Any) -> Optional[TreeNode]:
        if not node:
            return None
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            # Found node: cases 0/1/2 children
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Two children: promote inorder successor
            succ_parent = node
            succ = node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            node.val = succ.val
            if succ_parent.left is succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
        return node

    def delete(self, key: Any) -> None:
        self.root = self._delete(self.root, key)

    def kth_smallest(self, k: int) -> Any:
        stack: List[TreeNode] = []
        cur = self.root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

    def validate_bst(self) -> bool:
        def dfs(node: Optional[TreeNode], low: Any, high: Any) -> bool:
            if not node:
                return True
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(self.root, None, None)


# =============================================================
# 3) N-ary Tree (General Tree)
# =============================================================

@dataclass
class NaryNode:
    val: Any
    children: List['NaryNode']

    def __repr__(self) -> str:
        return f"NaryNode({self.val!r})"


def nary_dfs(root: Optional[NaryNode]) -> List[Any]:
    out: List[Any] = []
    def dfs(node: Optional[NaryNode]):
        if not node:
            return
        out.append(node.val)
        for c in node.children:
            dfs(c)
    dfs(root)
    return out


def nary_bfs(root: Optional[NaryNode]) -> List[Any]:
    if not root:
        return []
    q: Deque[NaryNode] = deque([root])
    out: List[Any] = []
    while q:
        node = q.popleft()
        out.append(node.val)
        for c in node.children:
            q.append(c)
    return out


# =============================================================
# 4) Trie (Prefix Tree)
# =============================================================

class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word: str) -> bool:
        """Delete a word if it exists. Returns True if removed."""
        def _del(node: TrieNode, i: int) -> bool:
            if i == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            ch = word[i]
            child = node.children.get(ch)
            if not child:
                return False
            should_prune = _del(child, i + 1)
            if should_prune:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            return False
        removed = _del(self.root, 0)
        return removed


# =============================================================
# 5) Heap (Binary Min-Heap via heapq)
# =============================================================

def demo_heap(nums: Iterable[int]) -> List[int]:
    """Return numbers sorted using a heap (priority queue)."""
    h: List[int] = []
    for x in nums:
        heapq.heappush(h, x)
    out: List[int] = []
    while h:
        out.append(heapq.heappop(h))
    return out


# =============================================================
# 6) Segment Tree (Range Sum, Point Update)
# =============================================================

class SegmentTree:
    """A classic array-based segment tree for range sums.
    - build: O(n)
    - point update: O(log n)
    - range sum query: O(log n)
    """

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        # Build leaves
        self.tree[size:size + self.n] = arr[:]
        # Build internal nodes
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx: int, value: int) -> None:
        i = self.size + idx
        self.tree[i] = value
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def range_sum(self, l: int, r: int) -> int:
        """Sum on [l, r] inclusive."""
        l += self.size
        r += self.size
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]
                l += 1
            if r % 2 == 0:
                s += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return s


# =============================================================
# Usage Examples
# =============================================================
if __name__ == "__main__":
    print("\n--- Binary Tree build/serialize/pretty ---")
    root = build_tree_from_level_list([1, 2, 3, None, 4, 5, 6])
    pretty_print(root)
    print("level list:", serialize_level(root))

    print("\n--- Traversals ---")
    print("preorder(rec):  ", preorder_recursive(root))
    print("inorder(rec):   ", inorder_recursive(root))
    print("postorder(rec): ", postorder_recursive(root))
    print("preorder(iter): ", preorder_iterative(root))
    print("inorder(iter):  ", inorder_iterative(root))
    print("postorder(iter):", postorder_iterative(root))
    print("level order:    ", level_order(root))
    print("zigzag level:   ", zigzag_level_order(root))

    print("\n--- Properties ---")
    print("size:", size(root))
    print("height:", height(root))
    print("balanced?:", is_balanced(root))
    print("diameter:", diameter(root))

    print("\n--- Paths & sums ---")
    print("paths:", root_to_leaf_paths(root))
    print("has path sum (1+2+4=7)?:", has_path_sum(root, 7))

    print("\n--- LCA ---")
    # Find LCA of nodes 4 and 5
    # (Note: quick way to locate references by inorder search)
    def find(node: Optional[TreeNode], x: Any) -> Optional[TreeNode]:
        if not node:
            return None
        if node.val == x:
            return node
        return find(node.left, x) or find(node.right, x)
    n4 = find(root, 4)
    n5 = find(root, 5)
    print("LCA(4,5):", lca_binary_tree(root, n4, n5).val if n4 and n5 else None)

    print("\n--- BST ---")
    bst = BST.from_iterable([7, 3, 9, 1, 5, 8, 10])
    pretty_print(bst.root)
    print("search 5:", bst.search(5))
    print("kth_smallest(3):", bst.kth_smallest(3))
    print("valid BST?:", bst.validate_bst())
    bst.delete(7)
    print("after delete 7:")
    pretty_print(bst.root)

    print("\n--- N-ary Tree ---")
    nroot = NaryNode(1, [NaryNode(2, []), NaryNode(3, [NaryNode(4, [])])])
    print("DFS:", nary_dfs(nroot))
    print("BFS:", nary_bfs(nroot))

    print("\n--- Trie ---")
    tri = Trie()
    for w in ["cat", "car", "cart", "dog"]:
        tri.insert(w)
    print("search 'car':", tri.search("car"))
    print("starts_with 'ca':", tri.starts_with("ca"))
    tri.delete("car")
    print("search 'car' after delete:", tri.search("car"))

    print("\n--- Heap ---")
    print("heap sorted:", demo_heap([5, 1, 4, 2, 9, 0]))

    print("\n--- Segment Tree ---")
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print("sum[1,3] (3+5+7):", st.range_sum(1, 3))
    st.update(2, 6)  # arr[2]=6
    print("sum[1,3] after update (3+6+7):", st.range_sum(1, 3))
# Definition for a binary tree node.