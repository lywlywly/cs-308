# COMPSCI 308 Design and Analysis of Algorithms Weekly Journal 4

Luyao Wang | April 14 2024

This week, we focused on Minimum Spanning Trees (MSTs) and explored two popular greedy algorithms for building MSTs: Kruskal's algorithm and Prim's algorithm.

We began by understanding the concept of MSTs, which are tree-like structures derived from **connected**, **undirected** graphs. MSTs are **acyclic** and are not unique, meaning there can be multiple valid MSTs for a given graph.

We then learned about the **generic method** for constructing MSTs using a **greedy** approach. The key idea is to start with a subset $A$ that is included in some MST and iteratively add **safe edges** to $A$. A safe edge is an edge $(u, v)$ that, when added to $A$, maintains the tree structure without creating a cycle. To determine safe edges, we explored a theorem stating that if $(u, v)$ is the **light edge** crossing a cut (S, V-S) which **respects** $A$, it is safe for $A$.

Next, we studied Kruskal's algorithm, which constructs an MST by growing a **forest** of disconnected trees. The algorithm repeatedly selects the least-weight edge that connects two distinct components of the forest. To efficiently manage the components, Kruskal's algorithm utilizes the **disjoint-set data structure (union-find)**. This algorithm guarantees the construction of an MST and has a time complexity of $O(E \log V)$, where E is the number of edges and V is the number of vertices in the graph.

Prim's algorithm builds an MST by incrementally growing a **tree** from a single vertex. At each step, the algorithm selects the least-weight edge that connects the existing tree to a vertex not yet in the tree. Prim's algorithm uses a **minimum priority queue** to efficiently identify the least-weight edges. Similar to Kruskal's algorithm, Prim's algorithm guarantees the construction of an MST and has a time complexity of $O(E \log V)$.
